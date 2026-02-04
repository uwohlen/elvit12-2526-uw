import json

filnavn = "Elever-fag.json"

with open(filnavn, encoding="Windows-1252") as fil:
  data = json.load(fil)

print(data)


for info in data:
  for key,value in info.items():
    print(key, " : ", value)



