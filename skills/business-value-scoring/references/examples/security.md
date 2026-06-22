# Ví dụ — Security

Các case đã chấm/hiệu chỉnh cho loại ticket này. Mỗi block nằm giữa cặp marker `<!-- ex:security:<id> -->`. Xem `README.md` để biết cách calibration.

<!-- ex:security:seed-security -->
### #seed-security — Rotate secret bị lộ
<sub>cập nhật 2026-06-19 · nguồn: seed</sub>

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
(1×2 + 3×10 + 4×13 + 3×18 + 2×8 + 5×50) / 5 = 80.8
```

**→ 80.8 — Expedite / sprint gần nhất.** Driver: RR·VH.
<!-- /ex:security:seed-security -->
