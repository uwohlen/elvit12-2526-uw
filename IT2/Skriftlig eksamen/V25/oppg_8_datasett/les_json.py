import json

filnavn = "friluftsaktiviteter.json"

with open(filnavn, encoding="utf-8") as fil:
  data = json.load(fil)

#print(data)

sammen = []

# Setter sammen linjer som har blitt delt pga. komma-tegn i teksten
for info in data:
  sammen.append({"deltatt":""})
  for key,value in info.items():
    #print(key, " : ", value)
    if sammen[-1]["deltatt"] == "":
      sammen[-1]["deltatt"] += value
    else:
      sammen[-1]["deltatt"] += "," + value
  #print(sammen[-1])

sammen.pop(0)
keys = sammen.pop(0)

keys["deltatt"] = keys["deltatt"].split(";")

for i in range(1,len(keys["deltatt"])):
  keys["deltatt"][i] = keys["deltatt"][i][24:-1]
  if keys["deltatt"][i].count("-") > 0:
    plass = keys["deltatt"][i].index("-")
    keys["deltatt"][i] = keys["deltatt"][i][:plass-1]

keys["deltatt"][0] = keys["deltatt"][0][1:-1]
#print(keys)

for i in range(len(sammen)):
  sammen[i]["deltatt"] = sammen[i]["deltatt"].split(";")
  for j in range(len(keys["deltatt"])):
    if j == 0:
      sammen[i][keys["deltatt"][j]] = sammen[i]["deltatt"][j][1:-1]
    else:
      sammen[i][keys["deltatt"][j]] = int(sammen[i]["deltatt"][j])
  sammen[i].pop("deltatt")


# Bare for å se hva jeg har:
for info in sammen:
  for key,value in info.items():
    print(key, " : ", value)
    #pass