import json


filnavn = "05994_20240126-145813-json.json"


with open(filnavn, encoding="cp1250") as fil:
  next(fil)
  next(fil)
  data = json.load(fil)

print(data)

for info in data:
  for key,value in info.items():
    print(key, " : ", value)

# encoding "Windows 1250" : programmet feiler pga. et tegn i json-filen som ikke er riktig kodet
# encoding cp1250 : programmet virker, men æøå og ¬ er ikke riktig kodet