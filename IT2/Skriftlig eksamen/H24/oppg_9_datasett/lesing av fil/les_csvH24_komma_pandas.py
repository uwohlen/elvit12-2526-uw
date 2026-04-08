import pandas as pd

filnavn = "Datasett_fodselstall_komma.csv"
kolonner = {'�r':'År', 'Levendef�dte i alt':'Levendefødte i alt'}
df = pd.read_csv(filnavn)
#newdf = df.rename(columns=kolonner)
print(df.columns)