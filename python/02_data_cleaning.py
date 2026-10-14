import pandas as pd
import numpy as np

customers = pd.read_csv("data/customers.csv")
products = pd.read_csv("data/products.csv")
orders = pd.read_csv("data/orders.csv")
order_items = pd.read_csv("data/order_items.csv")

customers_clean = customers.copy()
products_clean = products.copy()
orders_clean = orders.copy()
order_items_clean = order_items.copy()


print(customers_clean.isnull().sum())

print(products_clean.isnull().sum())
print(orders_clean.isnull().sum())
print(order_items_clean.isnull().sum())


print(customers_clean.isnull().sum().sum())


missing_percentage = (
    customers_clean.isnull().sum()
    / len(customers_clean)
) * 100

print(missing_percentage)




print(
    "Customer duplicates:",
    customers_clean.duplicated().sum()
)




print(
    "Product duplicates:",
    products_clean.duplicated().sum()
)

print(
    "Order duplicates:",
    orders_clean.duplicated().sum()
)

print(
    "Order item duplicates:",
    order_items_clean.duplicated().sum()
)


duplicates = customers_clean[
    customers_clean.duplicated()
]

print(duplicates)



customers_clean = customers_clean.drop_duplicates()
products_clean = products_clean.drop_duplicates()
orders_clean = orders_clean.drop_duplicates()
order_items_clean = order_items_clean.drop_duplicates()



customers_clean["signup_date"] = pd.to_datetime(
    customers_clean["signup_date"]
)





orders_clean["order_date"] = pd.to_datetime(
    orders_clean["order_date"]
)


print(customers_clean["signup_date"].dtype)
print(orders_clean["order_date"].dtype)



print(products_clean["price"].describe())

print(products_clean["cost_price"].describe())

print(order_items_clean["quantity"].describe())

print(order_items_clean["discount"].describe())

print(customers_clean["age"].describe())

print(
    customers_clean[
        (customers_clean["age"] < 0) |
        (customers_clean["age"] > 100)
    ]
)
invalid_prices = products_clean[
    products_clean["price"] <= 0
]

print(invalid_prices)

invalid_products = products_clean[
    products_clean["cost_price"] > products_clean["price"]
]

print(invalid_products)

invalid_quantity = order_items_clean[
    order_items_clean["quantity"] <= 0
]

print(invalid_quantity)

invalid_discount = order_items_clean[
    (order_items_clean["discount"] < 0) |
    (order_items_clean["discount"] > 1)
]

print(invalid_discount)

print(customers_clean["gender"].unique())


print(orders_clean["payment_method"].unique())
print(orders_clean["order_status"].unique())

print(products_clean["category"].unique())

print(
    products_clean["category"].value_counts()
)

print(
    orders_clean["order_status"].value_counts()
)
print(
    orders_clean["payment_method"].value_counts()
)

customers_clean["gender"] = (
    customers_clean["gender"]
    .str.strip()
    .str.title()
)

customers_clean["city"] = (
    customers_clean["city"]
    .str.strip()
    .str.title()
)

customers_clean["state"] = (
    customers_clean["state"]
    .str.strip()
    .str.title()
)

products_clean["product_name"]
products_clean["category"]
products_clean["subcategory"]
products_clean["brand"]

products_clean["brand"] = (
    products_clean["brand"]
    .str.strip()
    .str.title()
)

print(
    customers_clean["customer_id"].is_unique
)

print(
    products_clean["product_id"].is_unique
)


print(
    orders_clean["order_id"].is_unique
)


invalid_customer_ids = orders_clean[
    ~orders_clean["customer_id"].isin(
        customers_clean["customer_id"]
    )
]

print(invalid_customer_ids)



invalid_product_ids = order_items_clean[
    ~order_items_clean["product_id"].isin(
        products_clean["product_id"]
    )
]

print(invalid_product_ids)

invalid_order_ids = order_items_clean[
    ~order_items_clean["order_id"].isin(
        orders_clean["order_id"]
    )
]

print(invalid_order_ids)

Q1 = products_clean["price"].quantile(0.25)
Q3 = products_clean["price"].quantile(0.75)

IQR = Q3 - Q1

lower_limit = Q1 - 1.5 * IQR
upper_limit = Q3 + 1.5 * IQR

price_outliers = products_clean[
    (products_clean["price"] < lower_limit) |
    (products_clean["price"] > upper_limit)
]

print(price_outliers)

