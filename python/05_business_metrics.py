import pandas as pd

# ============================================================
# DAY 3 - BUSINESS METRICS
# ============================================================

data = pd.read_csv("data/ecommerce_analysis_ready.csv")

print("==========================================")
print("          BUSINESS METRICS")
print("==========================================")


# ------------------------------------------------------------
# 1. TOTAL SALES
# ------------------------------------------------------------

total_sales = data["sales"].sum()

print("\nTotal Sales:", round(total_sales, 2))


# ------------------------------------------------------------
# 2. TOTAL COST
# ------------------------------------------------------------

total_cost = data["cost"].sum()

print("Total Cost:", round(total_cost, 2))


# ------------------------------------------------------------
# 3. TOTAL PROFIT
# ------------------------------------------------------------

total_profit = data["profit"].sum()

print("Total Profit:", round(total_profit, 2))


# ------------------------------------------------------------
# 4. PROFIT MARGIN
# ------------------------------------------------------------

profit_margin = (
    total_profit / total_sales
) * 100

print(
    "Profit Margin:",
    round(profit_margin, 2),
    "%"
)


# ------------------------------------------------------------
# 5. TOTAL QUANTITY SOLD
# ------------------------------------------------------------

total_quantity = data["quantity"].sum()

print(
    "Total Quantity Sold:",
    total_quantity
)


# ------------------------------------------------------------
# 6. TOTAL ORDERS
# ------------------------------------------------------------

total_orders = data["order_id"].nunique()

print(
    "Total Orders:",
    total_orders
)


# ------------------------------------------------------------
# 7. TOTAL CUSTOMERS
# ------------------------------------------------------------

total_customers = data["customer_id"].nunique()

print(
    "Total Customers:",
    total_customers
)


# ------------------------------------------------------------
# 8. TOTAL PRODUCTS
# ------------------------------------------------------------

total_products = data["product_id"].nunique()

print(
    "Total Products:",
    total_products
)


# ------------------------------------------------------------
# 9. AVERAGE ORDER VALUE
# ------------------------------------------------------------

average_order_value = (
    total_sales / total_orders
)

print(
    "Average Order Value:",
    round(average_order_value, 2)
)


# ------------------------------------------------------------
# 10. SALES BY CATEGORY
# ------------------------------------------------------------

sales_by_category = (
    data.groupby("category")["sales"]
    .sum()
    .sort_values(ascending=False)
)

print("\n==========================================")
print("          SALES BY CATEGORY")
print("==========================================")

print(sales_by_category)


# ------------------------------------------------------------
# 11. PROFIT BY CATEGORY
# ------------------------------------------------------------

profit_by_category = (
    data.groupby("category")["profit"]
    .sum()
    .sort_values(ascending=False)
)

print("\n==========================================")
print("          PROFIT BY CATEGORY")
print("==========================================")

print(profit_by_category)


# ------------------------------------------------------------
# 12. SALES BY PAYMENT METHOD
# ------------------------------------------------------------

sales_by_payment = (
    data.groupby("payment_method")["sales"]
    .sum()
    .sort_values(ascending=False)
)

print("\n==========================================")
print("       SALES BY PAYMENT METHOD")
print("==========================================")

print(sales_by_payment)


# ------------------------------------------------------------
# 13. SALES BY ORDER STATUS
# ------------------------------------------------------------

sales_by_status = (
    data.groupby("order_status")["sales"]
    .sum()
    .sort_values(ascending=False)
)

print("\n==========================================")
print("        SALES BY ORDER STATUS")
print("==========================================")

print(sales_by_status)


# ------------------------------------------------------------
# 14. TOP 10 PRODUCTS
# ------------------------------------------------------------

top_products = (
    data.groupby("product_name")["sales"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

print("\n==========================================")
print("            TOP 10 PRODUCTS")
print("==========================================")

print(top_products)


# ------------------------------------------------------------
# 15. SALES BY STATE
# ------------------------------------------------------------

sales_by_state = (
    data.groupby("state")["sales"]
    .sum()
    .sort_values(ascending=False)
)

print("\n==========================================")
print("            SALES BY STATE")
print("==========================================")

print(sales_by_state)


# ------------------------------------------------------------
# 16. MONTHLY SALES
# ------------------------------------------------------------

monthly_sales = (
    data.groupby(
        ["year", "month", "month_name"]
    )["sales"]
    .sum()
    .reset_index()
    .sort_values(["year", "month"])
)

print("\n==========================================")
print("            MONTHLY SALES")
print("==========================================")

print(monthly_sales)


# ------------------------------------------------------------
# 17. SAVE ANALYSIS FILES
# ------------------------------------------------------------

sales_by_category.to_csv(
    "data/sales_by_category.csv"
)

profit_by_category.to_csv(
    "data/profit_by_category.csv"
)

top_products.to_csv(
    "data/top_10_products.csv"
)

sales_by_state.to_csv(
    "data/sales_by_state.csv"
)

monthly_sales.to_csv(
    "data/monthly_sales.csv",
    index=False
)


print("\n==========================================")
print("       BUSINESS ANALYSIS COMPLETED")
print("==========================================")

print("Analysis files saved in the data folder.")