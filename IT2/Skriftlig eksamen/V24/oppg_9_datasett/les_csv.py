import csv

filnavn = "05994_20240126-145813-csv.csv"

alt = []

with open(filnavn,encoding="Windows-1252") as fil:
  hele_filen = csv.reader(fil,delimiter=";")
  tekst = next(hele_filen)
  tom = next(hele_filen)
  overskrifter = next(hele_filen)

  for linje in hele_filen:
    alt.append(linje)

for i in range(len(alt)):
  if alt[i][0] == "I alt":
    alt[i].append(0)
  elif alt[i][0][0:1] == "¬":
    alt[i].append(2)
  else:
    alt[i].append(1)
  print(alt[i])

print(overskrifter)
#print(alt)