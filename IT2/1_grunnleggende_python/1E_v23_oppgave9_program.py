import datasettV23 as ds

# Først: gjør meg litt kjent med datasettet
print(len(ds.appdata))

nokler = []

for key in ds.appdata[0].keys():
  nokler.append(key)
  
print(nokler)

kategorier = []
antall = []
rating = []
antall_rating = []

for app in ds.appdata:
  if app["Category"] not in kategorier and app["Category"] != "1.9":
    kategorier.append(app["Category"])
    antall.append(0)
    rating.append(0)
    antall_rating.append(0)

print(kategorier)

for app in ds.appdata:
  if app["Category"] != "1.9":
    indeks = kategorier.index(app["Category"])
    antall[indeks] += 1
    if app["Rating"] != "NaN":
      rating[indeks] += float(app["Rating"])
      antall_rating[indeks] += 1

print(antall)

alt = []

for i in range(len(kategorier)):
  alt.append([kategorier[i],antall[i],round(rating[i],3),antall_rating[i],round(rating[i]/antall_rating[i],3)])

alt.sort(key=lambda rad:rad[1], reverse=True)

print(alt[:3])

