import pandas as pd

filnavn = "Datasett_fodselstall.csv"

df = pd.read_csv(filnavn,encoding="ansi",delimiter="\t")

print(df.columns)