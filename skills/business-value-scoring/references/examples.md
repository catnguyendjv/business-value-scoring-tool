# Ví dụ chấm điểm

Ba ví dụ minh họa cách áp anchor, trọng số theo loại ticket và ra priority lane. Dùng để đối chiếu khi không chắc nên cho điểm nào.

## Ví dụ 1 — Bug Fix: notification không gửi

**Bối cảnh:** 12% notification fail trong 3 ngày gần đây, ảnh hưởng trực tiếp workflow user, support nhận nhiều complaint, có log lỗi rõ, nguyên nhân đã xác định.

| Nhóm | Tiêu chí | Điểm | Lý do |
|---|---|---:|---|
| DM | TM | 2 | Không trực tiếp tạo revenue, nhưng ảnh hưởng trust |
| DM | KH | 5 | User-facing, nhiều complaint |
| DM | CL | 3 | Ảnh hưởng flow quan trọng |
| PM | VH | 5 | Fail rate rõ, ảnh hưởng vận hành |
| PM | EN | 1 | Không mở đường nhiều cho tương lai |
| PM | RR | 2 | Có thể ảnh hưởng cam kết service nhưng chưa nghiêm trọng |

Trọng số Bug Fix: TM 11, KH 24, CL 11, VH 35, EN 5, RR 14.

```
(2×11 + 5×24 + 3×11 + 5×35 + 1×5 + 2×14) / 5
= (22 + 120 + 33 + 175 + 5 + 28) / 5
= 383 / 5 = 76.6
```

**→ 76.6 — High Priority.** Driver chính: VH và KH.

## Ví dụ 2 — Tech Debt: refactor module notification

**Bối cảnh:** Code khó maintain, thêm notification mới tốn thời gian, đã gây 3 bug production trong 2 tháng, mở đường cho nhiều feature notification sau này.

| Nhóm | Tiêu chí | Điểm | Lý do |
|---|---|---:|---|
| DM | TM | 1 | Không tạo revenue trực tiếp |
| DM | KH | 2 | Gián tiếp giảm bug cho user |
| DM | CL | 4 | Liên quan roadmap notification sắp tới |
| PM | VH | 4 | Giảm bug production, giảm support/on-call |
| PM | EN | 5 | Mở đường cho nhiều feature sau |
| PM | RR | 2 | Có risk lỗi nhưng không phải compliance/security |

Trọng số Tech Debt: TM 5, KH 5, CL 15, VH 21, EN 41, RR 13.

```
(1×5 + 2×5 + 4×15 + 4×21 + 5×41 + 2×13) / 5
= (5 + 10 + 60 + 84 + 205 + 26) / 5
= 390 / 5 = 78.0
```

**→ 78.0 — High Priority.** Driver chính: EN (enablement), kế đến VH.

## Ví dụ 3 — Security: rotate secret bị lộ

**Bối cảnh:** Secret nằm trong repo private, chưa thấy dấu hiệu bị khai thác, secret có quyền truy cập staging và một phần production config, fix tương đối rõ.

| Nhóm | Tiêu chí | Điểm | Lý do |
|---|---|---:|---|
| DM | TM | 1 | Không tạo revenue trực tiếp |
| DM | KH | 3 | Nếu bị khai thác sẽ ảnh hưởng trust |
| DM | CL | 4 | Security hygiene quan trọng |
| PM | VH | 3 | Có thể ảnh hưởng vận hành nếu bị abuse |
| PM | EN | 2 | Có thể cải thiện process secret management |
| PM | RR | 5 | Credential exposure là risk cao |

Trọng số Security: TM 2, KH 10, CL 13, VH 18, EN 8, RR 50.

```
(1×2 + 3×10 + 4×13 + 3×18 + 2×8 + 5×50) / 5
= (2 + 30 + 52 + 54 + 16 + 250) / 5
= 404 / 5 = 80.8
```

**→ 80.8 — Expedite.** Driver chính: RR. Lưu ý: nếu có bằng chứng đang bị khai thác → rơi vào hard gate, expedite ngay không cần chờ scoring.
