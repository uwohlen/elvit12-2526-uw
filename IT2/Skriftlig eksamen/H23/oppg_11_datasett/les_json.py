import json

filnavn = "Global YouTube Statistics.json"

with open(filnavn, encoding="utf-8") as fil:
  data = json.load(fil)

#print(data[6])

for key,value in data[6].items():
  print(key, value)



