import pandas as pd

# ============================================================
# DAY 3 - DATA VALIDATION
# ============================================================

print("==========================================")
print("          DATA VALIDATION")
print("==========================================")


# 1. LOAD FINAL DATASET

data = pd.read_csv(
    "data/ecommerce_analysis_ready.csv"
)

print("\nDataset loaded successfully!")


# 2. DATASET SIZE

print("\nDATASET SIZE")
print("------------------------------------------")

print("Rows:", data.shape[0])
print("Columns:", data.shape[1])


# 3. COLUMN NAMES

print("\nCOLUMN NAMES")
print("------------------------------------------")

print(data.columns.tolist())


# 4. MISSING VALUES

print("\nMISSING VALUES")
print("------------------------------------------")

print(data.isnull().sum())


# 5. DUPLICATES

print("\nDUPLICATES")
print("------------------------------------------")

print(
    "Duplicate rows:",
    data.duplicated().sum()
)


# 6. SALES CHECK

print("\nSALES CHECK")
print("------------------------------------------")

print("Minimum Sales:", data["sales"].min())
print("Maximum Sales:", data["sales"].max())
print("Total Sales:", data["sales"].sum())


# 7. COST CHECK

print("\nCOST CHECK")
print("------------------------------------------")

print("Minimum Cost:", data["cost"].min())
print("Maximum Cost:", data["cost"].max())
print("Total Cost:", data["cost"].sum())


# 8. PROFIT CHECK

print("\nPROFIT CHECK")
print("------------------------------------------")

print("Minimum Profit:", data["profit"].min())
print("Maximum Profit:", data["profit"].max())
print("Total Profit:", data["profit"].sum())


# 9. QUANTITY CHECK

print("\nQUANTITY CHECK")
print("------------------------------------------")

print("Minimum Quantity:", data["quantity"].min())
print("Maximum Quantity:", data["quantity"].max())
print("Total Quantity:", data["quantity"].sum())


# 10. ORDER STATUS

print("\nORDER STATUS")
print("------------------------------------------")

print(data["order_status"].value_counts())


# 11. PAYMENT METHOD

print("\nPAYMENT METHOD")
print("------------------------------------------")

print(data["payment_method"].value_counts())


# 12. PRODUCT CATEGORY

print("\nPRODUCT CATEGORY")
print("------------------------------------------")

print(data["category"].value_counts())


# 13. CUSTOMER GENDER

print("\nCUSTOMER GENDER")
print("------------------------------------------")

print(data["gender"].value_counts())


# 14. ORDER DATE RANGE

print("\nORDER DATE RANGE")
print("------------------------------------------")

print("First Order Date:", data["order_date"].min())
print("Last Order Date:", data["order_date"].max())


# 15. UNIQUE COUNTS

print("\nUNIQUE COUNTS")
print("------------------------------------------")

print("Customers:", data["customer_id"].nunique())
print("Orders:", data["order_id"].nunique())
print("Products:", data["product_id"].nunique())
print("Order Items:", data["order_item_id"].nunique())


# 16. PROFIT CALCULATION CHECK

print("\nPROFIT CALCULATION CHECK")
print("------------------------------------------")

calculated_profit = data["sales"] - data["cost"]

difference = (
    calculated_profit - data["profit"]
).abs().sum()

print(
    "Profit calculation difference:",
    difference
)


# 17. SAMPLE DATA

print("\nSAMPLE DATA")
print("------------------------------------------")

print(
    data[
        [
            "order_id",
            "order_date",
            "customer_id",
            "product_id",
            "quantity",
            "discount",
            "sales",
            "cost",
            "profit"
        ]
    ].head(10)
)


# FINAL

print("\n==========================================")
print("       VALIDATION COMPLETED")
print("==========================================")