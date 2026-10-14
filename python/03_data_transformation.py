import pandas as pd

# ============================================================
# DAY 3 - DATA TRANSFORMATION & TABLE MERGING
# ============================================================

print("==========================================")
print("   DAY 3 - DATA TRANSFORMATION")
print("==========================================")


# ============================================================
# 1. LOAD DATA
# ============================================================

customers = pd.read_csv("data/customers.csv")
products = pd.read_csv("data/products.csv")
orders = pd.read_csv("data/orders.csv")
order_items = pd.read_csv("data/order_items.csv")


print("\nDATA LOADED SUCCESSFULLY")
print("------------------------------------------")

print("Customers shape:", customers.shape)
print("Products shape:", products.shape)
print("Orders shape:", orders.shape)
print("Order Items shape:", order_items.shape)


# ============================================================
# 2. CONVERT DATE COLUMNS
# ============================================================

customers["signup_date"] = pd.to_datetime(
    customers["signup_date"]
)

orders["order_date"] = pd.to_datetime(
    orders["order_date"]
)

print("\nDate columns converted successfully.")


# ============================================================
# 3. MERGE ORDER ITEMS WITH PRODUCTS
# ============================================================

order_product = pd.merge(
    order_items,
    products,
    on="product_id",
    how="left"
)

print("\nOrder Items + Products")
print("------------------------------------------")
print("Shape:", order_product.shape)


# ============================================================
# 4. CALCULATE GROSS SALES
# ============================================================

order_product["gross_sales"] = (
    order_product["price"]
    * order_product["quantity"]
)


# ============================================================
# 5. CALCULATE DISCOUNT AMOUNT
# ============================================================

order_product["discount_amount"] = (
    order_product["gross_sales"]
    * order_product["discount"]
)


# ============================================================
# 6. CALCULATE NET SALES
# ============================================================

order_product["sales"] = (
    order_product["gross_sales"]
    - order_product["discount_amount"]
)


# ============================================================
# 7. CALCULATE COST
# ============================================================

order_product["cost"] = (
    order_product["cost_price"]
    * order_product["quantity"]
)


# ============================================================
# 8. CALCULATE PROFIT
# ============================================================

order_product["profit"] = (
    order_product["sales"]
    - order_product["cost"]
)


print("\nSales, Cost and Profit calculated successfully.")


# ============================================================
# 9. MERGE WITH ORDERS
# ============================================================

orders_full = pd.merge(
    order_product,
    orders,
    on="order_id",
    how="left"
)

print("\nOrder Items + Products + Orders")
print("------------------------------------------")
print("Shape:", orders_full.shape)


# ============================================================
# 10. MERGE WITH CUSTOMERS
# ============================================================

final_data = pd.merge(
    orders_full,
    customers,
    on="customer_id",
    how="left"
)

print("\nFINAL MERGE")
print("------------------------------------------")
print("Shape:", final_data.shape)


# ============================================================
# 11. CREATE DATE FEATURES
# ============================================================

final_data["year"] = (
    final_data["order_date"].dt.year
)

final_data["month"] = (
    final_data["order_date"].dt.month
)

final_data["month_name"] = (
    final_data["order_date"].dt.month_name()
)


print("\nDate features created successfully.")


# ============================================================
# 12. CHECK MISSING VALUES
# ============================================================

print("\nMISSING VALUES")
print("------------------------------------------")

print(final_data.isnull().sum())


# ============================================================
# 13. CHECK DUPLICATES
# ============================================================

print("\nDUPLICATE ROWS")
print("------------------------------------------")

print(
    "Duplicate rows:",
    final_data.duplicated().sum()
)


# ============================================================
# 14. DISPLAY FINAL COLUMNS
# ============================================================

print("\nFINAL DATASET COLUMNS")
print("------------------------------------------")

print(final_data.columns.tolist())


# ============================================================
# 15. DISPLAY FIRST 5 ROWS
# ============================================================

print("\nFIRST 5 ROWS")
print("------------------------------------------")

print(final_data.head())


# ============================================================
# 16. BUSINESS SUMMARY
# ============================================================

print("\n==========================================")
print("          BUSINESS SUMMARY")
print("==========================================")

print(
    "Total Sales:",
    round(final_data["sales"].sum(), 2)
)

print(
    "Total Cost:",
    round(final_data["cost"].sum(), 2)
)

print(
    "Total Profit:",
    round(final_data["profit"].sum(), 2)
)

print(
    "Total Quantity:",
    final_data["quantity"].sum()
)

print(
    "Total Order Items:",
    final_data["order_item_id"].nunique()
)

print(
    "Total Orders:",
    final_data["order_id"].nunique()
)

print(
    "Total Customers:",
    final_data["customer_id"].nunique()
)


# ============================================================
# 17. SAVE FINAL DATASET
# ============================================================

final_data.to_csv(
    "data/ecommerce_analysis_ready.csv",
    index=False
)

print("\n==========================================")
print("       TRANSFORMATION COMPLETED")
print("==========================================")

print(
    "Final dataset saved successfully!"
)

print(
    "File: data/ecommerce_analysis_ready.csv"
)