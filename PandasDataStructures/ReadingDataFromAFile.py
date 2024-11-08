import pandas as pd

#read_csv, read_json, read_parquet, read_excel

sales = pd.read_csv('sales.csv')

print(sales.head())

#Read only some of the columns from the csv file

sales = pd.read_csv("sales.csv", usecols=["product_code", "product_group", "stock_qty"], nrows = 1000)

print(sales)