import pandas as pd

# ============================================================
# DAY 3 - TIME SERIES ANALYSIS
# ============================================================

print("==========================================")
print("         TIME SERIES ANALYSIS")
print("==========================================")

# Load dataset
data = pd.read_csv("data/ecommerce_analysis_ready.csv")

# Convert order date
data["order_date"] = pd.to_datetime(data["order_date"])


# ------------------------------------------------------------
# 1. MONTHLY SALES
# ------------------------------------------------------------

monthly_sales = (
    data.groupby(
        ["year", "month", "month_name"]
    )["sales"]
    .sum()
    .reset_index()
    .sort_values(["year", "month"])
)

print("\nMONTHLY SALES")
print("------------------------------------------")
print(monthly_sales)


# ------------------------------------------------------------
# 2. MONTHLY PROFIT
# ------------------------------------------------------------

monthly_profit = (
    data.groupby(
        ["year", "month", "month_name"]
    )["profit"]
    .sum()
    .reset_index()
    .sort_values(["year", "month"])
)

print("\nMONTHLY PROFIT")
print("------------------------------------------")
print(monthly_profit)


# ------------------------------------------------------------
# 3. YEARLY SALES
# ------------------------------------------------------------

yearly_sales = (
    data.groupby("year")["sales"]
    .sum()
    .sort_values(ascending=False)
)

print("\nYEARLY SALES")
print("------------------------------------------")
print(yearly_sales)


# ------------------------------------------------------------
# 4. YEARLY PROFIT
# ------------------------------------------------------------

yearly_profit = (
    data.groupby("year")["profit"]
    .sum()
    .sort_values(ascending=False)
)

print("\nYEARLY PROFIT")
print("------------------------------------------")
print(yearly_profit)


# ------------------------------------------------------------
# 5. BEST SALES MONTH
# ------------------------------------------------------------

best_sales_month = monthly_sales.loc[
    monthly_sales["sales"].idxmax()
]

print("\nBEST SALES MONTH")
print("------------------------------------------")
print(
    best_sales_month[
        ["year", "month_name", "sales"]
    ]
)


# ------------------------------------------------------------
# 6. WORST SALES MONTH
# ------------------------------------------------------------

worst_sales_month = monthly_sales.loc[
    monthly_sales["sales"].idxmin()
]

print("\nWORST SALES MONTH")
print("------------------------------------------")
print(
    worst_sales_month[
        ["year", "month_name", "sales"]
    ]
)


# ------------------------------------------------------------
# 7. BEST PROFIT MONTH
# ------------------------------------------------------------

best_profit_month = monthly_profit.loc[
    monthly_profit["profit"].idxmax()
]

print("\nBEST PROFIT MONTH")
print("------------------------------------------")
print(
    best_profit_month[
        ["year", "month_name", "profit"]
    ]
)


# ------------------------------------------------------------
# 8. WORST PROFIT MONTH
# ------------------------------------------------------------

worst_profit_month = monthly_profit.loc[
    monthly_profit["profit"].idxmin()
]

print("\nWORST PROFIT MONTH")
print("------------------------------------------")
print(
    worst_profit_month[
        ["year", "month_name", "profit"]
    ]
)


# ------------------------------------------------------------
# 9. MONTHLY ORDER COUNT
# ------------------------------------------------------------

monthly_orders = (
    data.groupby(
        ["year", "month", "month_name"]
    )["order_id"]
    .nunique()
    .reset_index(name="orders")
    .sort_values(["year", "month"])
)

print("\nMONTHLY ORDERS")
print("------------------------------------------")
print(monthly_orders)


# ------------------------------------------------------------
# 10. SAVE FILES
# ------------------------------------------------------------

monthly_sales.to_csv(
    "data/monthly_sales.csv",
    index=False
)

monthly_profit.to_csv(
    "data/monthly_profit.csv",
    index=False
)

yearly_sales.to_csv(
    "data/yearly_sales.csv"
)

yearly_profit.to_csv(
    "data/yearly_profit.csv"
)

monthly_orders.to_csv(
    "data/monthly_orders.csv",
    index=False
)


print("\n==========================================")
print("       TIME SERIES ANALYSIS COMPLETED")
print("==========================================")

print("Analysis files saved successfully.")
