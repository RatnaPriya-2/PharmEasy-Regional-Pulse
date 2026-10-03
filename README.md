# PharmEasy Regional Pulse — Regional Performance Intelligence Pipeline

## 1. Setup & End-to-End Pipeline Execution Guide

### Prerequisites

- Python 3.9+
- Standard open-source libraries: `pandas`, `plotly`, `streamlit` (`sqlite3` is built-in)
- Zero paid services, zero API keys, zero signup-gated tools required.

### Installation

Install the necessary packages:

```bash
pip install pandas plotly streamlit
```

### End-to-End Execution Commands

Run the complete pipeline from scratch using these exact commands in order:

```bash
# Step 1: Generate the raw dataset deterministically (seed 2026)
python generate_dataset.py

# Step 2: Clean the data, impute missing values, and validate schema
python clean_data.py

# Step 3: Build the SQLite database (pharmeasy.db)
python build_db.py

# Step 4: Run SQL JOIN validations and metrics queries
python queries.py

# Step 5: Run the metrics engine, 8% alerting, and state persistence
python metrics_engine.py

# Step 6: Generate Context-Insight-Implication (CII) narrative blocks
python draft_report.py

# Step 7: Run human review gate test harness (approve, edit, reject) & generate audit log
python review_gate.py

# Step 8: Launch the interactive Streamlit dashboard
streamlit run app.py
```

---

## 2. Executive Cover Note — Key Evaluation Artifacts

### Headline Finding

Between April and May 2026, Guntur recorded a **+122.19% month-on-month sales increase** (rising from ₹62,442.27 to ₹138,738.93) before partially retracing in June (**−28.11%** to ₹99,745.18), representing the **largest-magnitude flagged month-on-month swing** in the dataset.

### Pointers to the 4 Evaluation Artifacts

- **Streamlit Dashboard (`app.py`):** Live data exploration tool implementing a 3-level hierarchy (Overview, Category, Detail) connected by an interactive region filter.
- **Embedded CII Narrative (inside `app.py`):** Executive summary embedded at the top of the dashboard framing what the high-level metrics mean operationally.
- **One-Page Memo (`memo.md`):** Formal 7-field decision document with inline verification risk tiers (`[LOW]`, `[MEDIUM]`, `[HIGH]`) for each factual claim.
- **Presentation Storyline (`presentation_storyline.md`):** Dual audience-reframed presentation narratives (SCR for executives and OCD for regional leads) alongside a stakeholder pushback defense.

### Recommended Reviewer Consumption Order

To evaluate this project coherently, review the deliverables in this sequence:

1. **`app.py` (Embedded CII Summary & Live Dashboard):** Grasp the headline findings and explore regional and category patterns interactively.
2. **`memo.md`:** Review the grounded business recommendation and verification-risk-tagged claims.
3. **`presentation_storyline.md`:** See how the core finding is tailored for executive vs. operational audiences and defended against stakeholder skepticism.
4. **Data & Metrics Pipeline Scripts (`clean_data.py`, `build_db.py`, `queries.py`, `metrics_engine.py`, `review_gate.py`):** Verify data foundation rigor, SQL joins, deterministic calculations, and audit logging.

### Upfront Unverified Assumption

> **From `memo.md` (Assumptions):**
>
> *"Hypothesis: The increase could be related to changes in the number of orders, products or quantities sold. However, the current analysis does not provide enough evidence to confirm the reason for the increase. Further analysis of the order-level data is required."*

---

## 📁 Repository Structure

```text
├── generate_dataset.py       # Deterministic dataset builder (seed 2026)
├── clean_data.py             # Data cleaning pipeline & schema validator
├── data_quality_report.md    # 7 data quality dimensions mapping
├── build_db.py               # SQLite database initializer (pharmeasy.db)
├── queries.py                # SQL JOIN validations and metrics queries
├── metrics_engine.py         # MoM percentage changes, 8% threshold flagging, state persistence
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
├── orders_clean.csv          # Cleaned working dataset
├── pharmeasy.db              # SQLite verified database
└── state.json                # Persisted state for incremental metrics
```