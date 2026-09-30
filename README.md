# PharmEasy Regional Pulse — Data Analytics & AI Capstone

## 📌 Executive Cover Note

### 1. Headline Finding
Between April and May 2026, Guntur recorded an extraordinary month-on-month sales surge of **+122.19%** (rising from ₹62,442.27 to ₹138,738.93) before partially retracing in June (−28.11% to ₹99,745.18), representing the single largest percentage swing in the dataset.

### 2. The 4 Evaluation Artifacts
- **Live Interactive Dashboard (`app.py`):** Multi-level Streamlit + Plotly application for exploratory visual analysis across Overview, Category, and Detail levels with dynamic regional filtering.
- **Embedded CII Narrative (inside `app.py`):** Context–Insight–Implication executive summary at the top of the dashboard framing what the high-level metrics mean operationally.
- **One-Page Recommendation Memo (`memo.md`):** Formal 7-field decision document with inline verification risk tiers (`[LOW]`, `[MEDIUM]`, `[HIGH]`) guiding leadership on actionable next steps.
- **Presentation Storyline (`presentation_storyline.md`):** Dual audience-reframed presentation narratives (SCR for executives and OCD for regional leads) alongside an analytically rigorous 3-question pushback defense.

### 3. Recommended Reviewer Consumption Order
To evaluate this project coherently, review the deliverables in this sequence:
1. **`app.py` (Embedded CII Summary & Live Dashboard):** Grasp the headline findings and explore regional/category patterns interactively.
2. **`memo.md`:** Review the grounded business recommendation and risk-tiered evidence.
3. **`presentation_storyline.md`:** See how the core finding is tailored for executive vs. operational audiences and defended against stakeholder skepticism.
4. **Data & Metrics Pipeline Scripts (`clean_data.py`, `build_db.py`, `queries.py`, `metrics_engine.py`, `review_gate.py`):** Verify data foundation rigor, SQL joins, deterministic calculations, and audit logging.

### 4. Upfront Unverified Assumption
> **From `memo.md` (Assumptions):**  
> *"Hypothesis: The increase could be related to changes in the number of orders, products or quantities sold. However, the current analysis does not provide enough evidence to confirm the reason for the increase. Further analysis of the order-level data is required."*

---

## 🚀 Setup & Execution Guide

### Prerequisites
- Python 3.9+
- Standard packages: `pandas`, `plotly`, `streamlit`

Install dependencies:
```bash
pip install pandas plotly streamlit
```

---

## 🛠️ Step-by-Step Pipeline Execution

### Part 1 — Data Foundation & Validation
1. **Regenerate Raw Dataset:**
   ```bash
   python generate_dataset.py
   ```
   *Generates deterministic `pharmeasy_orders_raw.csv` (2,159 rows) and `regions_master.csv` (10 rows).*

2. **Clean & Validate Data:**
   ```bash
   python clean_data.py
   ```
   *Removes 59 duplicates, standardizes 9 canonical regions, imputes missing categories and profits, verifies schema on clean and broken copies, and writes `orders_clean.csv` (2,100 rows).*
   *Review data quality dimensions in `data_quality_report.md`.*

---

### Part 2 — SQL Metrics & Significance Flagging
1. **Build SQLite Database:**
   ```bash
   python build_db.py
   ```
   *Creates `pharmeasy.db` with tables `orders_clean` and `regions_master`.*

2. **Run JOIN Validations & Audits:**
   ```bash
   python queries.py
   ```
   *Verifies zero-order region survival (Kurnool 2101 LEFT vs 2100 INNER), order_id uniqueness, and COUNT(*) vs COUNT(fk).*

3. **Compute Metrics & Operational Flags:**
   ```bash
   python metrics_engine.py
   ```
   *Computes MoM growth, flags regions crossing the 8% operational threshold, and verifies state persistence round-tripping via `state.json`.*

---

### Part 3 — Insights, Governance & Review Gate
1. **Generate CII Blocks:**
   ```bash
   python draft_report.py
   ```
   *Generates Context–Insight–Implication blocks for all flagged regions.*

2. **Run Human Review Gate & Audit Log:**
   ```bash
   python review_gate.py
   ```
   *Executes test harness across `approve`, `edit`, and `reject` decision paths and records entries into `audit_log.jsonl`.*

3. **Check Reliability Governance:**
   *Review `memo.md` and `reliability_checklist.md`.*

---

### Part 4 — Dashboard & Presentation
1. **Launch Streamlit Dashboard:**
   ```bash
   streamlit run app.py
   ```
   *Runs locally with zero external API keys or network dependencies.*

2. **Review Stakeholder Defense:**
   *Examine `presentation_storyline.md` for SCR, OCD, and 3-step Direct Acknowledgement Q&A.*

---

## 📁 Repository Structure

```
├── generate_dataset.py       # Deterministic dataset builder (seed 2026)
├── clean_data.py             # Data cleaning pipeline & schema validator
├── data_quality_report.md    # 7 data quality dimensions mapping
├── build_db.py               # SQLite database initializer (pharmeasy.db)
├── queries.py                # SQL JOIN validations and metrics queries
├── metrics_engine.py         # MoM percentage changes, 8% alerting, state persistence
├── draft_report.py           # CII insight generation for flagged regions
├── memo.md                   # 1-page risk-tiered recommendation memo
├── review_gate.py            # Governance review gate with 3 decision paths
├── audit_log.jsonl           # Audit trail of review gate decisions
├── reliability_checklist.md  # 4-step reliability workflow checklist
├── app.py                    # Streamlit + Plotly 3-level dashboard
├── presentation_storyline.md # SCR & OCD reframings + stakeholder Q&A defense
├── README.md                 # Project cover note, setup & execution instructions
├── pharmeasy_orders_raw.csv  # Raw data export
├── regions_master.csv        # Master region reference data
└── orders_clean.csv          # Cleaned working dataset
```
