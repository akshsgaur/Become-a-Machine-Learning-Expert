import pandas as pd

myseries = pd.Series([10,20,30])

print(myseries)


myseries = pd.Series(
    [10,20,30], 
    index = ["a", "b", "c"]

)

print(myseries)

myseries = pd.Series(
    ["Jane", "John", "Emily", "Matt"]
)

print(myseries[0])

#Any Duplicate items in a series => True
myseries = pd.Series([1,2,3])
print(myseries.is_unique)

#Any Non-Duplicate items in a series => False
myseries = pd.Series([1,2,3])
print(myseries.is_unique)

