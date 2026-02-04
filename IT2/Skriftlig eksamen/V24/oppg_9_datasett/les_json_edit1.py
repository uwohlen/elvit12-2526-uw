import json


filnavn = "05994_20240126-145813-json_edit1.json"


with open(filnavn, encoding="Windows 1252") as fil:
  next(fil)
  next(fil)
  data = json.load(fil)

print(data)

for info in data:
  for key,value in info.items():
    print(key, " : ", value)
