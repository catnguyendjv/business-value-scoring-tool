#!/usr/bin/env python3
"""
bv_model.py — Lõi dùng chung cho Business Value Scoring.

Chứa trọng số, mapping loại ticket Redmine, và các hàm tính toán (số học
thuần). Cả score_batch.py và add_example.py import từ đây để đảm bảo MỌI
nơi tính điểm theo cùng một logic.
"""

# Trọng số theo loại ticket (mỗi hàng cộng = 100).
WEIGHTS = {
    "New Feature":            {"TM": 28, "KH": 23, "CL": 26, "VH": 5,  "EN": 10, "RR": 8},
    "Enhancement / Maintain": {"TM": 18, "KH": 28, "CL": 18, "VH": 13, "EN": 15, "RR": 8},
    "Bug Fix":                {"TM": 11, "KH": 24, "CL": 11, "VH": 35, "EN": 5,  "RR": 14},
    "Tech Debt":              {"TM": 5,  "KH": 5,  "CL": 15, "VH": 21, "EN": 41, "RR": 13},
    "Ops / Infra":            {"TM": 5,  "KH": 8,  "CL": 13, "VH": 43, "EN": 18, "RR": 13},
    "Security":               {"TM": 2,  "KH": 10, "CL": 13, "VH": 18, "EN": 8,  "RR": 50},
    "Research / Spike":       {"TM": 6,  "KH": 6,  "CL": 29, "VH": 12, "EN": 29, "RR": 18},
}

# Custom field "ticket type" của Redmine → loại của mô hình.
# Lưu ý: Redmine không có Security; issue liên quan security xử lý như Improvement.
REDMINE_MAP = {
    "Feature":        "New Feature",
    "Bug":            "Bug Fix",
    "Improvement":    "Enhancement / Maintain",
    "Refactor":       "Tech Debt",
    "Infrastructure": "Ops / Infra",
    "Spike":          "Research / Spike",
}

CRIT = ["TM", "KH", "CL", "VH", "EN", "RR"]
GROUP_OF = {"TM": "DM", "KH": "DM", "CL": "DM", "VH": "PM", "EN": "PM", "RR": "PM"}

# Tên gọn cho cột bảng batch.
SHORT = {
    "New Feature": "Feature", "Enhancement / Maintain": "Improve", "Bug Fix": "Bug",
    "Tech Debt": "Refactor", "Ops / Infra": "Infra", "Security": "Security",
    "Research / Spike": "Spike",
}

# Tên file (slug) cho từng loại trong references/examples/.
SLUG = {
    "New Feature": "new-feature",
    "Enhancement / Maintain": "enhancement-maintain",
    "Bug Fix": "bug-fix",
    "Tech Debt": "tech-debt",
    "Ops / Infra": "ops-infra",
    "Security": "security",
    "Research / Spike": "research-spike",
}

# Tên lane đầy đủ (tiếng Việt) theo bậc 0..3.
LANE_FULL = ["Backlog / Batch", "Medium Priority", "High Priority", "Expedite / sprint gần nhất"]


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


def lane_tier(score):
    if score >= 80:
        return 3
    if score >= 65:
        return 2
    if score >= 50:
        return 1
    return 0


def lane_short(score):
    return ["Backlog", "Medium", "High", "Expedite"][lane_tier(score)]


def validate_scores(scores, ticket_id="?"):
    for c in CRIT:
        v = scores.get(c)
        if not isinstance(v, int) or not (0 <= v <= 5):
            raise ValueError(f"Điểm {c} của ticket {ticket_id} phải là số nguyên 0–5, nhận {v!r}.")


def compute(ticket_type, scores, ticket_id="?"):
    """Trả về (model_type, total, drivers, contributions)."""
    mtype = resolve_type(ticket_type)
    validate_scores(scores, ticket_id)
    w = WEIGHTS[mtype]
    contrib = {c: scores[c] * w[c] / 5 for c in CRIT}   # 0..weight
    total = round(sum(contrib.values()), 1)
    drivers = sorted(CRIT, key=lambda c: contrib[c], reverse=True)[:2]
    return mtype, total, drivers, contrib
