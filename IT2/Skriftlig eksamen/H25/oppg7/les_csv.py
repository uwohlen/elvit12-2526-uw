import csv
filnavn = "Elever-fag.csv"

alt = []

with open(filnavn,encoding="Windows-1252") as fil:
  hele_filen = csv.reader(fil,delimiter=",")
  overskrifter = next(hele_filen)

  for linje in hele_filen:
    alt.append(linje)

"""
# Det går ikke an å oversette, fordi æ, ø og å har samme verdi "ï¿½" i datasettet
for i in range(len(alt)):
  for j in range(len(alt[i])):
    alt[i][j] = alt[i][j].replace("ï¿½","å")
"""


print(overskrifter)
print(alt)
