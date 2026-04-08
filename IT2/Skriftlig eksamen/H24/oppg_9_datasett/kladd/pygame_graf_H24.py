"""
Oppgavetekst: "Programmet du lager i denne oppgaven, skal inneholde en flerlinjekommentar øverst som beskriver de vurderingene og valgene du har gjort for å forberede datasettet til bruk i programmering, hvis du har gjort det."

Behandling av datasett-filen:
-det står at CSV-filen er UTF-8-kodet, men å og ø i overskriftene til de to første kolonnene blir ikke kodet riktig. Jeg har valgt å hardkode overskriftene i programmet under slik at de inneholder å og ø på riktig måte. Dermed vil nye versjoner av data-filen fremdeles kunne leses uten manuelle endringer i datafilen.

Tabellen blir fin hvis skriftstørrelsen ikke er for stor i forhold til terminalvinduet / konsollen.

Oppgave 9a kommer i terminalen
Oppgave 9b kommer i pygame-vinduet
"""

##################################
# IMPORT. START pygame           #
##################################

import pygame as pg
import sys # brukes for å avslutte med sys.exit()
pg.init()

# For datasett innlest fra CSV-fil
import csv

# For grafer inn i pygame
import matplotlib
import matplotlib.pyplot as plt
from io import BytesIO
# Sett Matplotlib til ikke-interaktiv modus med "Agg" som backend
matplotlib.use("Agg")

# Ta med muligheten til interaksjon ved tastaturet
from pygame.locals import (K_q)

########################
# KONSTANTER           #
########################

# Størrelse på vindu, alt må forholde seg til det
VINDU_BREDDE = 1000
VINDU_HOYDE  = 700



########################
# VINDU og FONT        #
########################

# Oppretter et vindu der vi skal "tegne" innholdet vårt
vindu = pg.display.set_mode([VINDU_BREDDE, VINDU_HOYDE])

# Angir hvilken skrifttype og tekststørrelse vi vil bruke på tekst
font = pg.font.SysFont("Arial", 24)


##################################
# DATASETT, TABELL og GRAF       #
##################################

filnavn = "Datasett_fodselstall_komma.csv"
alt = []

# Leser med csv.reader for å kunne endre overskriftene som inneholder å og ø
with open(filnavn,encoding="utf-8") as fil:
  hele_filen = csv.reader(fil)

  overskrifter = next(hele_filen)
  overskrifter[0] = "År"
  overskrifter[1] = "Fødselstall"
  overskrifter.append("Netto folkevekst")

  for linje in hele_filen:
    # kan ikke gjøre utregninger hvis vi ikke har alle verdiene
    if linje[1] != "" and linje[2] != "" and linje[3] != "": 
      linje.append(int(linje[1]) + int(linje[2]) - int(linje[3])) # regn ut netto folkevekst
    else:
      linje.append("") # legg inn tom verdi om netto folkevekst ikke kan regnes ut
    alt.append(linje)

# Alternativene som skal stå i nedtrekksmenyene:
  alternativer = overskrifter[1:] # kolonne
  startaar_alternativer = []
  for i in range(1945,2025):
    startaar_alternativer.append(i)
  
def oppg9a():
  print()
  print("Oppgave 9a: Tabell over Fødselstall, Innflyttinger, Utflyttinger og Netto folkevekst")
  print()
  # Lag overskrifter i tabellen
  for i in range(len(overskrifter)):
    print(f"{overskrifter[i]:16}" + " | ", end="") # Bredeste overskrift er 15 bokstaver, +1 for luft
  print()

  # Strek mellom overskrifter og innhold
  for i in range(19*len(overskrifter)): # Kolonnebredden er 19 bokstaver inkludert |
    print("-", end="")
  print()

  # Skriv ut hele tabellen, årstall er venstrestilt, resten høyrestilt
  # Regner med at tabellen skal inneholde årstall selv om det ikke sto i oppgaveteksten.
  for i in range(len(alt)):
    for j in range(len(alt[i])):
      if j == 0:
        print(f"{alt[i][j]:<16}" + " | ", end="")
      else:
        print(f"{alt[i][j]:>16}" + " | ", end="")
    print()

  # Strek under tabellen
  for i in range(19*len(overskrifter)):
    print("-", end="")
  print()

  #### FERDIG OPPGAVE 9A ####

oppg9a()

def graf(xliste,yliste,start,slutt):

  # Lag en figur-variabel, og putt grafen inn i den
  fig, ax = plt.subplots()
  ax.plot(xliste, yliste)
  ax.scatter(xliste, yliste)

  # For verdiene på x-aksen:
  plt.xlim(start,slutt) # Få med start og slutt-årstall selv om verdier mangler
  if len(xliste) < 10:
    plt.xticks(xliste,minor=False) # unngå desimaltall når det er få verdier

  # Lagre diagrammet som en bildebuffer
  buf = BytesIO()
  plt.savefig(buf, format="png")
  buf.seek(0)
  plt.close(fig) # Putter figurvariabelen inn i png-filen
  bilde_av_graf = pg.image.load(buf)

  # Skalerer bildet til å passe til vinduet.
  bilde_skalert = pg.transform.scale(bilde_av_graf,(800,600))
  return bilde_skalert

###########################
# WHILE                   #
###########################

# Gjenta helt til brukeren lukker vinduet

# Globale variabler - status-sjekk
klikk = False               # Har brukeren klikket med musepekeren?
valg_objekter = []          # objekter for "kollisjon" av alternativene
valgt = ""                  # Har brukeren valgt noe fra nedtrekksmenyen?
valg_startaar_objekter = [] # objekter for "kollisjon" av alternativene
valgt_startaar = ""         # Har brukeren valgt noe fra nedtrekksmenyen?
valg_sluttaar_objekter = [] # objekter for "kollisjon" av alternativene
valgt_sluttaar = ""         # Har brukeren valgt noe fra nedtrekksmenyen?
  
while True:

  ###################
  # BRUKER-INPUT    #
  ###################

  for event in pg.event.get():
    # Sjekker om brukeren har lukket vinduet (X i øvre høyre hjørne)
    if event.type == pg.QUIT:
      pg.quit() # avslutter med en gang
      sys.exit()
    # Sjekker om brukeren har klikket med musepekeren
    elif event.type == pg.MOUSEBUTTONDOWN:
      x, y = pg.mouse.get_pos() # får tak i posisjonen
      klikk = True

  # Henter en liste med status for alle tastatur-taster
  trykkede_taster = pg.key.get_pressed()
  # Sjekker om brukeren har trykket på tastaturet siden forrige runde 
  # Behandler forskjellige taster (flere kan være brukt):
  if trykkede_taster[K_q]: # q for quit
    pg.quit()
    sys.exit()
  
   

  ###############################
  # OBJEKTER, FIGURER og TEKST  #
  ###############################

  #### BAKGRUNN ####
  vindu.fill("white")

  
  #### LAG KNAPPER FOR VALG ####
  # Hovedruta for nedtrekksmenyen (kolonne)
  nedtrekk = pg.Rect(10,10,160,40)
  # Hovedruta for nedtrekksmenyen (startår)
  startaar = pg.Rect(180,10,160,40)
  # Hovedruta for nedtrekksmenyen (sluttår)
  sluttaar = pg.Rect(350,10,160,40)
  # Knapp (tegn graf)
  knapp = pg.Rect(520,10,160,40) 
  


  ########################
  # KLIKK + COLLIDEPOINT #
  ########################  

  # Tegner graf basert på kolonne og valgte årstall
  if klikk and knapp.collidepoint((x,y)):
      if valgt in overskrifter and valgt_startaar != "" and valgt_sluttaar != "":
        indeks = overskrifter.index(valgt)
        x_verdier = []
        y_verdier = []

        for aar in range(valgt_startaar,(valgt_sluttaar+1)):
          aar_indeks = startaar_alternativer.index(aar)
          if alt[aar_indeks][indeks] != "":
            x_verdier.append(aar)
            y_verdier.append(int(alt[aar_indeks][indeks]))

        bilde_skalert = graf(x_verdier, y_verdier, valgt_startaar, valgt_sluttaar)
        vindu.blit(bilde_skalert, (100, 50))


  # Vis fram alternativene i nedtrekksmenyen
  elif klikk and nedtrekk.collidepoint((x,y)): # klikket på nedtrekksmenyen
    valgt = ""
    valg_objekter = []
    valgt_startaar = ""
    valg_startaar_objekter = []
    valgt_sluttaar = ""
    valg_sluttaar_objekter = []
    for i in range(len(alternativer)): # åpne nedtrekksmenyen ved å tegne firkanter
      valg_objekter.append(pg.Rect(10,50+40*i,160,40)) # settes under den forrige
      pg.draw.rect(vindu,"magenta3",valg_objekter[i])
      nedtrekk_bilde1 = font.render(alternativer[i],True,"black")
      vindu.blit(nedtrekk_bilde1,(20,55+40*i))
  else:
    # Sjekk om man klikket på et alternativ
    for i in range(len(valg_objekter)):
      if klikk and valg_objekter[i].collidepoint((x,y)):
        valgt = alternativer[i]
        klikk = False
    # Alternativene er brukt opp, eller man klikket utenfor
    valg_objekter = []
    # Sjekk om man klikket på et startaar
    for i in range(len(valg_startaar_objekter)):
      if klikk and valg_startaar_objekter[i].collidepoint((x,y)):
        valgt_startaar = startaar_alternativer[i]
        klikk = False
    valg_startaar_objekter = []
    # Sjekk om man klikket på et sluttaar
    for i in range(len(valg_sluttaar_objekter)):
      if klikk and valg_sluttaar_objekter[i].collidepoint((x,y)):
        valgt_sluttaar = sluttaar_alternativer[i]
        klikk = False
    valg_sluttaar_objekter = []

  # Oppdater nedtrekksmenyen basert på alternativ valgt
  pg.draw.rect(vindu,"magenta",nedtrekk) 
  if valgt == "":
    nedtrekk_bilde = font.render("Velg kolonne", True, "black")
    vindu.blit(nedtrekk_bilde,(20,15))
  else:
    nedtrekk_bilde = font.render(valgt, True, "black")
    vindu.blit(nedtrekk_bilde,(20,15))
    #### VELG STARTÅR ####
    # Tegn hovedruta for nedtrekksmenyen (startår)
    pg.draw.rect(vindu,"magenta",startaar)
      
    # Tid for å velge startår
    if valgt_startaar == "":  
      startaar_tekst = font.render("Velg startår", True, "black")
      vindu.blit(startaar_tekst,(190,15))

      shift_x = 0
      shift_y = 0
      for j in range(len(startaar_alternativer)): # åpne nedtrekksmenyen for startår
        valg_startaar_objekter.append(pg.Rect(180+50*shift_x,50+30*shift_y,50,30))
        pg.draw.rect(vindu,"magenta3",valg_startaar_objekter[j])
        startaar_tekst = font.render(str(startaar_alternativer[j]),True,"black")
        vindu.blit(startaar_tekst,(185+50*shift_x,55+30*shift_y))
        shift_y += 1
        if shift_y%20 == 0:
          shift_x += 1
          shift_y = 0
    else:
      startaar_tekst = font.render(str(valgt_startaar), True, "black")
      vindu.blit(startaar_tekst,(190,15))
      #### VELG SLUTTÅR ####
      # Tegn hovedruta for nedtrekksmenyen (sluttår)
      pg.draw.rect(vindu,"magenta",sluttaar)
      if valgt_sluttaar == "":
        sluttaar_tekst = font.render("Velg sluttår", True, "black")
        vindu.blit(sluttaar_tekst,(360,15))
        startaar_indeks = startaar_alternativer.index(valgt_startaar) +1
        sluttaar_alternativer = startaar_alternativer[startaar_indeks:]
        shift_x = 0
        shift_y = 0
        for k in range(len(sluttaar_alternativer)):
          valg_sluttaar_objekter.append(pg.Rect(350+50*shift_x,50+30*shift_y,50,40))
          pg.draw.rect(vindu,"magenta3",valg_sluttaar_objekter[k])
          sluttaar_tekst = font.render(str(sluttaar_alternativer[k]),True,"black")
          vindu.blit(sluttaar_tekst,(355+50*shift_x,55+30*shift_y))
          shift_y += 1
          if shift_y%20 == 0:
            shift_x += 1
            shift_y = 0
      else:
        sluttaar_tekst = font.render(str(valgt_sluttaar),True, "black")  
        vindu.blit(sluttaar_tekst,(360,15)) 
        #### TEGN GRAF ####
        pg.draw.rect(vindu,"magenta",knapp)
        bilde = font.render("Tegn graf", True, "black")
        vindu.blit(bilde, (530, 15))


  #####################
  # OPPDATER VINDU    #
  #####################
  pg.display.flip()
