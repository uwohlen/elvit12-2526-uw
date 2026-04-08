import matplotlib.pyplot as plt
import numpy as np
import csv

# Klasse for å holde orden på data for hvert årstall
class Aarsdata:
  """Klasse for å representere data for ett årstall"""
  def __init__(self, aarstall:int, fodselstall:int, innflyttere:int, utflyttere:int):
    """Konstruktør"""
    self.aarstall = aarstall
    self.fodselstall = fodselstall
    self.innflyttere = innflyttere
    self.utflyttere = utflyttere
    self.netto_folkevekst = fodselstall + innflyttere - utflyttere

  def lagListe(self):
    return [self.aarstall, self.fodselstall, self.innflyttere, self.utflyttere, self.netto_folkevekst]

  def lagListeTekst(self):
    print(f"{self.aarstall:10} {self.fodselstall:10} {self.innflyttere:14} {self.utflyttere:13} {self.netto_folkevekst:18}")
 
  def visInfo(self):
    """Skriver ut informasjon om et årstall"""
    print(f"År {self.aarstall} hadde {self.fodselstall} fødsler, {self.innflyttere} innflyttere, {self.utflyttere} utflyttere og dermed en netto folkevekst på {self.netto_folkevekst}.")

# Liste for å holde på Aarsdata-objekter
aarsdata = []

# Leser inn datasettet
filnavn = "Datasett_fodselstall_komma.csv"

with open(filnavn, encoding="utf-8-sig") as fil:
  filinnhold = csv.reader(fil, delimiter=",")

  overskrifter = next(filinnhold)

  for rad in filinnhold:
    aarsdata_inn = 0
    fodselstall_inn = 0
    innflyttere_inn = 0
    utflyttere_inn = 0

    if rad[0] != '':
      aarsdata_inn = int(rad[0])
    if rad[1] != '':
      fodselstall_inn = int(rad[1])
    if rad[2] != '':
      innflyttere_inn = int(rad[2])
    if rad[3] != '':
      utflyttere_inn = int(rad[3])
   
    aarsdata.append(Aarsdata(aarsdata_inn, fodselstall_inn, innflyttere_inn, utflyttere_inn))

# Funksjon for å skrive ut datasettet i tabellform
def lagTabell():
  print("")
  print(f"{'Årstall':>10} {'Fødsler':>10} {'Innflyttere':>14} {'Utflyttere':>13} {'Netto folkevekst':>18}")
  for a in aarsdata:
    a_liste = a.lagListe()
    print(f"{a_liste[0]:10} {a_liste[1]:10} {a_liste[2]:14} {a_liste[3]:13} {a_liste[4]:18}")
  print("")

# Funksjon for å lage graf basert på brukerens ønsker
def lagGraf():
  print("")
  valgt_startaar = int(input("Velg startår (1945-2024): "))
  valgt_sluttaar = int(input("Velg sluttår (1945-2024): "))
  print("1 - fødselstall, 2 - innflyttinger, 3 - utflyttinger, 4 - netto folkevekst")
  valgt_alternativ = int(input("Velg kolonne/variabel: "))

  merkelapper = ["Årstall", "Antall fødsler", "Antall innflyttere", "Antall utflyttere", "Netto folkevekst"]
  aarstall = []
  verdi = []

  for aar in aarsdata:
    # Sjekker om årstall er innenfor valgt intervall
    if valgt_startaar <= aar.aarstall <= valgt_sluttaar:
      aarstall.append(aar.aarstall)

      verdi.append(aar.lagListe()[valgt_alternativ])

  if len(verdi) > 0:
    plt.plot(aarstall, verdi)
    plt.xlabel(merkelapper[0])
    plt.ylabel(merkelapper[valgt_alternativ])
    plt.grid()
    plt.show()
  else:
    print("Du må angi et gyldig årstall-intervall (i perioden 1945-2024).")

# Meny som lar brukeren velge hva som skal vises
avslutt = False
valgt_alternativ = 0

while not avslutt:
  print("")
  print("###########################")
  print("# Hva ønsker du å gjøre?  #")
  print("# 1 - vis tabell          #")
  print("# 2 - tegn graf           #")
  print("# 0 - avslutt             #")
  print("###########################")
  valgt_alternativ = int(input("Velg: "))

  if valgt_alternativ == 0:
    avslutt = True
  elif valgt_alternativ == 1:
    lagTabell()
  elif valgt_alternativ == 2:
    lagGraf()