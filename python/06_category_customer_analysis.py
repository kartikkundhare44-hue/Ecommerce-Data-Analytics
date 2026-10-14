import pandas as pd

# ============================================================
# DAY 3 - CATEGORY & CUSTOMER ANALYSIS
# ============================================================

print("==========================================")
print("    CATEGORY & CUSTOMER ANALYSIS")
print("==========================================")

# Load final dataset
data = pd.read_csv("data/ecommerce_analysis_ready.csv")


# ------------------------------------------------------------
# 1. CATEGORY PERFORMANCE
# ------------------------------------------------------------

category_analysis = (
    data.groupby("category")
    .agg(
        Sales=("sales", "sum"),
        Profit=("profit", "sum"),
        Quantity=("quantity", "sum"),
        Orders=("order_id", "nunique")
    )
    .sort_values("Sales", ascending=False)
)

print("\nCATEGORY PERFORMANCE")
print("------------------------------------------")
print(category_analysis)


# ------------------------------------------------------------
# 2. TOP 10 CUSTOMERS BY SALES
# ------------------------------------------------------------

customer_sales = (
    data.groupby("customer_id")
    .agg(
        Sales=("sales", "sum"),
        Profit=("profit", "sum"),
        Orders=("order_id", "nunique"),
        Quantity=("quantity", "sum")
    )
    .sort_values("Sales", ascending=False)
)

print("\nTOP 10 CUSTOMERS BY SALES")
print("------------------------------------------")
print(customer_sales.head(10))


# ------------------------------------------------------------
# 3. TOP 10 CUSTOMERS BY PROFIT
# ------------------------------------------------------------

top_customers_profit = (
    customer_sales
    .sort_values("Profit", ascending=False)
    .head(10)
)

print("\nTOP 10 CUSTOMERS BY PROFIT")
print("------------------------------------------")
print(top_customers_profit)


# ------------------------------------------------------------
# 4. STATE ANALYSIS
# ------------------------------------------------------------

state_analysis = (
    data.groupby("state")
    .agg(
        Sales=("sales", "sum"),
        Profit=("profit", "sum"),
        Orders=("order_id", "nunique"),
        Quantity=("quantity", "sum")
    )
    .sort_values("Sales", ascending=False)
)

print("\nSTATE PERFORMANCE")
print("------------------------------------------")
print(state_analysis)


# ------------------------------------------------------------
# 5. CITY ANALYSIS
# ------------------------------------------------------------

city_analysis = (
    data.groupby("city")
    .agg(
        Sales=("sales", "sum"),
        Profit=("profit", "sum"),
        Orders=("order_id", "nunique")
    )
    .sort_values("Sales", ascending=False)
)

print("\nTOP 10 CITIES BY SALES")
print("------------------------------------------")
print(city_analysis.head(10))


# ------------------------------------------------------------
# 6. PAYMENT METHOD ANALYSIS
# ------------------------------------------------------------

payment_analysis = (
    data.groupby("payment_method")
    .agg(
        Sales=("sales", "sum"),
        Profit=("profit", "sum"),
        Orders=("order_id", "nunique")
    )
    .sort_values("Sales", ascending=False)
)

print("\nPAYMENT METHOD PERFORMANCE")
print("------------------------------------------")
print(payment_analysis)


# ------------------------------------------------------------
# 7. ORDER STATUS ANALYSIS
# ------------------------------------------------------------

status_analysis = (
    data.groupby("order_status")
    .agg(
        Sales=("sales", "sum"),
        Profit=("profit", "sum"),
        Orders=("order_id", "nunique")
    )
    .sort_values("Orders", ascending=False)
)

print("\nORDER STATUS ANALYSIS")
print("------------------------------------------")
print(status_analysis)


# ------------------------------------------------------------
# 8. GENDER ANALYSIS
# ------------------------------------------------------------

gender_analysis = (
    data.groupby("gender")
    .agg(
        Sales=("sales", "sum"),
        Profit=("profit", "sum"),
        Orders=("order_id", "nunique"),
        Quantity=("quantity", "sum")
    )
    .sort_values("Sales", ascending=False)
)

print("\nCUSTOMER GENDER ANALYSIS")
print("------------------------------------------")
print(gender_analysis)


# ------------------------------------------------------------
# 9. SAVE ANALYSIS FILES
# ------------------------------------------------------------

category_analysis.to_csv(
    "data/category_analysis.csv"
)

customer_sales.to_csv(
    "data/customer_analysis.csv"
)

state_analysis.to_csv(
    "data/state_analysis.csv"
)

city_analysis.to_csv(
    "data/city_analysis.csv"
)

payment_analysis.to_csv(
    "data/payment_analysis.csv"
)

status_analysis.to_csv(
    "data/order_status_analysis.csv"
)

gender_analysis.to_csv(
    "data/gender_analysis.csv"
)


print("\n==========================================")
print("   CATEGORY & CUSTOMER ANALYSIS COMPLETED")
print("==========================================")

print("All analysis files saved successfully.")