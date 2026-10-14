import pandas as pd
import matplotlib.pyplot as plt

# ============================================================
# DAY 4 - DATA VISUALIZATION
# ============================================================

print("==========================================")
print("         DATA VISUALIZATION")
print("==========================================")

# Load final dataset
data = pd.read_csv("data/ecommerce_analysis_ready.csv")

# Convert date column
data["order_date"] = pd.to_datetime(data["order_date"])

print("Dataset loaded successfully!")
print("Rows:", data.shape[0])
print("Columns:", data.shape[1])





# ============================================================
# 1. MONTHLY SALES TREND
# ============================================================

monthly_sales = (
    data.groupby(["year", "month", "month_name"])["sales"]
    .sum()
    .reset_index()
    .sort_values(["year", "month"])
)

plt.figure(figsize=(12, 6))

plt.plot(
    monthly_sales["month_name"],
    monthly_sales["sales"],
    marker="o"
)

plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales")

plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig(
    "data/monthly_sales_trend.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()

print("\nMonthly Sales Trend chart created successfully!")




# ============================================================
# 2. MONTHLY PROFIT TREND
# ============================================================

monthly_profit = (
    data.groupby(["year", "month", "month_name"])["profit"]
    .sum()
    .reset_index()
    .sort_values(["year", "month"])
)

plt.figure(figsize=(12, 6))

plt.plot(
    monthly_profit["month_name"],
    monthly_profit["profit"],
    marker="o"
)

plt.title("Monthly Profit Trend")
plt.xlabel("Month")
plt.ylabel("Profit")

plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig(
    "data/monthly_profit_trend.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()

print("Monthly Profit Trend chart created successfully!") 




# ============================================================
# 2. MONTHLY PROFIT TREND
# ============================================================

monthly_profit = (
    data.groupby(["year", "month", "month_name"])["profit"]
    .sum()
    .reset_index()
    .sort_values(["year", "month"])
)

# Create chart
plt.figure(figsize=(12, 6))

plt.plot(
    monthly_profit["month_name"],
    monthly_profit["profit"],
    marker="o"
)

plt.title("Monthly Profit Trend", fontsize=16)
plt.xlabel("Month")
plt.ylabel("Total Profit")

plt.xticks(rotation=45)
plt.grid(True, alpha=0.3)
plt.tight_layout()

# Save chart
plt.savefig(
    "data/monthly_profit_trend.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()

print("Monthly Profit Trend chart created successfully!")






# ============================================================
# 3. SALES BY CATEGORY
# ============================================================

sales_by_category = (
    data.groupby("category")["sales"]
    .sum()
    .sort_values(ascending=False)
)

plt.figure(figsize=(12, 6))

bars = plt.bar(
    sales_by_category.index,
    sales_by_category.values
)

plt.title("Sales by Category", fontsize=16)
plt.xlabel("Product Category")
plt.ylabel("Total Sales")

plt.xticks(rotation=35, ha="right")

# Display sales values above the bars
plt.bar_label(bars, fmt="%.0f", padding=3)

plt.tight_layout()

plt.savefig(
    "data/sales_by_category.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()

print("Sales by Category chart created successfully!")




# ============================================================
# 4. PROFIT BY CATEGORY
# ============================================================

profit_by_category = (
    data.groupby("category")["profit"]
    .sum()
    .sort_values(ascending=False)
)

plt.figure(figsize=(12, 6))

bars = plt.bar(
    profit_by_category.index,
    profit_by_category.values
)

plt.title("Profit by Category", fontsize=16)
plt.xlabel("Product Category")
plt.ylabel("Total Profit")

plt.xticks(rotation=35, ha="right")

# Display profit values above the bars
plt.bar_label(bars, fmt="%.0f", padding=3)

plt.tight_layout()

plt.savefig(
    "data/profit_by_category.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()

print("Profit by Category chart created successfully!")



# ============================================================
# 5. TOP 10 PRODUCTS BY SALES
# ============================================================

top_products = (
    data.groupby("product_name")["sales"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
    .sort_values(ascending=True)
)

plt.figure(figsize=(12, 7))

bars = plt.barh(
    top_products.index,
    top_products.values
)

plt.title("Top 10 Products by Sales", fontsize=16)
plt.xlabel("Total Sales")
plt.ylabel("Product Name")

# Display sales values beside the bars
plt.bar_label(bars, fmt="%.0f", padding=4)

plt.tight_layout()

plt.savefig(
    "data/top_10_products_by_sales.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()

print("Top 10 Products by Sales chart created successfully!")




# ============================================================
# 6. SALES BY STATE
# ============================================================

sales_by_state = (
    data.groupby("state")["sales"]
    .sum()
    .sort_values(ascending=False)
)

plt.figure(figsize=(12, 7))

bars = plt.barh(
    sales_by_state.index[::-1],
    sales_by_state.values[::-1]
)

plt.title("Sales by State", fontsize=16)
plt.xlabel("Total Sales")
plt.ylabel("State")

# Display sales values beside the bars
plt.bar_label(bars, fmt="%.0f", padding=4)

plt.tight_layout()

plt.savefig(
    "data/sales_by_state.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()

print("Sales by State chart created successfully!")




# ============================================================
# 7. SALES BY PAYMENT METHOD
# ============================================================

sales_by_payment = (
    data.groupby("payment_method")["sales"]
    .sum()
    .sort_values(ascending=False)
)

plt.figure(figsize=(10, 6))

bars = plt.bar(
    sales_by_payment.index,
    sales_by_payment.values
)

plt.title("Sales by Payment Method", fontsize=16)
plt.xlabel("Payment Method")
plt.ylabel("Total Sales")

plt.xticks(rotation=30, ha="right")

# Display sales values above the bars
plt.bar_label(bars, fmt="%.0f", padding=4)

plt.tight_layout()

plt.savefig(
    "data/sales_by_payment_method.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()

print("Sales by Payment Method chart created successfully!")



# ============================================================
# 8. ORDER STATUS DISTRIBUTION
# ============================================================

order_status = data["order_status"].value_counts()

plt.figure(figsize=(9, 7))

plt.pie(
    order_status.values,
    labels=order_status.index,
    autopct="%1.1f%%",
    startangle=90
)

plt.title("Order Status Distribution", fontsize=16)

plt.tight_layout()

plt.savefig(
    "data/order_status_distribution.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()

print("Order Status Distribution chart created successfully!")


# ============================================================
# VISUALIZATION COMPLETED
# ============================================================

print("\n==========================================")
print("     ALL 8 CHARTS COMPLETED")
print("==========================================")

print("1. Monthly Sales Trend")
print("2. Monthly Profit Trend")
print("3. Sales by Category")
print("4. Profit by Category")
print("5. Top 10 Products by Sales")
print("6. Sales by State")
print("7. Sales by Payment Method")
print("8. Order Status Distribution")
# python python/08_visualization.py