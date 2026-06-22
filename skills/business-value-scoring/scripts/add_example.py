#!/usr/bin/env python3
"""
add_example.py — Ghi (hoặc cập nhật) một ví dụ chấm điểm vào file theo loại ticket.

Dùng cho "calibration": sau khi user feedback về điểm số, Claude gọi script này
để lưu lại case đã hiệu chỉnh vào references/examples/<loại>.md. Upsert theo `id`
— gọi lại với cùng id sẽ GHI ĐÈ block cũ (không nhân bản), nên feedback lần sau
luôn cập nhật đúng ví dụ đó.

Script chỉ làm số học + ghi file. Điểm 0–5 và lý do là phần Claude đã phán đoán.

INPUT: 1 object JSON, truyền qua đường dẫn file HOẶC chuỗi inline:
  {
    "type": "Bug",                       # giá trị Redmine hoặc model type
    "id": "1001",                        # khoá upsert; thiếu thì tự sinh theo thời gian
    "title": "Fix lỗi notification",
    "context": "12% notification fail trong 3 ngày…",
    "scores": {"TM":2,"KH":5,"CL":3,"VH":5,"EN":1,"RR":2},
    "reasons": {"KH":"nhiều complaint","VH":"fail rate rõ"},   # tùy chọn, theo mã
    "source": "feedback",                # feedback | manual | seed
    "correction": "Trước chấm KH=3 → 5 vì support xác nhận diện rộng"  # tùy chọn
  }

Dùng:
  python add_example.py <path.json>
  python add_example.py --json '{"type":"Bug", ...}'
  python add_example.py <path.json> --root /đường/dẫn/references/examples

OUTPUT: in xác nhận + đường dẫn file đã cập nhật, kèm cảnh báo nếu thư mục chỉ-đọc.
"""

import argparse
import datetime
import json
import os
import re
import sys

from bv_model import compute, lane_tier, GROUP_OF, CRIT, SLUG, LANE_FULL, WEIGHTS


def default_root():
    return os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "references", "examples")


def render_block(item):
    mtype, total, drivers, _ = compute(item["type"], item["scores"], item.get("id", "?"))
    slug = SLUG[mtype]
    ex_id = str(item.get("id") or datetime.datetime.now().strftime("%Y%m%d%H%M%S"))
    title = item.get("title", "").strip() or "(không tiêu đề)"
    context = item.get("context", "").strip()
    reasons = item.get("reasons", {}) or {}
    source = item.get("source", "manual")
    correction = item.get("correction", "").strip()
    date = datetime.date.today().isoformat()
    s = item["scores"]
    w = WEIGHTS[mtype]

    rows = "\n".join(
        f"| {GROUP_OF[c]} | {c} | {s[c]} | {reasons.get(c, '').strip()} |"
        for c in CRIT
    )
    calc_terms = " + ".join(f"{s[c]}×{w[c]}" for c in CRIT)
    weight_line = ", ".join(f"{c} {w[c]}" for c in CRIT)
    lane = LANE_FULL[lane_tier(total)]
    corr_line = f"\n**Hiệu chỉnh:** {correction}" if correction else ""

    block = (
        f"<!-- ex:{slug}:{ex_id} -->\n"
        f"### #{ex_id} — {title}\n"
        f"<sub>cập nhật {date} · nguồn: {source}</sub>\n\n"
        f"**Bối cảnh:** {context}\n\n"
        f"| Nhóm | Tiêu chí | Điểm | Lý do |\n|---|---|---:|---|\n{rows}\n\n"
        f"Trọng số {mtype}: {weight_line}.\n\n"
        f"```\n({calc_terms}) / 5 = {total}\n```\n\n"
        f"**→ {total} — {lane}.** Driver: {'·'.join(drivers)}.{corr_line}\n"
        f"<!-- /ex:{slug}:{ex_id} -->"
    )
    return mtype, slug, ex_id, block


def upsert(root, slug, ex_id, block):
    path = os.path.join(root, f"{slug}.md")
    if not os.path.exists(path):
        raise FileNotFoundError(
            f"Không thấy file ví dụ: {path}. Skill có thể đang ở chế độ chỉ-đọc — "
            f"khi đó hãy xuất block dưới đây cho user lưu thủ công rồi đóng gói lại."
        )
    with open(path, encoding="utf-8") as f:
        content = f.read()

    start = f"<!-- ex:{slug}:{ex_id} -->"
    end = f"<!-- /ex:{slug}:{ex_id} -->"
    pattern = re.compile(re.escape(start) + r".*?" + re.escape(end), re.DOTALL)

    if pattern.search(content):
        content = pattern.sub(block, content)
        action = "cập nhật"
    else:
        content = content.rstrip() + "\n\n" + block + "\n"
        action = "thêm mới"

    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    return path, action


def load_item(args):
    if args.json:
        return json.loads(args.json)
    if args.input and os.path.exists(args.input):
        with open(args.input, encoding="utf-8") as f:
            return json.load(f)
    if args.input:  # treat as inline JSON
        return json.loads(args.input)
    raise SystemExit("Cần truyền <path.json> hoặc --json '<...>'.")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("input", nargs="?", help="Đường dẫn file JSON (hoặc chuỗi JSON inline)")
    ap.add_argument("--json", help="Object JSON inline")
    ap.add_argument("--root", help="Thư mục references/examples (mặc định: cạnh script)")
    args = ap.parse_args()

    item = load_item(args)
    root = args.root or default_root()
    mtype, slug, ex_id, block = render_block(item)

    try:
        path, action = upsert(root, slug, ex_id, block)
        print(f"✓ Đã {action} ví dụ #{ex_id} ({mtype}) → {os.path.normpath(path)}")
    except (FileNotFoundError, PermissionError, OSError) as e:
        print(f"⚠ Không ghi được file ({e}).", file=sys.stderr)
        print("Block ví dụ để lưu thủ công:\n", file=sys.stderr)
        print(block)
        sys.exit(1)


if __name__ == "__main__":
    main()
