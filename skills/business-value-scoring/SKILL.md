---
name: business-value-scoring
description: Chấm điểm Business Value (0–100) và xác định priority lane cho một ticket/issue trong backlog sản phẩm IT, dùng mô hình 6 tiêu chí chia theo DM (Thương mại, Khách hàng, Chiến lược) và PM (Vận hành, Enablement, Risk). Dùng skill này bất cứ khi nào user muốn đánh giá business value, chấm điểm hoặc xếp ưu tiên cho một ticket/issue/backlog item — kể cả khi họ chỉ hỏi "ticket này nên ưu tiên không", "scoring cái này giúp tôi", "đánh giá giá trị của task này", "nên đưa vào sprint không", hoặc dán mô tả một Redmine/Jira issue và hỏi mức độ quan trọng. Ưu tiên skill này thay vì tự ước lượng cảm tính khi có yếu tố priority/backlog/business value.
---

# Business Value Scoring cho ticket

## Mục đích

Chuẩn hóa việc đánh giá **business value** của một ticket để hỗ trợ backlog prioritization, thay cho cảm tính. Mỗi ticket được chấm theo **6 tiêu chí**, ra **điểm 0–100** và một **priority lane**. Điểm số là *input cho thảo luận planning*, không phải quyết định tuyệt đối — luôn kèm lý do và giả định để người đọc tự cân nhắc.

Hai nhóm người chấm (giúp mỗi tiêu chí được đánh giá đúng góc nhìn):
- **DM** (Decision Maker / business): **TM** Thương mại, **KH** Khách hàng, **CL** Chiến lược.
- **PM** (Product Manager): **VH** Vận hành, **EN** Enablement tương lai, **RR** Risk.

Khi chạy skill này một mình, hãy chấm cả 6 tiêu chí dựa trên thông tin có được, nhưng **gắn nhãn nhóm (DM/PM) cho từng tiêu chí** để người dùng biết phần nào nên do business xác nhận và phần nào do product/tech xác nhận.

## Quy trình

1. **Thu thập thông tin ticket.** Cần: tiêu đề, loại ticket, người/đối tượng bị ảnh hưởng, vấn đề & hệ quả nếu không làm, evidence (số liệu/log/feedback), deadline/dependency. Nếu user chỉ đưa mô tả ngắn, suy luận hợp lý từ những gì có, đừng bịa số liệu.
2. **Phân loại ticket** vào một trong 7 loại (xác định bộ trọng số): New Feature, Enhancement / Maintain, Bug Fix, Tech Debt, Ops / Infra, Security, Research / Spike. Nếu mơ hồ, chọn loại sát nhất và nêu rõ giả định.
3. **Kiểm tra hard gate** (mục bên dưới). Nếu dính, đề xuất **Expedite ngay**, vẫn chấm điểm để ghi nhận nhưng nói rõ hard gate ưu tiên trước scoring.
4. **Chấm 6 tiêu chí 0–5** theo anchor bên dưới. Mỗi điểm phải có một câu lý do bám vào evidence.
5. **Tính điểm** theo công thức, dùng đúng cột trọng số của loại ticket.
6. **Xác định priority lane** từ điểm.
7. **Xuất kết quả** theo template ở mục "Output".

## 6 tiêu chí & anchor 0–5

Chấm mức gần đúng nhất; nếu lưỡng lự giữa hai mức và evidence yếu, chọn mức thấp hơn (tránh thổi phồng).

**TM — Thương mại** *(DM)* · doanh thu, chi phí, hợp đồng, deal, renewal, cost saving.
- 0 không tác động · 1 rất gián tiếp · 2 hỗ trợ business nhưng chưa có deal cụ thể · 3 đáng kể (retention/giảm chi phí) · 4 trực tiếp deal/renewal/cost saving rõ · 5 rất lớn (deal lớn, bảo vệ KH chiến lược, ngăn mất doanh thu nghiêm trọng).

**KH — Khách hàng** *(DM)* · phạm vi user bị ảnh hưởng, mức đau, tần suất, cải thiện trải nghiệm.
- 0 user không cảm nhận · 1 rất nhỏ/nhóm rất nhỏ · 2 cải thiện nhẹ 1 nhóm · 3 cải thiện rõ flow tần suất vừa · 4 lớn, nhiều user/KH quan trọng · 5 rất lớn, critical journey hoặc phần lớn user.

**CL — Chiến lược / Urgency / Cost of Delay** *(DM)* · gắn OKR, roadmap, deadline, cam kết, cost of delay.
- 0 không gắn gì · 1 liên quan nhẹ roadmap dài hạn · 2 hỗ trợ mục tiêu nhưng không khẩn · 3 mục tiêu quý hoặc unblock một phần · 4 quan trọng roadmap/OKR hiện tại, delay thiệt hại rõ · 5 critical path/deadline cứng/mất cơ hội lớn.

**VH — Vận hành / Reliability** *(PM)* · stability, latency, error, SLO/SLA, incident, support load, toil.
- 0 không ảnh hưởng · 1 cải thiện nhỏ không metric · 2 giảm pain cục bộ · 3 cải thiện rõ service quan trọng · 4 giảm đáng kể incident/latency/support/toil · 5 đang/sắp breach SLO/SLA, SEV cao, ảnh hưởng core flow.

**EN — Enablement tương lai** *(PM)* · nền tảng cho feature/team/architecture/automation/delivery speed sau này.
- 0 không mở đường · 1 cải thiện nhỏ 1 module · 2 lợi cho vài thay đổi sau · 3 unblock vài ticket/giảm effort 1 area · 4 mở đường initiative lớn/nhiều team · 5 nền tảng quan trọng cho roadmap/architecture dài hạn.

**RR — Risk / Compliance / Security** *(PM)* · pháp lý, compliance, security, privacy, audit, contractual, reputational.
- 0 không liên quan · 1 hygiene nhỏ rủi ro thấp · 2 có rủi ro nhưng impact/likelihood thấp · 3 rủi ro thực tế cần xử lý gần · 4 rủi ro cao (security/compliance/trust rõ) · 5 critical (active exploit, credential leak, regulated data exposure, deadline pháp lý cứng).

## Ma trận trọng số (theo loại ticket)

Mỗi hàng cộng đủ 100. Cột nhóm theo người chấm: DM = TM·KH·CL, PM = VH·EN·RR.

| Loại ticket | TM | KH | CL | VH | EN | RR |
|---|---:|---:|---:|---:|---:|---:|
| New Feature            | 28 | 23 | 26 | 5  | 10 | 8  |
| Enhancement / Maintain | 18 | 28 | 18 | 13 | 15 | 8  |
| Bug Fix                | 11 | 24 | 11 | 35 | 5  | 14 |
| Tech Debt              | 5  | 5  | 15 | 21 | 41 | 13 |
| Ops / Infra            | 5  | 8  | 13 | 43 | 18 | 13 |
| Security               | 2  | 10 | 13 | 18 | 8  | 50 |
| Research / Spike       | 6  | 6  | 29 | 12 | 29 | 18 |

## Công thức & priority lane

```
Business Value Score = Σ(score × weight) / 5
```
Vì tổng trọng số = 100 và mỗi tiêu chí 0–5, điểm nằm trong **0–100**. Làm tròn 1 chữ số thập phân. **Luôn hiển thị phép tính** `(s_TM×w_TM + ... + s_RR×w_RR) / 5 = …` để người dùng kiểm chứng.

| Điểm | Priority lane |
|---:|---|
| 80–100 | **Expedite** / sprint gần nhất |
| 65–79  | **High Priority** |
| 50–64  | **Medium Priority** |
| < 50   | **Backlog / Batch** |

## Hard gate — không chờ scoring

Nếu ticket rơi vào bất kỳ trường hợp nào sau đây, đề xuất **Expedite** bất kể điểm số:
- SEV1 / incident nghiêm trọng đang diễn ra.
- Security đang bị khai thác hoặc credential leak nghiêm trọng.
- Deadline pháp lý / compliance cứng.
- SLA/SLO đang breach hoặc error budget burn rất cao.
- Cam kết hợp đồng với khách hàng chiến lược có deadline cụ thể.

## Output

Trình bày kết quả theo đúng cấu trúc này:

```
Ticket: <tiêu đề>
Loại: <loại ticket>   |   Hard gate: <Không | Có — lý do>

Scoring (DM)
- TM <0–5> — <lý do bám evidence>
- KH <0–5> — <lý do>
- CL <0–5> — <lý do>
Scoring (PM)
- VH <0–5> — <lý do>
- EN <0–5> — <lý do>
- RR <0–5> — <lý do>

Tính điểm: (s×w + …) / 5 = <điểm>
→ Business Value Score: <điểm>/100
→ Priority lane: <lane>

Khuyến nghị: <1–2 câu hành động>
Thiếu thông tin: <những gì cần xác nhận để tăng độ tin cậy, hoặc "không">
Giả định: <giả định đã dùng khi chấm, hoặc "không">
```

Sau bảng kết quả, nếu hữu ích, nêu ngắn gọn tiêu chí nào đang kéo điểm (driver chính) để người đọc hiểu vì sao ra lane đó.

## Nguyên tắc khi chấm

- **Evidence trước, điểm sau.** Mỗi điểm số gắn với dữ liệu/lý do; nếu chỉ là phỏng đoán, nói rõ trong "Giả định" và đừng cho điểm cao.
- **Đừng thổi phồng.** Ticket thiếu dữ liệu → chấm thận trọng và liệt kê "Thiếu thông tin"; nếu quá mơ hồ, đề xuất tạo Research/Spike để làm rõ trước.
- **Loại ticket quyết định trọng số**, không phải cảm giác về độ "ngầu" của ticket. Một bug fix vẫn có thể vượt một feature nếu VH/KH cao.
- **Hard gate thắng scoring.** Nêu rõ khi áp dụng.
- Chấm nhiều ticket một lúc: lập bảng so sánh (Ticket · Loại · Điểm · Lane · Driver) để dễ xếp thứ tự.

## Chế độ batch — chấm nhiều ticket (vd. ~100 issue từ Redmine)

Khi cần chấm nhiều ticket một lúc, **phần phán đoán vẫn do Claude làm** (đọc issue, xác nhận loại, gán 0–5 cho 6 tiêu chí kèm lý do). Phần *số học* (áp trọng số, tính điểm, gán lane, xếp hạng) giao cho script để đảm bảo nhất quán tuyệt đối trên nhiều dòng — không tính tay trong văn bản với số lượng lớn.

**Quy trình:**

1. **Lấy issue** qua `drjoy-management:redmine` (subject, description, comment, và custom field *ticket type*).
2. **Map loại ticket** từ custom field Redmine sang model type (script tự map, nhưng cần hiểu để xác nhận):

   | Redmine | Model type |
   |---|---|
   | Feature | New Feature |
   | Bug | Bug Fix |
   | Improvement | Enhancement / Maintain |
   | Refactor | Tech Debt |
   | Infrastructure | Ops / Infra |
   | Spike (gồm cả ticket điều tra) | Research / Spike |

   Redmine **không có loại Security**, và ở đây ta **không** tạo override riêng. Issue liên quan security xử lý như **Improvement** (→ Enhancement / Maintain) theo custom field. Đổi lại, trọng số RR chỉ 8 nên điểm RR cao không kéo nhiều — điều này chấp nhận được cho security hygiene thường. Các trường hợp security thực sự khẩn (active exploit, credential leak, compliance/audit deadline cứng) vẫn được bắt qua `hard_gate` → `Expedite⚡`, không phụ thuộc trọng số, nên không bị bỏ sót.
3. **Chấm 0–5** cho từng issue theo anchor. Nếu số lượng lớn, chia mẻ ~15–20 issue để giữ chất lượng phán đoán, nối dần vào một list. Issue thiếu evidence → chấm thận trọng và ghi vào `note`.
4. **Ghi ra JSON** (list các object), mỗi ticket:
   ```json
   {
     "id": "12345",
     "title": "…",
     "type": "Bug",
     "scores": {"TM":2,"KH":5,"CL":3,"VH":5,"EN":1,"RR":2},
     "hard_gate": false,
     "note": ""
   }
   ```
   `type` nhận cả giá trị Redmine lẫn model type. `hard_gate`: để chuỗi lý do nếu dính (SEV1, exploit…), khi đó ticket được đẩy lên đầu và gán `Expedite⚡`.
5. **Chạy script** để tính và xếp hạng:
   ```bash
   python scripts/score_batch.py <path-to-scores.json>
   ```
6. **Hiển thị bảng** mà script in ra (Markdown) trực tiếp trong khung chat. Bảng đã sắp xếp: hard gate trước, rồi điểm giảm dần; kèm tóm tắt số lượng theo lane và cột Driver/Ghi chú.

Kết quả batch nên hiểu là **bản triage để xếp thứ tự sơ bộ**, không phải điểm cuối — vì nhiều issue Redmine thiếu metric cho nhóm DM (TM/KH/CL), phần đó sẽ có giả định. Khuyến nghị DM/PM soi kỹ nhóm điểm cao và nhóm sát ngưỡng lane; cột `note` giúp lọc các ticket thiếu dữ liệu.

## Tích hợp (tùy chọn)

Nếu ticket là một issue Redmine/DrJoy và user muốn lấy thông tin trực tiếp hoặc ghi kết quả lại, dùng skill/MCP tương ứng (`drjoy-management:redmine` v.v.). Skill này chỉ phụ trách *logic chấm điểm*; mọi thao tác ghi (comment, custom field) phải được user xác nhận trước.

## Ví dụ

Xem `references/examples.md` để có 3 ví dụ đã tính sẵn (Bug Fix, Tech Debt, Security) minh họa cách chấm điểm, áp trọng số và ra lane. Đọc file này khi cần đối chiếu cách chấm trong tình huống thực tế hoặc khi không chắc về mức anchor.

Script `scripts/score_batch.py` dùng cho chế độ batch (mục trên) — nhận JSON điểm đã chấm và in bảng xếp hạng. Script chỉ làm số học, không tự chấm.
