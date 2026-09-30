# ==============================================================================
# Task 1.2 — Data Cleaning Pipeline & Task 1.3 — Schema Validation
# ==============================================================================
import pandas as pd

# Step 1.2: Cleaning pipeline
df = pd.read_csv("pharmeasy_orders_raw.csv")
print("Total Rows:", len(df))

# Remove duplicates after counting them
duplicate_count = df.duplicated().sum()
print("Duplicates :", duplicate_count)

df = df.drop_duplicates()

missing_category_count = df['category'].isna().sum()
missing_profit_count = df['profit_inr'].isna().sum()
print("Missing Category:", missing_category_count)
print("Missing Profit :", missing_profit_count)

print(f"Removed {duplicate_count} duplicate rows")

# Normalise the region names (remove extra white spaces and add title case)
df['region'] = df['region'].str.strip().str.title()

# Impute categories where missing for products from already known product category lookup
known_category_rows = df[df['category'].notna()]
product_category_lookup = dict(zip(known_category_rows['product'], known_category_rows['category']))
df['category'] = df['category'].fillna(df['product'].map(product_category_lookup))
print("Missing Category after imputation:", df['category'].isna().sum())

# Impute profit where missing for sales
known_profit_rows = df[df['profit_inr'].notna()].copy()
known_profit_rows['margin'] = known_profit_rows['profit_inr'] / known_profit_rows['sales_inr']
category_mean_margin = known_profit_rows.groupby('category').agg({'margin': 'mean'})
category_mean_margin_table = category_mean_margin['margin'].to_dict()

df['profit_inr'] = df['profit_inr'].fillna(df['sales_inr'] * df['category'].map(category_mean_margin_table)).round(2)

print("Missing Profit after imputation:", df['profit_inr'].isna().sum())
print(df.isna().sum())
print("Duplicates remaining:", df.duplicated().sum())
print("Unique regions:", df['region'].unique())
print("Region count:", df['region'].nunique())
print("Total number of rows and columns:", df.shape)

df.to_csv("orders_clean.csv", index=False)

# Validation
df = pd.read_csv("orders_clean.csv")

required_columns = ["order_id", "order_date", "region", "category", "product", "quantity", "sales_inr", "profit_inr"]

def validate_schema(df, required_columns):
    missing = [column for column in required_columns if column not in df.columns]

    if missing:
        return {'ok': False, 'status': 'blocked_schema', 'missing': missing, 'rows': None}
    return {'ok': True, 'status': 'validated', 'missing': [], 'rows': len(df)}

print("\n--- Schema Validation (Clean Data) ---")
print(validate_schema(df, required_columns))

print("\n--- Schema Validation (Deliberately Broken Copy) ---")
df2 = df[["order_id", "order_date", "region", "category", "product", "quantity"]].copy()
print(validate_schema(df2, required_columns))
