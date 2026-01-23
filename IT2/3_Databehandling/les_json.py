import json

filnavn = "kvadrater.json"

with open(filnavn, encoding="utf-8") as fil:
  data = json.load(fil)

print(data)

for info in data:
  for key,value in info.items():
    print(key, value)



