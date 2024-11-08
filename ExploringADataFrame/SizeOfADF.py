import pandas as pd

sales = pd.read_csv('sales.csv')

print(sales.shape)
print(sales.size)
print(len(sales))