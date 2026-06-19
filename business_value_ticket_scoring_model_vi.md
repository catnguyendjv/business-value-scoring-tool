# Khung tiêu chuẩn đánh giá Business Value cho ticket (Scoring Model)

## 1. Mục tiêu

Tài liệu này định nghĩa một **khung chuẩn (scoring model)** để đánh giá **Business Value cho từng ticket** trong backlog sản phẩm IT, bao gồm phát triển chức năng mới, cải tiến/maintain, fix bug, tech debt, ops/infra, security và research/spike.

Mục tiêu là giúp team và stakeholder đánh giá mức độ ưu tiên của ticket dựa trên **giá trị kinh doanh, tác động đến khách hàng, mức độ chiến lược, độ ổn định vận hành, khả năng mở đường cho tương lai và rủi ro**, thay vì chỉ dựa vào cảm tính hoặc loại ticket.

---

## 2. Hai nhóm người đánh giá

Khung này chia 6 tiêu chí thành 2 nhóm, mỗi nhóm do một vai trò phụ trách:

| Vai trò | Phụ trách đánh giá | Góc nhìn chính |
|---|---|---|
| **DM** (Decision Maker / phía business) | **TM** (Thương mại), **KH** (Khách hàng), **CL** (Chiến lược) | Giá trị kinh doanh, khách hàng, mục tiêu/định hướng |
| **PM** (Product Manager) | **VH** (Vận hành), **EN** (Enablement tương lai), **RR** (Risk) | Vận hành hệ thống, nền tảng tương lai, rủi ro |

Việc tách vai trò giúp mỗi tiêu chí được chấm bởi người có đủ ngữ cảnh và dữ liệu, đồng thời giảm thiên kiến khi một người chấm toàn bộ.

---

## 3. Nguyên tắc đánh giá

Business Value của một ticket không chỉ đến từ doanh thu trực tiếp. Một ticket có thể tạo value bằng nhiều cách:

- Tạo hoặc bảo vệ doanh thu (TM).
- Tăng trải nghiệm và hiệu quả cho người dùng (KH).
- Hỗ trợ OKR, roadmap, deadline hoặc cam kết khách hàng (CL).
- Tăng reliability, giảm incident, giảm support load (VH).
- Mở đường cho các feature hoặc kiến trúc tương lai (EN).
- Giảm rủi ro security, compliance, privacy hoặc audit (RR).

Do đó, mỗi ticket được đánh giá bằng **6 nhóm tiêu chí chính**.

---

## 4. Tổng quan 6 nhóm tiêu chí

| Người chấm | Mã | Nhóm tiêu chí | Ý nghĩa |
|---|---|---|---|
| **DM** | **TM** | Thương mại / Business & Revenue Impact | Ticket có tạo, bảo vệ hoặc hỗ trợ doanh thu không |
| **DM** | **KH** | Khách hàng / User Impact | Ticket ảnh hưởng bao nhiêu user/khách hàng và cải thiện trải nghiệm thế nào |
| **DM** | **CL** | Chiến lược / Urgency / Cost of Delay | Ticket có gắn với OKR, roadmap, deadline hoặc cơ hội thị trường không |
| **PM** | **VH** | Vận hành / Reliability | Ticket có cải thiện stability, SLA/SLO, incident, support load hoặc toil không |
| **PM** | **EN** | Enablement tương lai | Ticket có mở đường cho feature, team, architecture hoặc delivery speed sau này không |
| **PM** | **RR** | Risk / Compliance / Security | Ticket có giảm rủi ro pháp lý, bảo mật, privacy hoặc audit không |

---

## 5. Định nghĩa chi tiết từng nhóm tiêu chí

### 5.1. TM — Thương mại / Business & Revenue Impact *(DM)*

**Định nghĩa:** Đo mức độ ticket có tác động đến doanh thu, chi phí, hợp đồng, cơ hội bán hàng, renewal, upsell hoặc khả năng go-to-market.

**Câu hỏi đánh giá:**

- Ticket này có liên quan trực tiếp đến revenue không?
- Có khách hàng hoặc deal cụ thể đang chờ không?
- Nếu không làm, có nguy cơ mất khách hàng, mất renewal hoặc mất cơ hội sales không?
- Có giúp giảm chi phí cloud, support, vận hành hoặc thao tác thủ công không?
- Tác động là trực tiếp hay gián tiếp?

**Dữ liệu nên dùng:** Deal pipeline, ARR/MRR, renewal value, lost reason, cost saving estimate, product analytics liên quan conversion/activation/billing/checkout.

**Thang điểm:**

| Điểm | Ý nghĩa |
|---:|---|
| 0 | Không có tác động thương mại rõ ràng |
| 1 | Tác động rất gián tiếp, khó định lượng |
| 2 | Có thể hỗ trợ business nhưng chưa có khách hàng/deal cụ thể |
| 3 | Có tác động thương mại đáng kể, ví dụ hỗ trợ retention hoặc giảm chi phí |
| 4 | Ảnh hưởng trực tiếp đến deal, renewal, paid customer hoặc cost saving rõ |
| 5 | Tác động rất lớn: chốt deal lớn, bảo vệ khách hàng chiến lược hoặc ngăn mất doanh thu nghiêm trọng |

### 5.2. KH — Khách hàng / User Impact *(DM)*

**Định nghĩa:** Đo mức độ ticket ảnh hưởng đến người dùng hoặc khách hàng: phạm vi ảnh hưởng, mức độ đau, tần suất sử dụng và mức cải thiện trải nghiệm.

**Câu hỏi đánh giá:**

- Bao nhiêu user/customer bị ảnh hưởng?
- Đây có phải flow quan trọng không?
- User có đang complain không?
- Có support ticket hoặc feedback lặp lại không?
- Ticket này giúp user nhanh hơn, ít lỗi hơn, ít khó chịu hơn không?
- Tác động là daily, weekly, monthly hay chỉ one-off?

**Dữ liệu nên dùng:** DAU/WAU/MAU, số lượt dùng feature, support ticket, complaint, VOC, user interview, usability test, task completion rate, drop-off, time-on-task, customer segment.

**Thang điểm:**

| Điểm | Ý nghĩa |
|---:|---|
| 0 | User hầu như không cảm nhận được |
| 1 | Ảnh hưởng rất nhỏ hoặc nhóm user rất nhỏ |
| 2 | Cải thiện nhẹ cho một nhóm user cụ thể |
| 3 | Cải thiện rõ cho flow có tần suất sử dụng vừa |
| 4 | Ảnh hưởng lớn đến nhiều user hoặc nhóm khách hàng quan trọng |
| 5 | Ảnh hưởng rất lớn đến critical journey hoặc phần lớn user/customer |

### 5.3. CL — Chiến lược / Urgency / Cost of Delay *(DM)*

**Định nghĩa:** Đo mức độ ticket gắn với OKR, roadmap, deadline, market window, cam kết khách hàng hoặc cost of delay.

**Câu hỏi đánh giá:**

- Ticket này có link trực tiếp đến OKR/roadmap không?
- Có deadline cụ thể không?
- Nếu delay 1 sprint hoặc 1 tháng thì mất gì?
- Có ticket hoặc team nào đang bị block không?
- Đây là nice-to-have hay critical path?
- Có cost of delay rõ không?

**Dữ liệu nên dùng:** OKR, product roadmap, release milestone, contract, customer commitment, dependency map, launch/campaign deadline.

**Thang điểm:**

| Điểm | Ý nghĩa |
|---:|---|
| 0 | Không gắn với chiến lược/deadline nào |
| 1 | Có liên quan nhẹ đến roadmap dài hạn |
| 2 | Hỗ trợ mục tiêu nhưng không khẩn cấp |
| 3 | Gắn với mục tiêu quý hoặc unblock một phần kế hoạch |
| 4 | Quan trọng cho roadmap/OKR hiện tại, delay gây thiệt hại rõ |
| 5 | Critical path, deadline cứng hoặc delay làm mất cơ hội/cam kết lớn |

### 5.4. VH — Vận hành / Reliability *(PM)*

**Định nghĩa:** Đo mức độ ticket cải thiện độ ổn định, availability, latency, error rate, SLO/SLA, observability, incident response, support load hoặc toil.

**Câu hỏi đánh giá:**

- Ticket này có liên quan đến incident, SLO hoặc SLA không?
- Có metric latency/error/availability xấu không?
- Có complaint do performance hoặc downtime không?
- Có giảm support/on-call/toil không?
- Có giúp detect, debug hoặc recover nhanh hơn không?
- Nếu không làm, khả năng incident tăng không?

**Dữ liệu nên dùng:** p95/p99 latency, error rate, availability, SLO/SLA breach, error budget burn, incident report, postmortem, MTTR, support escalation, alert volume.

**Thang điểm:**

| Điểm | Ý nghĩa |
|---:|---|
| 0 | Không ảnh hưởng vận hành/reliability |
| 1 | Cải thiện nhỏ, không có metric rõ |
| 2 | Giảm một số pain vận hành cục bộ |
| 3 | Cải thiện rõ cho service/flow quan trọng |
| 4 | Giảm đáng kể incident, latency, support load hoặc toil |
| 5 | Đang/sắp breach SLO/SLA, SEV cao hoặc ảnh hưởng nghiêm trọng đến availability/core flow |

### 5.5. EN — Enablement tương lai *(PM)*

**Định nghĩa:** Đo mức độ ticket tạo nền tảng cho các feature, team, architecture, automation, platform capability hoặc delivery speed trong tương lai.

**Câu hỏi đánh giá:**

- Ticket này mở đường cho những ticket/feature nào?
- Có bao nhiêu team/ticket phụ thuộc vào nó?
- Sau khi làm, delivery sau này nhanh hơn bao nhiêu?
- Có giảm coupling hoặc giảm risk khi thay đổi không?
- Có tạo reusable capability không?
- Nếu không làm, roadmap sau này có bị chậm không?

**Dữ liệu nên dùng:** Roadmap dependency, ADR, list ticket bị block, lead time/cycle time, repeated workaround, code complexity/testability, engineering feedback.

**Thang điểm:**

| Điểm | Ý nghĩa |
|---:|---|
| 0 | Không mở đường gì cho tương lai |
| 1 | Cải thiện nhỏ trong một module |
| 2 | Có lợi cho một số thay đổi sau |
| 3 | Unblock vài ticket hoặc giảm effort đáng kể cho một area |
| 4 | Mở đường cho initiative lớn hoặc nhiều team |
| 5 | Nền tảng quan trọng cho roadmap/architecture dài hạn, nếu không làm sẽ chặn nhiều việc |

### 5.6. RR — Risk / Compliance / Security *(PM)*

**Định nghĩa:** Đo mức độ ticket giúp giảm rủi ro pháp lý, compliance, security, privacy, audit, contractual risk hoặc reputational risk.

**Câu hỏi đánh giá:**

- Có liên quan đến security, privacy hoặc compliance không?
- Có dữ liệu nhạy cảm không?
- Có deadline audit/pháp lý không?
- Có CVE, exploit, secret leak hoặc access control issue không?
- Asset bị ảnh hưởng có critical không?
- Nếu xảy ra sự cố, impact đến khách hàng/công ty là gì?

**Dữ liệu nên dùng:** Security finding, CVE/CVSS/EPSS, exploit status, audit finding, data classification, privacy impact assessment, contractual security requirement.

**Thang điểm:**

| Điểm | Ý nghĩa |
|---:|---|
| 0 | Không liên quan risk/compliance/security |
| 1 | Hygiene nhỏ, rủi ro thấp |
| 2 | Có rủi ro nhưng impact hoặc likelihood thấp |
| 3 | Rủi ro thực tế, cần xử lý trong kế hoạch gần |
| 4 | Rủi ro cao: security/compliance/customer trust bị ảnh hưởng rõ |
| 5 | Critical: active exploit, credential leak, regulated data exposure hoặc audit/legal deadline cứng |

---

## 6. Công thức tính điểm

Mỗi tiêu chí được chấm từ **0 đến 5**. Mỗi loại ticket có bộ trọng số khác nhau.

```text
Business Value Score = Σ(score × weight) / 5
```

Vì tổng trọng số của mỗi loại ticket là 100, kết quả cuối cùng nằm trong thang **0–100**.

---

## 7. Ma trận trọng số theo loại ticket

Cột được nhóm theo người chấm: **DM** (TM, KH, CL) và **PM** (VH, EN, RR). Mỗi hàng cộng đủ 100.

| Loại ticket | TM | KH | CL | VH | EN | RR |
|---|---:|---:|---:|---:|---:|---:|
| **New Feature** | 28 | 23 | 26 | 5 | 10 | 8 |
| **Enhancement / Maintain** | 18 | 28 | 18 | 13 | 15 | 8 |
| **Bug Fix** | 11 | 24 | 11 | 35 | 5 | 14 |
| **Tech Debt** | 5 | 5 | 15 | 21 | 41 | 13 |
| **Ops / Infra** | 5 | 8 | 13 | 43 | 18 | 13 |
| **Security** | 2 | 10 | 13 | 18 | 8 | 50 |
| **Research / Spike** | 6 | 6 | 29 | 12 | 29 | 18 |

> Ghi chú: trọng số này được chuẩn hóa lại từ mô hình 8 tiêu chí gốc sau khi bỏ Effort (EF) và Confidence (CF), giữ nguyên tỷ lệ tương đối giữa 6 tiêu chí còn lại và scale về tổng 100.

---

## 8. Priority lane đề xuất

| Business Value Score | Priority lane | Ý nghĩa |
|---:|---|---|
| 80–100 | Expedite / Sprint gần nhất | Nên xử lý ngay hoặc đưa vào sprint gần nhất |
| 65–79 | High Priority | Nên ưu tiên trong planning hiện tại |
| 50–64 | Medium Priority | Có value, nhưng cần so sánh với các ticket khác |
| < 50 | Backlog / Batch | Chưa nên làm riêng; cân nhắc gom batch hoặc chờ thêm evidence |

---

## 9. Hard gate: các trường hợp không chờ scoring

| Trường hợp | Hành động đề xuất |
|---|---|
| SEV1 / incident nghiêm trọng | Expedite |
| Security đang bị khai thác hoặc credential leak nghiêm trọng | Expedite |
| Deadline pháp lý/compliance cứng | Expedite |
| SLA/SLO đang breach hoặc error budget burn rất cao | Expedite |
| Cam kết hợp đồng với khách hàng chiến lược có deadline cụ thể | Expedite |

Scoring vẫn có thể thực hiện sau đó để ghi nhận business value và phục vụ retrospective.

---

## 10. Quy trình áp dụng trong backlog

1. **Intake thông tin ticket:** mô tả vấn đề, người bị ảnh hưởng, thiệt hại nếu không làm, evidence, deadline/dependency và estimate sơ bộ.
2. **Phân loại ticket:** New Feature, Enhancement/Maintain, Bug Fix, Tech Debt, Ops/Infra, Security hoặc Research/Spike.
3. **Kiểm tra hard gate:** nếu là incident/security/compliance/SLO critical thì đưa vào expedite lane.
4. **Chấm điểm 6 tiêu chí:**
   - **DM** chấm **TM, KH, CL** (góc nhìn business/khách hàng/chiến lược).
   - **PM** chấm **VH, EN, RR** (góc nhìn vận hành/nền tảng/rủi ro).
5. **Tính điểm cuối:** áp dụng trọng số theo loại ticket.
6. **Ra quyết định priority lane:** dựa trên điểm, hard gate, dependency và capacity sprint.
7. **Review định kỳ:** kiểm tra ticket điểm cao có thật sự tạo value, điều chỉnh rubric/trọng số nếu cần.

---

## 11. Template đánh giá ticket

```text
Ticket title:
Ticket type:
Requester:
Target user/customer:
Problem statement:
Expected outcome:
Deadline/dependency:
Evidence:

Scoring (DM):
- TM:
- KH:
- CL:

Scoring (PM):
- VH:
- EN:
- RR:

Business Value Score:
Priority lane:
Recommendation:
Missing information:
Assumptions:
```

---

## 12. Ví dụ minh họa

### Ví dụ 1: Fix lỗi notification không gửi

**Loại ticket:** Bug Fix

**Bối cảnh:** 12% notification bị fail trong 3 ngày gần đây, ảnh hưởng trực tiếp workflow user, support nhận nhiều complaint, có log lỗi rõ ràng, nguyên nhân đã xác định.

| Người chấm | Tiêu chí | Điểm | Lý do |
|---|---|---:|---|
| DM | TM | 2 | Không trực tiếp tạo revenue, nhưng ảnh hưởng trust |
| DM | KH | 5 | User-facing, nhiều complaint |
| DM | CL | 3 | Ảnh hưởng flow quan trọng |
| PM | VH | 5 | Fail rate rõ, ảnh hưởng vận hành |
| PM | EN | 1 | Không mở đường nhiều cho tương lai |
| PM | RR | 2 | Có thể ảnh hưởng cam kết service nhưng chưa nghiêm trọng |

```text
(2×11 + 5×24 + 3×11 + 5×35 + 1×5 + 2×14) / 5 = 76.6
```

**Kết luận:** 76.6 điểm → High Priority.

### Ví dụ 2: Refactor module notification

**Loại ticket:** Tech Debt

**Bối cảnh:** Code hiện tại khó maintain, mỗi lần thêm notification mới mất nhiều thời gian, đã gây 3 bug production trong 2 tháng, mở đường cho nhiều feature notification sau này.

| Người chấm | Tiêu chí | Điểm | Lý do |
|---|---|---:|---|
| DM | TM | 1 | Không tạo revenue trực tiếp |
| DM | KH | 2 | Gián tiếp giảm bug cho user |
| DM | CL | 4 | Liên quan roadmap notification sắp tới |
| PM | VH | 4 | Giảm bug production, giảm support/on-call |
| PM | EN | 5 | Mở đường cho nhiều feature sau |
| PM | RR | 2 | Có risk lỗi nhưng không phải compliance/security |

```text
(1×5 + 2×5 + 4×15 + 4×21 + 5×41 + 2×13) / 5 = 78.0
```

**Kết luận:** 78.0 điểm → High Priority.

### Ví dụ 3: Rotate secret bị lộ

**Loại ticket:** Security

**Bối cảnh:** Secret nằm trong repository private, chưa thấy dấu hiệu bị khai thác, secret có quyền truy cập staging và một phần production config, fix tương đối rõ.

| Người chấm | Tiêu chí | Điểm | Lý do |
|---|---|---:|---|
| DM | TM | 1 | Không tạo revenue trực tiếp |
| DM | KH | 3 | Nếu bị khai thác sẽ ảnh hưởng trust |
| DM | CL | 4 | Security hygiene quan trọng |
| PM | VH | 3 | Có thể ảnh hưởng vận hành nếu bị abuse |
| PM | EN | 2 | Có thể cải thiện process secret management |
| PM | RR | 5 | Credential exposure là risk cao |

```text
(1×2 + 3×10 + 4×13 + 3×18 + 2×8 + 5×50) / 5 = 80.8
```

**Kết luận:** 80.8 điểm → Làm ngay. Nếu có bằng chứng bị khai thác, đưa vào hard gate/expedite.

---

## 13. Cách diễn giải với cấp trên

Đề xuất áp dụng mô hình **Business Value Score per Ticket** nhằm chuẩn hóa cách đánh giá và ưu tiên backlog trong môi trường IT Product. Mỗi ticket được đánh giá theo 6 nhóm tiêu chí, chia cho 2 vai trò:

- **DM** đánh giá phía business: Thương mại (TM), Khách hàng (KH), Chiến lược/Khẩn cấp (CL).
- **PM** đánh giá phía sản phẩm/kỹ thuật: Vận hành/Reliability (VH), Enablement tương lai (EN), Risk/Compliance/Security (RR).

Mỗi tiêu chí được chấm từ 0 đến 5. Sau đó hệ thống áp dụng trọng số khác nhau tùy loại ticket như New Feature, Enhancement, Bug Fix, Tech Debt, Ops/Infra, Security hoặc Research/Spike. Kết quả cuối cùng là điểm 0–100, dùng làm một input định lượng cho backlog prioritization.

Mô hình này giúp team cân bằng giữa delivery feature mới và các công việc quan trọng khác như fix bug, security, reliability và tech debt. Nhờ đó, stakeholder có thể nhìn thấy business value của cả những ticket kỹ thuật vốn khó giải thích bằng ngôn ngữ business.

---

## 14. Lưu ý khi triển khai

- Không dùng điểm số như quyết định tuyệt đối; điểm số là input cho thảo luận planning.
- Cần ghi rõ evidence và assumption khi chấm.
- Với ticket thiếu dữ liệu, không nên tự động chấm cao; nên hạ điểm các tiêu chí thiếu bằng chứng hoặc tạo Research/Spike để làm rõ trước.
- DM và PM nên thống nhất ngắn gọn ở các ticket biên (điểm gần ngưỡng lane) để tránh lệch góc nhìn.
- Trọng số có thể được điều chỉnh theo chiến lược từng giai đoạn.
- Nên review mô hình sau 1–2 sprint đầu tiên để calibrate.
- Nên đo lại kết quả sau khi ticket hoàn thành để kiểm tra scoring có phản ánh đúng value thực tế không.

---

## 15. Kết luận

Khung Business Value Score (6 tiêu chí) giúp chuyển backlog prioritization từ cảm tính sang có cấu trúc, đồng thời phân định rõ trách nhiệm đánh giá giữa DM (business) và PM (sản phẩm/kỹ thuật). Mô hình không chỉ ưu tiên feature mới, mà còn giúp nhìn nhận đúng business value của bug fix, tech debt, security, reliability và các hoạt động enablement dài hạn.

Khi được áp dụng nhất quán, framework này hỗ trợ planning minh bạch hơn, ưu tiên backlog công bằng hơn, giao tiếp tốt hơn giữa business và engineering, giảm tranh luận cảm tính, đồng thời bảo vệ chất lượng sản phẩm và tốc độ phát triển dài hạn.
