import csv
filnavn = "Datasett_fodselstall.csv"
alt = []

with open(filnavn,encoding="ansi") as fil:
  hele_filen = csv.reader(fil,delimiter="\t")
  overskrifter = next(hele_filen)

  for linje in hele_filen:
    alt.append(linje)

print(overskrifter)
#print(alt)
