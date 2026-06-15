import pandas as pd

df = pd.read_csv("8.2.csv")
print(df)

print(df[df["Name"] == "xyz"])
