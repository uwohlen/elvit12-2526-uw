import csv

filnavn = "05994_20240126-145813-csv.csv"

alt = []

#with open(filnavn,encoding="ansi") as fil: # Virker også med ANSI, som Notisblokk foreslår.
with open(filnavn,encoding="Windows-1252") as fil:
  next(fil) # Fjerner innledende tekst
  next(fil) # Fjerner tom linje
  resten = csv.DictReader(fil,delimiter=";")

  for linje in resten:
    alt.append(linje)

# Har fått en liste med ordbøker:
for rad in alt:
  for nokkel,verdi in rad.items():
    if nokkel == "kjønn": # ø har blitt lest ok
      print(nokkel,verdi)

