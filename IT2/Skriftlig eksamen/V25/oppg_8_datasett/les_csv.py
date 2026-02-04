import csv

filnavn = "friluftsaktiviteter.csv"

alt = []

with open(filnavn,encoding="utf-8") as fil:
  hele_filen = csv.reader(fil,delimiter=";")
  overskrifter = next(hele_filen)

  for linje in hele_filen:
    alt.append(linje)


for i in range(len(alt)):
  for j in range(1,len(alt[i])):
    alt[i][j] = int(alt[i][j])
    
print(overskrifter)
print(alt)