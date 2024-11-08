#It important to use proper data types for two main reasons: 
# 1. Data Structures of data data take a different amount of memory space. Having proper data types save is from wasting memory
# Some methods and functions can also be used with certain data types.

import pandas as pd

sales = pd.read_csv("sales.csv")

print(sales.dtypes)

print("As index: ")
print(sales.columns)

print("As list: ")
print(list(sales.columns))
