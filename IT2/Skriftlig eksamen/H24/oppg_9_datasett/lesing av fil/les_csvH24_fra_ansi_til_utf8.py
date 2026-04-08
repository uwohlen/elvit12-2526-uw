import csv
filnavn = "test_fra_ansi_til_utf8.csv"
alt = []

with open(filnavn,encoding="utf-8-sig") as fil:
  hele_filen = csv.reader(fil,delimiter=";")
  overskrifter = next(hele_filen)

  for linje in hele_filen:
    alt.append(linje)

print(overskrifter)
#print(alt)
