# Ví dụ — Bug Fix

Các case đã chấm/hiệu chỉnh cho loại ticket này. Mỗi block nằm giữa cặp marker `<!-- ex:bug-fix:<id> -->`. Xem `README.md` để biết cách calibration.

<!-- ex:bug-fix:seed-bug -->
### #seed-bug — Fix lỗi notification không gửi
<sub>cập nhật 2026-06-19 · nguồn: seed</sub>

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
(2×11 + 5×24 + 3×11 + 5×35 + 1×5 + 2×14) / 5 = 76.6
```

**→ 76.6 — High Priority.** Driver: VH·KH.
<!-- /ex:bug-fix:seed-bug -->
