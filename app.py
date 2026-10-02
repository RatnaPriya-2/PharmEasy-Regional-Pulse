import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="PharmEasy Sales Dashboard",
    page_icon="💊",
    layout="wide",
)

# Data loading
@st.cache_data
def load_data():
    df = pd.read_csv("orders_clean.csv")
    df["order_date"] = pd.to_datetime(df["order_date"])
    df["month"] = pd.Categorical(
        df["order_date"].dt.strftime("%b"),
        categories=["Apr", "May", "Jun"],
        ordered=True,
    )
    return df

orders_df = load_data()
MONTH_ORDER = ["Apr", "May", "Jun"]
FLAGGED_REGION = "Guntur"

# Page header
st.title("💊 PharmEasy Regional Sales Dashboard")
st.caption("April – June 2026  |  Andhra Pradesh & Telangana")

# Task 4.2 - Embedded Executive Summary (CII format, 4 sentences)
# Structure: Headline KPIs -> Trend/Shape -> Category/Region breakdown ->
#            Implication/CTA -> Pointer to dashboard
st.subheader("📋 Executive Summary")
st.info(
    "Across **2,100 distinct orders** in April–June 2026, PharmEasy recorded "
    "total sales of **₹32,65,191** and total profit of **₹4,92,280**, with "
    "Medical Devices and Wellness & Nutrition as the top two revenue-contributing categories. "
    "Sales trended upward from April to May across most regions before partially retracing "
    "in June, with Guntur recording a **+122.19%** increase April→May and "
    "Visakhapatnam recording a **−62.46%** decrease over the same period. "
    "These opposing regional movements suggest the May uplift was not uniform — it is "
    "concentrated in specific regions and categories, so allocating inventory or staffing "
    "based on the aggregate number alone risks misreading demand. "
    "Guntur's May spike warrants immediate verification of the order mix before committing "
    "to any supply or resourcing changes — use the Category and Detail sections below to drill in."
)

st.markdown("---")

# Region filter - connects all 3 hierarchy levels
# Filters: Overview KPIs, Category breakdown, Detail table.
# Bar chart (total sales by region) and line chart (monthly sales by region)
# are all-region comparison charts as defined by the spec - they use orders_df.
region_options = ["All Regions"] + sorted(orders_df["region"].unique().tolist())
selected_region = st.selectbox("🔍 Filter by Region", region_options)

region_df = (
    orders_df.copy()
    if selected_region == "All Regions"
    else orders_df[orders_df["region"] == selected_region].copy()
)

st.markdown("---")

# LEVEL 1 - OVERVIEW
# Task 4.1: KPI cards - total sales (INR), total profit (INR), total order count
# Order count must use distinct order_id, not a raw row count
st.markdown("## 📊 Level 1 — Overview")

total_sales  = region_df["sales_inr"].sum()
total_profit = region_df["profit_inr"].sum()
total_orders = region_df["order_id"].nunique()   # distinct-count

col1, col2, col3 = st.columns(3)
col1.metric("Total Sales (INR)",   f"₹{total_sales:,.0f}")
col2.metric("Total Profit (INR)",  f"₹{total_profit:,.0f}")
col3.metric("Total Order Count",   f"{total_orders:,}")

# Task 4.1: comparison/bar chart - total sales by region (all regions)
# Anti-pattern compliance:
#   y-axis starts at zero (rangemode="tozero")
#   no 3D
#   one neutral color; highlight color reserved for Guntur (flagged element) only
#   title answers a question; axes labeled with units
region_sales = (
    orders_df.groupby("region", observed=True)
    .agg(total_sales=("sales_inr", "sum"))
    .reset_index()
    .sort_values("total_sales", ascending=False)
)
region_sales["series"] = region_sales["region"].apply(
    lambda r: "Flagged (Guntur)" if r == FLAGGED_REGION else "All Regions"
)
fig_bar = px.bar(
    region_sales,
    x="total_sales",
    y="region",
    color="series",
    orientation="h",
    color_discrete_map={
        "All Regions": "#B7C9E2",
        "Flagged (Guntur)": "#E8543A",
    },
    category_orders={
        "region": region_sales["region"].tolist()
    },
    title="Which regions generate the most total sales? (Apr–Jun 2026)",
    labels={
        "total_sales": "Total Sales (INR ₹)",
        "region": "Region",
        "series": "",
    },
)

fig_bar.update_xaxes(
    rangemode="tozero",
    title_text="Total Sales (INR ₹)"
)

fig_bar.update_yaxes(
    title_text="Region",

)

fig_bar.update_layout(
    title_x=0.0
)

st.plotly_chart(fig_bar, width="stretch")

st.markdown("---")

# LEVEL 2 - CATEGORY BREAKDOWN
# Task 4.1: breakdown by medicine category; donut shows sales share by category
# Filter: uses region_df - responds to the region selectbox
st.markdown("## 🗂️ Level 2 — Category Breakdown")

category_sales = (
    region_df.groupby("category", observed=True)
    .agg(
        total_sales  =("sales_inr",  "sum"),
        total_orders =("order_id",   "nunique"),
        total_profit =("profit_inr", "sum"),
    )
    .reset_index()
    .sort_values("total_sales", ascending=False)
)

# Task 4.1: part-of-whole/donut chart - sales share by category (6 slices)
# Anti-pattern compliance:
#   6 slices (within 5-6 slice limit)
#   no 3D; hole=0.45 makes it a donut
#   title answers a question
fig_pie = px.pie(
    category_sales,
    names="category",
    values="total_sales",
    hole=0.45,
    title="What share of sales does each category contribute?",
    color_discrete_sequence=px.colors.qualitative.Set2,
)
fig_pie.update_traces(textposition="inside", textinfo="percent+label")
fig_pie.update_layout(title_x=0.0, showlegend=True)
st.plotly_chart(fig_pie, width='stretch')

# Category summary table
display_cat = category_sales.rename(columns={
    "category":     "Category",
    "total_sales":  "Total Sales (₹)",
    "total_orders": "Order Count",
    "total_profit": "Total Profit (₹)",
})
display_cat["Total Sales (₹)"]  = display_cat["Total Sales (₹)"].map("₹{:,.2f}".format)
display_cat["Total Profit (₹)"] = display_cat["Total Profit (₹)"].map("₹{:,.2f}".format)
st.dataframe(display_cat, hide_index=True, width='stretch')

st.markdown("---")

# LEVEL 3 - DETAIL
# Task 4.1: trend/line chart (monthly sales by region) + per-region/per-month table
st.markdown("## 📅 Level 3 — Monthly Detail")

# Task 4.1: trend/line chart - monthly sales by region across Apr/May/Jun (all regions)
# Anti-pattern compliance:
#   y-axis starts at zero (rangemode="tozero")
#   no 3D; markers=True for readability
#   one color per region/series
#   x-axis is a sequential time series (Apr/May/Jun) - line chart is valid here
#   title answers a question; axes labeled with units
monthly_region_sales = (
    orders_df.groupby(["month", "region"], observed=True)
    .agg(total_sales=("sales_inr", "sum"))
    .reset_index()
    .sort_values("month")
)

fig_line = px.line(
    monthly_region_sales,
    x="month",
    y="total_sales",
    color="region",
    markers=True,
    title="How do monthly sales trend across regions? (Apr–Jun 2026)",
    labels={
        "total_sales": "Total Sales (INR ₹)",
        "month":       "Month",
        "region":      "Region",
    },
    category_orders={"month": MONTH_ORDER},
)
fig_line.update_yaxes(rangemode="tozero", title_text="Total Sales (INR ₹)")
fig_line.update_xaxes(title_text="Month")
fig_line.update_layout(title_x=0.0)
st.plotly_chart(fig_line, width='stretch')

# Task 4.1: per-region, per-month data table - filtered by region selectbox
monthly_details = (
    region_df.groupby(["region", "month"], observed=True)
    .agg(
        total_sales  =("sales_inr",  "sum"),
        total_profit =("profit_inr", "sum"),
        total_orders =("order_id",   "nunique"),
    )
    .reset_index()
    .sort_values(["region", "month"])
    .rename(columns={
        "region":       "Region",
        "month":        "Month",
        "total_sales":  "Total Sales (₹)",
        "total_profit": "Total Profit (₹)",
        "total_orders": "Order Count",
    })
)
monthly_details["Total Sales (₹)"]  = monthly_details["Total Sales (₹)"].map("₹{:,.2f}".format)
monthly_details["Total Profit (₹)"] = monthly_details["Total Profit (₹)"].map("₹{:,.2f}".format)

st.markdown(f"**Per-region, per-month breakdown — {selected_region}**")
st.dataframe(monthly_details, hide_index=True, width='stretch')

st.caption(
    "Dashboard built with Streamlit & Plotly  ·  "
    "Source: PharmEasy orders_clean.csv, Apr–Jun 2026  ·  "
    "Order count uses distinct order_id, not row count."
)
