import json

filnavn = "friluftsaktiviteter.json"

with open(filnavn, encoding="utf-8") as fil:
  data = json.load(fil)

#print(data)

sammen = []

for info in data:
  sammen.append({"deltatt":""})
  for key,value in info.items():
    #print(key, " : ", value)
    if sammen[-1]["deltatt"] == "":
      sammen[-1]["deltatt"] += value
    else:
      sammen[-1]["deltatt"] += "," + value
  print(sammen[-1])


