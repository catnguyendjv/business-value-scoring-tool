#!/usr/bin/env python3
"""
score_batch.py — Tính Business Value Score cho nhiều ticket cùng lúc.

VAI TRÒ: chỉ làm phần số học (áp trọng số theo loại ticket, tính điểm, gán
priority lane, xác định driver, xếp hạng). Việc phân loại ticket và chấm 0–5
cho từng tiêu chí là phần phán đoán do Claude làm TRƯỚC rồi đưa điểm vào đây.
Script này KHÔNG đọc Redmine và KHÔNG tự chấm.

INPUT: đường dẫn tới 1 file JSON, là list các object:
  {
    "id": "12345",                         # mã issue Redmine (tùy chọn)
    "title": "Notification không gửi",     # tiêu đề (tùy chọn)
    "type": "Bug",                         # giá trị Redmine HOẶC model type
    "scores": {"TM":2,"KH":5,"CL":3,"VH":5,"EN":1,"RR":2},
    "hard_gate": false,                    # hoặc chuỗi lý do nếu dính hard gate
    "note": ""                             # ghi chú thiếu data / độ tin cậy (tùy chọn)
  }

OUTPUT: in ra stdout bảng Markdown đã xếp hạng + tóm tắt theo lane, để hiển
thị trực tiếp trong khung chat.

Dùng:  python score_batch.py <path-to-scores.json>
"""

import json
import sys

# Trọng số theo loại ticket của mô hình (mỗi hàng cộng = 100).
WEIGHTS = {
    "New Feature":            {"TM": 28, "KH": 23, "CL": 26, "VH": 5,  "EN": 10, "RR": 8},
    "Enhancement / Maintain": {"TM": 18, "KH": 28, "CL": 18, "VH": 13, "EN": 15, "RR": 8},
    "Bug Fix":                {"TM": 11, "KH": 24, "CL": 11, "VH": 35, "EN": 5,  "RR": 14},
    "Tech Debt":              {"TM": 5,  "KH": 5,  "CL": 15, "VH": 21, "EN": 41, "RR": 13},
    "Ops / Infra":            {"TM": 5,  "KH": 8,  "CL": 13, "VH": 43, "EN": 18, "RR": 13},
    "Security":               {"TM": 2,  "KH": 10, "CL": 13, "VH": 18, "EN": 8,  "RR": 50},
    "Research / Spike":       {"TM": 6,  "KH": 6,  "CL": 29, "VH": 12, "EN": 29, "RR": 18},
}

# Map custom field "ticket type" của Redmine → loại của mô hình.
REDMINE_MAP = {
    "Feature":        "New Feature",
    "Bug":            "Bug Fix",
    "Improvement":    "Enhancement / Maintain",
    "Refactor":       "Tech Debt",
    "Infrastructure": "Ops / Infra",
    "Spike":          "Research / Spike",
}

CRIT = ["TM", "KH", "CL", "VH", "EN", "RR"]


def resolve_type(t):
    """Chấp nhận cả giá trị Redmine lẫn tên model type (gồm 'Security')."""
    if t in WEIGHTS:
        return t
    if t in REDMINE_MAP:
        return REDMINE_MAP[t]
    raise ValueError(
        f"Loại ticket không hợp lệ: {t!r}. "
        f"Hợp lệ: {sorted(REDMINE_MAP)} hoặc {sorted(WEIGHTS)}."
    )


def lane(score):
    if score >= 80:
        return "Expedite"
    if score >= 65:
        return "High"
    if score >= 50:
        return "Medium"
    return "Backlog"


def evaluate(item):
    mtype = resolve_type(item["type"])
    w = WEIGHTS[mtype]
    s = item["scores"]
    for c in CRIT:
        v = s.get(c)
        if not isinstance(v, int) or not (0 <= v <= 5):
            raise ValueError(f"Điểm {c} của ticket {item.get('id','?')} phải là số nguyên 0–5, nhận {v!r}.")
    contrib = {c: s[c] * w[c] / 5 for c in CRIT}      # điểm đóng góp 0..weight
    total = round(sum(contrib.values()), 1)
    # driver = 2 tiêu chí đóng góp nhiều nhất
    drivers = sorted(CRIT, key=lambda c: contrib[c], reverse=True)[:2]
    hg = item.get("hard_gate")
    hg_active = bool(hg) and hg not in (False, "", "false", "False")
    return {
        "id": str(item.get("id", "")),
        "title": item.get("title", ""),
        "type": mtype,
        "scores": s,
        "total": total,
        "lane": "Expedite⚡" if hg_active else lane(total),
        "hard_gate": hg if hg_active else None,
        "drivers": drivers,
        "note": item.get("note", ""),
    }


def trunc(text, n):
    text = (text or "").replace("|", "/").replace("\n", " ").strip()
    return text if len(text) <= n else text[: n - 1] + "…"

# Tên model type viết gọn cho cột bảng
SHORT = {
    "New Feature": "Feature", "Enhancement / Maintain": "Improve", "Bug Fix": "Bug",
    "Tech Debt": "Refactor", "Ops / Infra": "Infra", "Security": "Security",
    "Research / Spike": "Spike",
}


def render(results):
    # Xếp hạng: hard gate lên đầu, sau đó theo điểm giảm dần
    results.sort(key=lambda r: (r["hard_gate"] is None, -r["total"]))

    lines = []
    # Tóm tắt theo lane
    order = ["Expedite⚡", "Expedite", "High", "Medium", "Backlog"]
    counts = {k: 0 for k in order}
    for r in results:
        counts[r["lane"]] = counts.get(r["lane"], 0) + 1
    summary = " · ".join(f"{k} {counts[k]}" for k in order if counts.get(k))
    lines.append(f"**{len(results)} ticket** — {summary}")
    lines.append("")

    # Bảng
    header = "| # | Ticket | Loại | TM | KH | CL | VH | EN | RR | Điểm | Lane | Driver | Ghi chú |"
    sep    = "|---|---|---|--:|--:|--:|--:|--:|--:|--:|---|---|---|"
    lines.append(header)
    lines.append(sep)
    for r in results:
        s = r["scores"]
        flag = []
        if r["hard_gate"]:
            flag.append(f"hard gate: {trunc(str(r['hard_gate']), 40)}")
        if r["note"]:
            flag.append(trunc(r["note"], 40))
        lines.append(
            f"| {r['id']} | {trunc(r['title'], 38)} | {SHORT.get(r['type'], r['type'])} "
            f"| {s['TM']} | {s['KH']} | {s['CL']} | {s['VH']} | {s['EN']} | {s['RR']} "
            f"| **{r['total']:.1f}** | {r['lane']} | {'·'.join(r['drivers'])} | {' / '.join(flag)} |"
        )
    return "\n".join(lines)


def main():
    if len(sys.argv) != 2:
        print("Dùng: python score_batch.py <path-to-scores.json>", file=sys.stderr)
        sys.exit(2)
    with open(sys.argv[1], encoding="utf-8") as f:
        data = json.load(f)
    if not isinstance(data, list):
        print("File JSON phải là một list các ticket.", file=sys.stderr)
        sys.exit(2)
    results = [evaluate(item) for item in data]
    print(render(results))


if __name__ == "__main__":
    main()
