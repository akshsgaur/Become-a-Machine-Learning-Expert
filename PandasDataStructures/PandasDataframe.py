import pandas as pd

#DataFrame => Two Dimensional data structure of Pandas. It consists of labeled rows and columns. 

df = pd.DataFrame({

    "Name": ["Jane", "John", "Matt", "Ashley"],
    "Age": [24,21, 26, 32]

})

print(df)
print(df.shape)