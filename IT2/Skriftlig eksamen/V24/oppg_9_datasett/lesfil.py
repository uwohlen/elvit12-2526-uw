import csv
import matplotlib.pyplot as plt
import numpy as np

filnavn = "05994_20240126-145813-csv.csv"

# legger hele datasettet inn i lista innhold for videre programmering
# og kolonnenavnene inn i lista overskrifter for å ta en kikk
innhold = []
with open(filnavn, encoding="Windows-1252") as fil:
  filinnhold = csv.reader(fil, delimiter=";")
  tekst = next(filinnhold)
  #print(tekst)
  tekst2 = next(filinnhold)
  #print(tekst2)
  overskrifter = next(filinnhold)
  #print(overskrifter)

  for rad in filinnhold:
    #print(rad)
    innhold.append(rad)


desimaltall = []
hovedkategorier = []

for i in range(len(innhold)):
    innhold[i][2] = float(innhold[i][2])
    heltall = np.floor(innhold[i][2])
    desimaltall.append(round(innhold[i][2] - heltall,2))
    innhold[i].append(float(heltall)+float(desimaltall[i]*100)/60)
    #print(innhold[i])
    if innhold[i][0][0] != "¬":
       hovedkategorier.append(innhold[i])

desimaltall.sort()
#print(desimaltall)

#print(hovedkategorier)

kategorier = []
alle = []
menn = []
kvinner = []

for i in range(len(hovedkategorier)):
  if hovedkategorier[i][0] != "I alt":
    if hovedkategorier[i][1] == "Alle":
      kategorier.append(hovedkategorier[i][0])
      alle.append(hovedkategorier[i][3])
    elif hovedkategorier[i][1] == "Menn":
      menn.append(hovedkategorier[i][3])
    else:
      kvinner.append(hovedkategorier[i][3])
   
print(kategorier)
print(alle)

plt.barh(kategorier,alle)  
#plt.barh(kategorier,menn)
#plt.barh(kategorier,kvinner)
plt.show()
