import json

filnavn = "Elever-fag.json"

with open(filnavn, encoding="Windows-1252") as fil:
  data = json.load(fil)

print(data)

# Det går ikke an å oversette, fordi æ, ø og å har samme verdi "\u00ef\u00bf\u00bd" i datasettet

for info in data:
  for key,value in info.items():
    print(key, " : ", value)



