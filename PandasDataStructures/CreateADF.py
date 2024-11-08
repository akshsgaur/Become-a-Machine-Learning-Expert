import pandas as pd
import numpy as np
#We can pass a dictionary to the DataFrame Constructor

df = pd.DataFrame(
    {
        "Names": ["Jane", "John", "Matt", "Ashley"], 
        "Ages": [26,24,28,25], 
        "Score": [91.2, 94.1, 89.5, 92.3]

    }

)

print(df)

arr = np.random.randint(1,10, size=(3,5))
df = pd.DataFrame(arr, columns=["A", "B", "C", "D", "E"])

print(df)

