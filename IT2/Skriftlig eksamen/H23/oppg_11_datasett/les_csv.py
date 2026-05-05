import csv
import matplotlib.pyplot as plt

filnavn = "Global YouTube Statistics.csv"

alt = []

with open(filnavn,encoding="ISO-8859-9") as fil:
  hele_filen = csv.reader(fil,delimiter=",")
  overskrifter = next(hele_filen)

  for linje in hele_filen:
    alt.append(linje)

print(overskrifter)
print(alt[6])
