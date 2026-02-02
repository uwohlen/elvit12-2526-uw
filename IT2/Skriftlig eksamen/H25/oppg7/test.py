import csv
import matplotlib.pyplot as plt

filnavn = "elever-fag.csv"

realfag = []
fagomraade = []

with open(filnavn, encoding="Windows-1252") as fil:
  filinnhold = csv.reader(fil, delimiter=",")
  overskrifter = next(filinnhold)
  for rad in filinnhold:
    if rad[0] == "Realfag":
      if rad[1] not in fagomraade:
        fagomraade.append(rad[1])
      rad[2] = rad[2].replace("studieforberedende utdanningsprogram","ST")
      rad[2] = rad[2].replace("påbygging til generell studiekompetanse","påbygg ST")
      rad[2] = rad[2].replace("påbygging til generell studiekompentanse","påbygg ST")
      rad[2] = rad[2].replace("i videregående opplæring ","")
      rad[2] = rad[2].replace("samisk plan","samisk")         
      realfag.append(rad)

aar = overskrifter[3:]

for rad in realfag:
  for i in range(3,len(overskrifter)):
    if rad[i] != '':
      rad[i] = rad[i].replace(" ","")
      rad[i] = int(rad[i])
    else:
      rad[i] = 0 # manglende verdier betyr 0 elever

tabell = []
for omraade in fagomraade:
  tabell.append([omraade,0,0,0])
  for rad in realfag:
    if rad[1] == omraade:
      tabell[-1][1] += rad[3]
      tabell[-1][2] += rad[4]
      tabell[-1][3] += rad[5]

print("Område                           ",end=" ")
print(overskrifter[3], end = "    ")
print(overskrifter[4], end = "    ")
print(overskrifter[5])

for rad in tabell:
  for i in range(len(rad)):
    if i == 0:
      print(f"{rad[i]:30}", end = " ")
    else:
      print(f"{rad[i]:10}", end = " ")
  print()

print()
svar = input("Velg fagområde (bruk forbokstaven): ")

print("Fag                              ",end=" ")
print(overskrifter[3], end = "    ")
print(overskrifter[4], end = "    ")
print(overskrifter[5])

valg = []

for rad in realfag:
  if rad[1][0] == svar.upper():
    for i in range(2,len(rad)):
      if i == 2:
        print(f"{rad[i]:30}", end = " ")
      else:
        print(f"{rad[i]:10}", end = " ")
    print()
    valg.append(rad)
  if rad[2] == "Matematikk 2P":
    _2p = rad[3:]
  if rad[2] == "Matematikk S1":
    s1 = rad[3:]
  if rad[2] == "Matematikk R1":
    r1 = rad[3:]
  

plt.plot(aar,_2p,label="2P")
plt.plot(aar,s1,label="S1")
plt.plot(aar,r1,label="R1")
plt.legend(title="Fag")
plt.ylim((0,22000))
plt.show()

for rad in realfag:
  rad.append(rad[5]-rad[3])
  if rad[3] != 0:
    rad.append(round(rad[6]/rad[3]*100))
  else:
    rad.append(0) # siden vi skal ha størst verdi, så vil 0 ikke påvirke utfallet

endring = sorted(realfag,key=lambda rad:rad[6])
prosent = sorted(realfag,key=lambda rad:rad[7])
resultater = [endring[-1],prosent[-1],endring[0],prosent[0]]
titler = ["absolutt oppgang  ","prosentvis oppgang","absolutt nedgang  ","prosentvis nedgang"]

print()
for j in range(len(resultater)):
  print(f"Fag med størst {titler[j]}",end=" ")
  print(overskrifter[3], end = "    ")
  print(overskrifter[4], end = "    ")
  print(overskrifter[5], end = "    ")
  print("Endring", end = "    ")
  print("Prosent")

  for i in range(2,len(resultater[j])):
    if i == 2:
      print(f"{resultater[j][i]:30}", end = " ")
    else:
      print(f"{resultater[j][i]:10}", end = " ")
  print()
  print()
