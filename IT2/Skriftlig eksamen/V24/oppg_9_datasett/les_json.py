import json


filnavn = "05994_20240126-145813-json.json"


with open(filnavn, encoding="Windows 1252") as fil:
  next(fil)
  next(fil)
  data = json.load(fil)

print(data)

for info in data:
  for key,value in info.items():
    print(key, " : ", value)

# programmet feiler pga. et tegn i json-filen som ikke er riktig kodet
