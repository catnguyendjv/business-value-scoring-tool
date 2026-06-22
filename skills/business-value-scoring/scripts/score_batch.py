#!/usr/bin/env python3
"""
score_batch.py — Tính Business Value Score cho nhiều ticket cùng lúc.

VAI TRÒ: chỉ làm phần số học (áp trọng số theo loại ticket, tính điểm, gán
priority lane, xác định driver, xếp hạng). Việc phân loại ticket và chấm 0–5
cho từng tiêu chí là phần phán đoán do Claude làm TRƯỚC rồi đưa điểm vào đây.
Script này KHÔNG đọc Redmine và KHÔNG tự chấm.

INPUT: đường dẫn tới 1 file JSON, là list các object:
  {
    "id": "12345",
    "title": "Notification không gửi",
    "type": "Bug",                         # giá trị Redmine HOẶC model type
    "scores": {"TM":2,"KH":5,"CL":3,"VH":5,"EN":1,"RR":2},
    "hard_gate": false,                    # hoặc chuỗi lý do nếu dính hard gate
    "note": ""
  }

OUTPUT: in ra stdout bảng Markdown đã xếp hạng + tóm tắt theo lane, để hiển
thị trực tiếp trong khung chat.

Dùng:  python score_batch.py <path-to-scores.json>
"""

import json
import sys

from bv_model import compute, lane_short, SHORT


def evaluate(item):
    mtype, total, drivers, _ = compute(item["type"], item["scores"], item.get("id", "?"))
    hg = item.get("hard_gate")
    hg_active = bool(hg) and hg not in (False, "", "false", "False")
    return {
        "id": str(item.get("id", "")),
        "title": item.get("title", ""),
        "type": mtype,
        "scores": item["scores"],
        "total": total,
        "lane": "Expedite⚡" if hg_active else lane_short(total),
        "hard_gate": hg if hg_active else None,
        "drivers": drivers,
        "note": item.get("note", ""),
    }


def trunc(text, n):
    text = (str(text) or "").replace("|", "/").replace("\n", " ").strip()
    return text if len(text) <= n else text[: n - 1] + "…"


def render(results):
    results.sort(key=lambda r: (r["hard_gate"] is None, -r["total"]))

    order = ["Expedite⚡", "Expedite", "High", "Medium", "Backlog"]
    counts = {}
    for r in results:
        counts[r["lane"]] = counts.get(r["lane"], 0) + 1
    summary = " · ".join(f"{k} {counts[k]}" for k in order if counts.get(k))

    lines = [f"**{len(results)} ticket** — {summary}", ""]
    lines.append("| # | Ticket | Loại | TM | KH | CL | VH | EN | RR | Điểm | Lane | Driver | Ghi chú |")
    lines.append("|---|---|---|--:|--:|--:|--:|--:|--:|--:|---|---|---|")
    for r in results:
        s = r["scores"]
        flag = []
        if r["hard_gate"]:
            flag.append(f"hard gate: {trunc(r['hard_gate'], 40)}")
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
    print(render([evaluate(i) for i in data]))


if __name__ == "__main__":
    main()
