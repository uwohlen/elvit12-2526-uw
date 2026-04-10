"""
En dårlig løsning, siden grafen inneholder summerings-kategorier, 
og dermed 72 timer istedenfor 24 timer
Se les_csv.py for en måte å gruppere dataene, 
eller lesfil.py / oppgave9.html for en måte å endre utvalget for grafen
"""

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
  #print(tekst) # info om filen, ikke data
  tekst2 = next(filinnhold)
  #print(tekst2) # tom linje, ikke data
  overskrifter = next(filinnhold)
  #print(overskrifter) # tar vare på overskrifter i tilfelle bruk, men de er ikke gode

  for rad in filinnhold:
    #print(rad) # data til bruk
    innhold.append(rad)


desimaltall = []
hovedkategorier = []

# Lager tabelloverskrifter
print("Nr Aktivitet                                  Kjønn     Tidsbruk");

# Leser data, omformer tidsbruk til tall, og skriver ut tabell
for i in range(len(innhold)):
    innhold[i][2] = float(innhold[i][2])
    heltall = np.floor(innhold[i][2])
    desimaltall.append(round(innhold[i][2] - heltall,2))
    innhold[i].append(float(heltall)+float(desimaltall[i]*100)/60)
    innhold[i].append(str(innhold[i][2]).replace(".",":"))
    if desimaltall[i] == 0:
       innhold[i][4] = innhold[i][4] + "0";
    print(f"{i+1:2.0f} {innhold[i][0]:42} {innhold[i][1]:13} {innhold[i][4]:5}")


desimaltall.sort()
#print(desimaltall) #sjekker for ugyldige verdier - alt ok i utvalg fra år 2000

# Lager tabell basert på kjønn
def tabell(kjonn):
  print()
  print("Tidsbruk for",kjonn)
  print()
  print("Nr Aktivitet                               Tidsbruk");
  t = 1
  total = 0
  for i in range(len(innhold)):
    if innhold[i][1] == kjonn:
      print(f"{t:2.0f} {innhold[i][0]:42} {innhold[i][4]:5}")
      t += 1
      total += innhold[i][3]
  timer = np.floor(total)
  minutter = round((total - timer)*60)
  totaltekst = str(int(timer)) + ":" 
  if minutter < 10:
    totaltekst = totaltekst + "0" + str(minutter)
  else:
    totaltekst = totaltekst + str(minutter)
  print()
  print("Totalt tidsbruk på aktiviteter er ",totaltekst," timer")

def graf(kjonn):
  kategorier = []
  verdier = []
  for i in range(len(innhold)):
    if innhold[i][1] == kjonn:
      kategorier.append(innhold[i][0])
      verdier.append(innhold[i][3])
  kategorier.reverse()
  verdier.reverse()
  plt.barh(kategorier,verdier)
  plt.subplots_adjust(left=0.5)
  plt.grid(axis="x")
  tittel = "Tidsbruk i timer for " + kjonn
  plt.title(tittel)
  plt.show()


while (True):
  print()
  print("Meny:")
  print("Velg kjønn: ")
  print("m for Menn")
  print("k for Kvinner")
  print("a for Alle")
  print("q for Quit (avslutt)")
  print()
  svar = input("Valg: ")
  if svar == "q":
    break
  elif svar == "m":
    tabell("Menn")
    graf("Menn")
  elif svar == "k":
    tabell("Kvinner")
    graf("Kvinner")
  elif svar == "a":
    tabell("Alle")
    graf("Alle")
  else:
    print("Ugyldig valg, prøv igjen")



