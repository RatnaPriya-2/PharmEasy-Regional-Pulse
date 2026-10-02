# Presentation Storyline

## 1. For an Executive — Situation–Complication–Resolution (SCR)

*Reframing the Guntur April→May +122.19% finding*

### Situation
*(What is true today)*

Guntur is one of nine PharmEasy regions tracked in the April–June 2026 dataset.

For the full quarter, total sales across all regions were ₹32,65,191 across 2,100 distinct orders.

Guntur's April sales stood at ₹62,442.27, before rising sharply in May.

### Complication
*(The surprising or at-risk element)*

In May, Guntur's sales increased to ₹138,738.93 — a **+122.19% increase** from April.

This was the largest month-on-month percentage swing recorded across the regions in the dataset; the next-largest increase was Tirupati at +66.87%.

The increase then partially reversed in June, with sales falling 28.11% to ₹99,745.18.

Therefore, the available data does not establish whether the May increase was a one-time surge or part of a sustained trend.

Acting on the increase without verification could lead to planning decisions based on a movement that may not recur.

### Resolution
*(Recommended action and next steps)*

Before the next planning cycle, the Guntur May order mix should be pulled by category to determine which categories contributed to the spike and whether those orders have repeat potential.

If further analysis confirms sustained demand growth, the Guntur target can be reviewed; if the movement appears to be one-off, it should be treated as an exceptional month rather than assumed to represent the future trend.

The dashboard's Category and Detail views provide the starting point for this investigation.

---

## 2. For a Regional Manager — Overview–Category–Detail (OCD)

*Reframing the same Guntur April→May +122.19% finding*

### Overview
*(The headline number)*

Guntur posted a **+122.19% month-on-month sales increase** in May 2026, rising from ₹62,442.27 in April to ₹138,738.93.

June then pulled back by 28.11% to ₹99,745.18, leaving the quarterly total at ₹3,00,926.38.

This was the largest month-on-month percentage swing recorded across the regions in the dataset.

### Category
*(Which specific area drives it)*

The dashboard's Category Breakdown for Guntur shows which of the six product categories — Medical Devices, Wellness & Nutrition, Prescription Medicines, Lab Tests, Personal Care, and OTC Medicines — were responsible for the May uplift.

Identifying whether the spike is concentrated in one high-ticket category (such as Medical Devices) or spread across several categories is a useful starting point.

A concentrated spike could indicate a one-time bulk order, while a broad-based rise may provide stronger evidence of wider demand — but either interpretation would need to be verified using order-level and business-context data.

### Detail
*(The supporting evidence and methodology)*

The per-region, per-month detail table in the dashboard shows order counts, sales, and profit for each month. Sales and profit are reported as sums; the order count uses a distinct `order_id` count rather than a raw row count, avoiding double-counting of the order-count metric.

April → May order volume for Guntur should be compared alongside the sales figure.

If order count also increased substantially, that would provide evidence that the sales increase was accompanied by higher transaction volume; if order count rose only slightly while sales increased sharply, the movement may have been driven by a smaller number of higher-value orders.

The underlying reason and repeatability would still need to be verified.

---

## 3. Anticipated Stakeholder Pushback — Q&A

*Each answer follows the 3-step Direct Acknowledgement Pattern:*
*(1) acknowledge the concern specifically → (2) state what is verified vs. not verified → (3) state exactly what would resolve the uncertainty and by when.*

---

### Q1. "Why should I believe this number?"
*(Category: credibility of the figure)*

**(1) Acknowledging the concern specifically:**

That is a fair challenge — a 122.19% single-month increase is significant enough to review the underlying records before acting on it.

**(2) What is verified vs. not verified:**

**Verified:** The April and May Guntur sales totals (₹62,442.27 and ₹138,738.93) were recalculated from `orders_clean.csv` as a sum of `sales_inr` and reconcile with the Part 2 per-region monthly figures. The corresponding order counts were calculated using distinct `order_id`. The percentage change was recalculated using the Part 2 formula and gives 122.19%.

**Not verified:** Whether the original source extract contains any unusual or test records within the May Guntur orders that could affect the reported figure.

**(3) What would resolve the uncertainty and by when:**

A line-by-line comparison of the May Guntur rows in `orders_clean.csv` against the original source extract — checking for duplicate `order_id` values or unusually high unit prices — would provide a direct check of the May Guntur records against the original source.

This check can be completed before the next regional review meeting.

---

### Q2. "What if an alternative explanation is driving this?"
*(Category: alternative explanations)*

**(1) Acknowledging the concern specifically:**

Correct — the dashboard shows *what* happened (sales volume), not *why* it happened. A local promotional campaign, a bulk institutional order, or even a one-off data migration could produce the same pattern without reflecting genuine market demand.

**(2) What is verified vs. not verified:**

**Verified:** The May sales figure is based on multiple order records in the cleaned dataset, and the Detail view provides the corresponding distinct order count for each month. This shows the movement is not based solely on one recorded order, although it does not by itself establish the reason for the increase.

**Not verified:** Whether a regional promotion, a new institutional client, or a seasonal event coincided with May in Guntur; the current dataset contains no promotional or client-type fields that would allow this to be tested directly.

**(3) What would resolve the uncertainty and by when:**

Cross-referencing the May Guntur orders against the CRM or promotion calendar would help determine whether a planned campaign coincided with the spike.

This can be requested from the sales operations team and resolved within one week of this meeting.