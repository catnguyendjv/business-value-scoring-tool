# Ví dụ chấm điểm (theo loại ticket)

Mỗi loại ticket có một file riêng để bộ ví dụ phình to dần mà vẫn dễ tham chiếu:

| File | Loại ticket |
|---|---|
| `new-feature.md` | New Feature |
| `enhancement-maintain.md` | Enhancement / Maintain (Redmine: Improvement) |
| `bug-fix.md` | Bug Fix (Redmine: Bug) |
| `tech-debt.md` | Tech Debt (Redmine: Refactor) |
| `ops-infra.md` | Ops / Infra (Redmine: Infrastructure) |
| `security.md` | Security |
| `research-spike.md` | Research / Spike (Redmine: Spike) |

## Cách dùng khi chấm

Khi không chắc nên cho điểm nào cho một tiêu chí, mở file của **đúng loại ticket**
đang chấm và đối chiếu với các ví dụ đã hiệu chỉnh trong đó. Chỉ cần đọc file của
loại liên quan, không cần đọc hết.

## Định dạng & calibration

Mỗi ví dụ là một block giữa cặp marker:

```
<!-- ex:<slug>:<id> -->
…nội dung ví dụ…
<!-- /ex:<slug>:<id> -->
```

`id` thường là mã issue Redmine. Khi user feedback chỉnh điểm, dùng
`scripts/add_example.py` với **cùng id** để ghi đè block cũ (không nhân bản) —
nhờ vậy ví dụ luôn phản ánh lần hiệu chỉnh mới nhất. Trường `correction` ghi lại
lý do thay đổi để sau này truy vết được vì sao calibrate.
