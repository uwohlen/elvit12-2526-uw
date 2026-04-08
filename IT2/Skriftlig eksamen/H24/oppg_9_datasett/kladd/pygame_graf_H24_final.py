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
from matplotlib.ticker import MaxNLocator
from io import BytesIO
# Sett Matplotlib til ikke-interaktiv modus med "Agg" som backend
matplotlib.use("Agg")

# Ta med muligheten til interaksjon ved tastaturet
from pygame.locals import (K_q, K_x)

# Egne KLASSER for knapper og nedtrekksmenyer 
import pygame_graf_H24_klasser_final as pk

######################################
# KONSTANTER, VINDU og FONT          #
######################################

# Størrelse på vindu, alt må forholde seg til det
VINDU_BREDDE = 1000
VINDU_HOYDE  = 700

# Oppretter et vindu der vi skal "tegne" innholdet vårt
vindu = pg.display.set_mode([VINDU_BREDDE, VINDU_HOYDE])

# Angir hvilken skrifttype og tekststørrelse vi vil bruke på tekst
font_overskrift = pg.font.SysFont("Arial",24)
font_knapp = pg.font.SysFont("Arial",20)
font_nedtrekk = pg.font.SysFont("Arial",20)

KNAPP_BREDDE = 160
KNAPP_HOYDE = 40
NEDTREKK_BREDDE = 160
NEDTREKK_HOYDE = 40
NEDTREKK_BREDDE_2D = 50
NEDTREKK_HOYDE_2D = 30

MENY_X = 50
MENY_Y = 50
MENY_FARGE = "magenta"
NEDTREKK_FARGE = "magenta3"
HOVER_FARGE = "green"

###########################
# DATASETT, TABELL        #
###########################

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
  for i in range(len(alt)):
    startaar_alternativer.append(alt[i][0])
  
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


##########################
# GRAF                   #
##########################

def graf(xliste,yliste,start,slutt,kolonne):

  tittel = kolonne + "   " + str(start) + " - " + str(slutt)
  # Lag en figur-variabel, og putt grafen inn i den
  fig, ax = plt.subplots()
  ax.plot(xliste, yliste)
  ax.scatter(xliste, yliste)
  ax.set_xlabel("Årstall")
  ax.set_ylabel("Antall personer")
  ax.set_title(tittel)

  # For verdiene på x-aksen:
  ax.xaxis.set_major_locator(MaxNLocator(integer=True))
  
  # Lagre diagrammet som en bildebuffer
  buf = BytesIO()
  plt.savefig(buf, format="png")
  buf.seek(0)
  plt.close(fig) # Putter figurvariabelen inn i png-filen
  bilde_av_graf = pg.image.load(buf)

  # Skalerer bildet til å passe til vinduet.
  #bilde_skalert = pg.transform.scale(bilde_av_graf,(800,600))
  return bilde_av_graf


###########################
# OBJEKTER                #
###########################


#### LAG KNAPPER FOR VALG ####
titler = ["Velg kolonne","Velg startår","Velg sluttår"]
kolonne = pk.Nedtrekk(vindu,MENY_X,MENY_Y,KNAPP_BREDDE,KNAPP_HOYDE,MENY_FARGE,titler[0],font_knapp,alternativer,NEDTREKK_FARGE,True)

kolonne.lag_alt_obj(NEDTREKK_BREDDE,NEDTREKK_HOYDE,font_nedtrekk)


startaar = pk.Nedtrekk(vindu,2*MENY_X+KNAPP_BREDDE,MENY_Y,KNAPP_BREDDE,KNAPP_HOYDE,MENY_FARGE,titler[1],font_knapp,startaar_alternativer,NEDTREKK_FARGE,False)


sluttaar = pk.Nedtrekk(vindu,3*MENY_X+2*KNAPP_BREDDE,MENY_Y,KNAPP_BREDDE,KNAPP_HOYDE,MENY_FARGE,titler[2],font_knapp,startaar_alternativer,NEDTREKK_FARGE,False)


nedtrekk = [kolonne,startaar,sluttaar]

###########################
# WHILE                   #
###########################

# Gjenta helt til brukeren lukker vinduet

# Globale variabler - status-sjekk
klikk = False   # Har brukeren klikket med musepekeren?

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
  if trykkede_taster[K_q] or trykkede_taster[K_x]: # q for quit, x for eXit
    pg.quit()
    sys.exit()
  
  # Museposisjon for hover-farge
  muspos = pg.mouse.get_pos()

   

  ###############################
  # OBJEKTER, FIGURER og TEKST  #
  ###############################

  #### BAKGRUNN ####
  vindu.fill("white")

  #### OVERSKRIFT ####
  pg.display.set_caption("Oppgave 9b")
  overskrift = font_overskrift.render("Befolkningsutvikling i årene 1945 - 2024", True, "black")
  vindu.blit(overskrift,(10,10))

  #### VELG KOLONNE ####
  if klikk and kolonne.obj.collidepoint(x,y):
    if not(kolonne.vis):
      kolonne.tekst = titler[0]
      startaar.tekst = titler[1]
      sluttaar.tekst = titler[2]
      startaar.vis = False
      sluttaar.vis = False
    kolonne.vis = not(kolonne.vis)
    klikk = False
  elif klikk and startaar.obj.collidepoint(x,y) and kolonne.tekst != titler[0]:
    if not(startaar.vis):
      startaar.tekst = titler[1]
      sluttaar.tekst = titler[2]
      sluttaar.vis = False
    startaar.vis = not(startaar.vis)
    klikk = False
  elif klikk and sluttaar.obj.collidepoint(x,y) and startaar.tekst != titler[1]:
    if not(sluttaar.vis):
      sluttaar.tekst = titler[2]
    sluttaar.vis = not(sluttaar.vis)
    klikk = False
  else:
    for n in kolonne.alt_obj:
      if klikk and n.obj.collidepoint(x,y) and kolonne.vis:
        kolonne.tekst = n.tekst
        indeks = overskrifter.index(kolonne.tekst)
        startaar.alternativer = []
        for i in range(len(alt)):
          if alt[i][indeks] != "":
            startaar.alternativer.append(alt[i][0])
        startaar.alt_obj = []
        startaar.lag_alt_obj(NEDTREKK_BREDDE_2D,NEDTREKK_HOYDE_2D,font_nedtrekk,20)
        kolonne.vis = False
        klikk = False
        startaar.tekst = titler[1]
        startaar.vis = True
        break
    for aar in startaar.alt_obj:
      if klikk and aar.obj.collidepoint(x,y) and startaar.vis:
        startaar.tekst = aar.tekst
        indeks = overskrifter.index(kolonne.tekst)
        sluttaar.alternativer = []
        for i in range(len(alt)):
          if alt[i][indeks] != "" and int(alt[i][0]) > int(startaar.tekst):
            sluttaar.alternativer.append(alt[i][0])
        sluttaar.alt_obj = []
        sluttaar.lag_alt_obj(NEDTREKK_BREDDE_2D,NEDTREKK_HOYDE_2D,font_nedtrekk,20)
        startaar.vis = False
        klikk = False
        sluttaar.tekst = titler[2]
        sluttaar.vis = True
        break
    for aar2 in sluttaar.alt_obj:
      if klikk and aar2.obj.collidepoint(x,y) and sluttaar.vis:
        sluttaar.tekst = aar2.tekst
        sluttaar.vis = False
        klikk = False
        break
        

  #### TEGN NEDTREKKSMENYER ####
  for objekt in nedtrekk:
    if objekt.obj.collidepoint(muspos): # hover
      objekt.tegn(farge=HOVER_FARGE)
    else:
      objekt.tegn()
    objekt.tegn(bredde=2)
    objekt.vis_tekst()

    if objekt.vis:
      for n in objekt.alt_obj:
        if n.obj.collidepoint(muspos): # hover
          n.tegn(farge=HOVER_FARGE)
        else:
          n.tegn()
        n.tegn(bredde=1)
        n.vis_tekst()
  
  #### TEGN GRAF ####
  if kolonne.tekst != titler[0] and startaar.tekst != titler[1] and sluttaar.tekst != titler[2]:
    kol_indeks = overskrifter.index(kolonne.tekst)
    x_verdier = []
    y_verdier = []

    for aar in range(int(startaar.tekst),int(sluttaar.tekst)+1):
      aar_indeks = startaar_alternativer.index(str(aar))
      if alt[aar_indeks][kol_indeks] != "":
        x_verdier.append(aar)
        y_verdier.append(int(alt[aar_indeks][kol_indeks]))

    bilde_skalert = graf(x_verdier, y_verdier, int(startaar.tekst),int(sluttaar.tekst),kolonne.tekst)
    vindu.blit(bilde_skalert, (MENY_X + KNAPP_BREDDE, 3*KNAPP_HOYDE))

  #####################
  # OPPDATER VINDU    #
  #####################
  pg.display.flip()

