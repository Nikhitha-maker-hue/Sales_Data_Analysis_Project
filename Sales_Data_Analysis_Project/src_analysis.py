"""
Sales Data Analysis Project
Author: Portfolio Project
Tools: Python, Pandas, Matplotlib
"""

import os
import pandas as pd
import matplotlib.pyplot as plt

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_FILE = os.path.join(BASE_DIR, "data", "sales_data.csv")
OUTPUT_DIR = os.path.join(BASE_DIR, "output", "charts")
os.makedirs(OUTPUT_DIR, exist_ok=True)

df = pd.read_csv(DATA_FILE, parse_dates=["Order_Date"])
df["Month"] = df["Order_Date"].dt.to_period("M").astype(str)

# Basic KPIs
total_revenue = df["Revenue"].sum()
total_profit = df["Profit"].sum()
total_orders = df["Order_ID"].nunique()
unique_customers = df["Customer_ID"].nunique()
average_order_value = total_revenue / total_orders
profit_margin = total_profit / total_revenue

print("=== SALES ANALYSIS ===")
print(f"Total Revenue:       {total_revenue:,.2f}")
print(f"Total Profit:        {total_profit:,.2f}")
print(f"Total Orders:        {total_orders:,}")
print(f"Unique Customers:    {unique_customers:,}")
print(f"Average Order Value: {average_order_value:,.2f}")
print(f"Profit Margin:       {profit_margin:.2%}")

# 1. Monthly trend
monthly = df.groupby("Month", as_index=False).agg(
    Revenue=("Revenue", "sum"),
    Profit=("Profit", "sum"),
    Orders=("Order_ID", "nunique")
)

plt.figure(figsize=(10, 5))
plt.plot(monthly["Month"], monthly["Revenue"], marker="o")
plt.title("Monthly Revenue Trend")
plt.xlabel("Month")
plt.ylabel("Revenue")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_DIR, "monthly_revenue.png"), dpi=150)
plt.close()

# 2. Product performance
product = df.groupby("Product", as_index=False).agg(
    Revenue=("Revenue", "sum"),
    Profit=("Profit", "sum"),
    Quantity=("Quantity", "sum")
).sort_values("Revenue", ascending=False)

plt.figure(figsize=(10, 6))
plt.barh(product["Product"].head(10)[::-1], product["Revenue"].head(10)[::-1])
plt.title("Top 10 Products by Revenue")
plt.xlabel("Revenue")
plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_DIR, "top_products.png"), dpi=150)
plt.close()

# 3. Regional performance
region = df.groupby("Region", as_index=False).agg(
    Revenue=("Revenue", "sum"),
    Profit=("Profit", "sum"),
    Orders=("Order_ID", "nunique")
).sort_values("Revenue", ascending=False)

plt.figure(figsize=(8, 5))
plt.bar(region["Region"], region["Revenue"])
plt.title("Revenue by Region")
plt.xlabel("Region")
plt.ylabel("Revenue")
plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_DIR, "regional_revenue.png"), dpi=150)
plt.close()

# 4. Customer segment performance
segment = df.groupby("Customer_Segment", as_index=False).agg(
    Revenue=("Revenue", "sum"),
    Profit=("Profit", "sum"),
    Orders=("Order_ID", "nunique")
).sort_values("Revenue", ascending=False)

print("\nTop Products:")
print(product.head(5).to_string(index=False))

print("\nRegional Performance:")
print(region.to_string(index=False))

print("\nCustomer Segments:")
print(segment.to_string(index=False))

# Export cleaned analysis tables
monthly.to_csv(os.path.join(BASE_DIR, "output", "monthly_summary.csv"), index=False)
product.to_csv(os.path.join(BASE_DIR, "output", "product_summary.csv"), index=False)
region.to_csv(os.path.join(BASE_DIR, "output", "region_summary.csv"), index=False)
segment.to_csv(os.path.join(BASE_DIR, "output", "segment_summary.csv"), index=False)
