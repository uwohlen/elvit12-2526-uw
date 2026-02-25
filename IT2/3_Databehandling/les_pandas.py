import pandas as pd

filnavn = "test.csv"

df = pd.read_csv(filnavn)

#print(df.columns)
print(df)

filnavn2 = "kvadrater_utf8.csv"

df2 = pd.read_csv(filnavn2,delimiter=";")

#print(df2.columns)
print(df2)