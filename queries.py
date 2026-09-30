# ==============================================================================
# Task 2.2 — SQL JOIN Validation & Task 2.3 — Region × Month Metrics
# ==============================================================================
import sqlite3
import pandas as pd

conn = sqlite3.connect('pharmeasy.db')

# Task 2.2: Row-count check — LEFT JOIN vs INNER JOIN (Kurnool zero-order delta)
query1 = '''SELECT COUNT(*) FROM regions_master r LEFT JOIN orders_clean o ON r.region=o.region'''
left_count = conn.execute(query1).fetchone()[0]
print("LEFT JOIN count:", left_count)

query2 = '''SELECT COUNT(*) FROM regions_master r INNER JOIN orders_clean o ON r.region=o.region'''
inner_count = conn.execute(query2).fetchone()[0]
print("INNER JOIN count:", inner_count)

# Task 2.2: Duplicate-key check — verify order_id uniqueness
query3 = '''SELECT order_id FROM orders_clean GROUP BY order_id HAVING COUNT(*)>1'''
result3 = conn.execute(query3).fetchall()
print("Duplicate order_id check (should be empty):", result3)

# Task 2.2: Null check — COUNT(*) vs COUNT(order_id) showing Kurnool 1 vs 0 pitfall
query4 = '''SELECT r.region, COUNT(*) FROM regions_master r LEFT JOIN orders_clean o ON r.region=o.region GROUP BY r.region'''
result4 = conn.execute(query4).fetchall()
print("COUNT(*) count:", result4)

query5 = '''SELECT r.region, COUNT(o.order_id)
FROM regions_master r
LEFT JOIN orders_clean o
ON r.region=o.region
GROUP BY r.region'''

result5 = conn.execute(query5).fetchall()
print("COUNT(o.order_id) count:", result5)

query6 = '''
SELECT
    r.region,
    COUNT(*) AS count_star,
    COUNT(o.order_id) AS count_order_id
FROM regions_master r
LEFT JOIN orders_clean o
ON r.region = o.region
GROUP BY r.region
HAVING COUNT(*) <> COUNT(o.order_id)
'''

result6 = conn.execute(query6).fetchall()
print("Where counts disagree:", result6)

# Task 2.2: Per-region order counts via LEFT JOIN + GROUP BY, ordered ascending
query7 = '''SELECT r.region, COUNT(o.order_id) AS order_count FROM regions_master r LEFT JOIN orders_clean o ON r.region=o.region GROUP BY r.region ORDER BY r.region ASC'''
result7 = conn.execute(query7).fetchall()
print("Region order counts:", result7)

# Task 2.3: Region × month sales metrics (Apr, May, Jun 2026) via SQL GROUP BY
query8 = '''SELECT r.region, SUM(o.sales_inr) AS total_sales, strftime("%Y-%m",o.order_date) AS month FROM regions_master as r LEFT JOIN orders_clean as o ON r.region=o.region GROUP BY r.region,month ORDER BY r.region,month'''
result8 = conn.execute(query8).fetchall()
print("Region and monthly order counts:", result8)

conn.close()
