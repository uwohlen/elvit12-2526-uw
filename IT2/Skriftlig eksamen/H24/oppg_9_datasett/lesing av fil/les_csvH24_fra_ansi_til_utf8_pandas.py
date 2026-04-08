import pandas as pd

filnavn = "test_fra_ansi_til_utf8.csv"

df = pd.read_csv(filnavn, delimiter=";")

print(df.columns)