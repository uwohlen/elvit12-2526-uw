import csv
filnavn = "Datasett_fodselstall_komma.csv"

alt = []

with open(filnavn,encoding="utf-8") as fil:
  hele_filen = csv.reader(fil,delimiter=",")
  overskrifter = next(hele_filen)

  for linje in hele_filen:
    alt.append(linje)

print(overskrifter)
print(alt)
