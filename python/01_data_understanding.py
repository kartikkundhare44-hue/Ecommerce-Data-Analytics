# import pandas as pd

# customers = pd.read_csv("data/customers.csv")

# print(customers.head())



import pandas as pd

customers = pd.read_csv("data/customers.csv")
products = pd.read_csv("data/products.csv")
orders = pd.read_csv("data/orders.csv")
order_items = pd.read_csv("data/order_items.csv")

print("Customers")
print(customers.head())

print("\nProducts")
print(products.head())

print("\nOrders")
print(orders.head())

print("\nOrder Items")
print(order_items.head())









print("Customers:", customers.shape)
print("Products:", products.shape)
print("Orders:", orders.shape)
print("Order Items:", order_items.shape)

print(customers.columns)

print(products.columns)
print(orders.columns)
print(order_items.columns)


print(customers.dtypes)




print(customers.isnull().sum())
print(customers.isnull().sum())
print(products.isnull().sum())
print(orders.isnull().sum())
print(order_items.isnull().sum())



print(customers.duplicated().sum())
print(products.duplicated().sum())
print(orders.duplicated().sum())
print(order_items.duplicated().sum())