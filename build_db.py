# ==============================================================================
# Task 2.1 — Build SQLite Database (pharmeasy.db)
# ==============================================================================
import pandas as pd
import sqlite3

orders_df = pd.read_csv("orders_clean.csv")
regions_df = pd.read_csv("regions_master.csv")

print("orders_df shape:", orders_df.shape)
print("regions_df shape:", regions_df.shape)

conn = sqlite3.connect('pharmeasy.db')
orders_df.to_sql('orders_clean', conn, if_exists='replace', index=False)
regions_df.to_sql('regions_master', conn, if_exists='replace', index=False)
print("Successfully created pharmeasy.db with tables orders_clean and regions_master")
conn.close()
