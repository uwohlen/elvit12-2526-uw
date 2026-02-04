import json

filnavn = "Datasett_fodselstall.json"

with open(filnavn, encoding="utf-8") as fil:
  data = json.load(fil)

#print(data)

for key,value in data.items():
  print(key, " : ", value)



