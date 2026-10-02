# ==============================================================================
# Task 2.3 — Region × Month Metrics & Task 2.4 — Significance Flagging Engine
# ==============================================================================
import pandas as pd
import sqlite3
import os
import json

conn = sqlite3.connect('pharmeasy.db')
query8 = '''SELECT r.region, SUM(o.sales_inr) AS total_sales, strftime("%Y-%m",o.order_date) AS month FROM regions_master as r LEFT JOIN orders_clean as o ON r.region=o.region GROUP BY r.region,month ORDER BY r.region,month'''
result8 = conn.execute(query8).fetchall()
conn.close()

monthly_sales = pd.DataFrame(result8, columns=['region', 'total_sales', 'month'])

monthly_pivot = monthly_sales.pivot(
    index='region',
    columns='month',
    values='total_sales'
)

monthly_pivot = monthly_pivot.reindex(
    columns=['2026-04', '2026-05', '2026-06']
)

monthly_summary = monthly_pivot.to_dict(orient='index')
print("Monthly Summary:")
print(monthly_summary)

summaries = {}

for region, monthly_values in monthly_summary.items():
    for month, value in monthly_values.items():
        if month not in summaries:
            summaries[month] = {}

        if pd.isna(value):
            summaries[month][region] = None 
        else:   
            summaries[month][region] = value

april_summary = summaries['2026-04']
may_summary = summaries['2026-05']
june_summary = summaries['2026-06']

# Task 2.4: compute_percentage_change_v1
# Handles zero or missing previous values by returning 0

def compute_percentage_change_v1(current, previous):
    if previous == 0 or previous is None:
        return 0
    return (current - previous) / previous * 100

mom_changes = {}

for region, monthly_values in monthly_summary.items():
    april = monthly_values['2026-04']
    may = monthly_values['2026-05']
    june = monthly_values['2026-06']

    apr_to_may = compute_percentage_change_v1(may, april)
    may_to_jun = compute_percentage_change_v1(june, may)

    mom_changes[region] = {
        'apr_to_may': round(apr_to_may, 2),
        'may_to_jun': round(may_to_jun, 2)
    }

print("\nMonth-on-Month Changes:")
print(mom_changes)

# Task 2.4: flag_significant_regions_v1 (threshold=8% operational alert)
def flag_significant_regions_v1(changes, threshold=8):
    flagged = {}

    for region, monthly_values in changes.items():
        triggered = {}
        for month, value in monthly_values.items():
            if abs(value) > threshold:
                triggered[month] = value
        
        if triggered:
            flagged[region] = triggered
    return flagged

flagged_regions = flag_significant_regions_v1(mom_changes, 8)
print("\nFlagged Regions (Threshold = 8%):")
print(flagged_regions)

# Task 2.4: State persistence functions (save_state_v1 and load_previous_state_v1)
state_path = "state.json"

def load_previous_state_v1(path):
    if os.path.exists(path):
        with open(path) as f:
            return json.load(f)
    return None

def save_state_v1(month_summary, path):
    with open(path, 'w') as f:
        json.dump(month_summary, f, indent=2)

save_state_v1(april_summary, state_path)
previous_state = load_previous_state_v1(state_path)
print("\nState persistence round-trip check (April summary == reloaded state):", april_summary == previous_state)
