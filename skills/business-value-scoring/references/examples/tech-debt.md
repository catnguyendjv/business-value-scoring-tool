# Ví dụ — Tech Debt

Các case đã chấm/hiệu chỉnh cho loại ticket này. Mỗi block nằm giữa cặp marker `<!-- ex:tech-debt:<id> -->`. Xem `README.md` để biết cách calibration.

<!-- ex:tech-debt:seed-techdebt -->
### #seed-techdebt — Refactor module notification
<sub>cập nhật 2026-06-19 · nguồn: seed</sub>

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
(1×5 + 2×5 + 4×15 + 4×21 + 5×41 + 2×13) / 5 = 78.0
```

**→ 78.0 — High Priority.** Driver: EN·VH.
<!-- /ex:tech-debt:seed-techdebt -->
