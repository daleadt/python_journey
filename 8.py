# pandas custom index

import pandas as pd

a = pd.Series([1, 2, 3, 4], index=["A", "B", "C", "D"])
print(a)
print(a["B"])
