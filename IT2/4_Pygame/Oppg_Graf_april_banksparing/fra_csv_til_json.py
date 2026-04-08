"""
CSV-filen ble lagd i excel, med "lagre som: CSV UTF-8 (kommadelt).csv"
Programmet under ble brukt for å lage en json-fil fra csv-filen.
"""
import csv

filnavn = "bank.csv"

# legger hele datasettet inn i lista innhold for videre programmering
# og kolonnenavnene inn i lista overskrifter for å ta en kikk
innhold = []
with open(filnavn, encoding="utf-8-sig") as fil:
    filinnhold = csv.reader(fil, delimiter=";")
    overskrifter = next(filinnhold)

    for rad in filinnhold:
        innhold.append(rad)

#print(overskrifter)
#print(innhold)

import json

tables = overskrifter
alt = []
teller = 0
for j in range(len(innhold)):
    data = {}
    for i in range(len(overskrifter)):
        data[overskrifter[i]] = innhold[j][i]
    alt.append(data)
    teller += 1

#print(teller)
with open("bank.json", "w", encoding="utf-8") as f:
    json.dump(alt, f)