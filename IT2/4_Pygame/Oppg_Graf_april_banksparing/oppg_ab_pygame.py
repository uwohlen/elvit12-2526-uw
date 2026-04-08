"""

Endret på oppgaven til å vise tabell basert på valgt kjønn,
siden tabellen ellers blir for lang.
Kan eventuelt dele tabellen i 2 og vise halvpartene ved siden av hverandre.

"""
###########################
# DATASETT, TABELL        #
###########################
 
import csv

filnavn = "bank.csv"

# legger hele datasettet inn i lista innhold for videre programmering
# og kolonnenavnene inn i lista overskrifter for å ta en kikk
innhold = []
with open(filnavn, encoding="utf-8-sig") as fil:
    filinnhold = csv.reader(fil, delimiter=";")
    overskrifter = next(filinnhold)

    for rad in filinnhold:
        innhold.append(rad)

overskrifter[0] = "ID"
overskrifter[1] = "Kjønn"
overskrifter[2] = overskrifter[2].capitalize() + " (kr)"
overskrifter[3] = "Rente (%)"
overskrifter.append("Etter ti år (kr)")
#print(overskrifter)
for rad in innhold:
    rad[0] = int(rad[0])
    rad[2] = int(rad[2])
    rad[3] = float(rad[3].replace(",","."))
    # regn ut innskudd * vekstfaktor ** 10
    # avrunding til 2 desimaler, gjør til tekst
    # hvis 2. desimal er 0, så vil den ikke vises i python float, 
    # legg den til som tekst
    rad.append(str(round((rad[2]*(1+rad[3]/100)**10)*100)/100))
    if rad[4][-2] == ".":
      rad[4] = rad[4] + "0"

#print(innhold)

##################################
# IMPORT. START pygame           #
##################################

import pygame as pg
import sys # brukes for å avslutte med sys.exit()
pg.init()

# Ta med muligheten til interaksjon ved tastaturet
from pygame.locals import (K_q, K_x)

# Egne KLASSER for knapper og nedtrekksmenyer 
import pygame_firkant_klasser as pk

######################################
# KONSTANTER, VINDU og FONT          #
######################################

# Størrelse på vindu, alt må forholde seg til det
VINDU_BREDDE = 1000
VINDU_HOYDE  = 730

# Oppretter et vindu der vi skal "tegne" innholdet vårt
vindu = pg.display.set_mode([VINDU_BREDDE, VINDU_HOYDE])

# Angir hvilken skrifttype og tekststørrelse vi vil bruke på tekst
font_overskrift = pg.font.SysFont("Arial",24)
font_knapp = pg.font.SysFont("Arial",20)
font_nedtrekk = pg.font.SysFont("Arial",20)


KNAPP_BREDDE = 100
KNAPP_HOYDE = 40
NEDTREKK_BREDDE = 100
NEDTREKK_HOYDE = 40
NEDTREKK_BREDDE_2D = 120
NEDTREKK_HOYDE_2D = 25

MENY_X = 50
MENY_Y = 50
MENY_FARGE = "magenta"
NEDTREKK_FARGE = "magenta3"
HOVER_FARGE = "green"

###########################
# OBJEKTER                #
###########################


#### LAG KNAPPER FOR VALG ####
titler = ["Velg kjønn"]
kolonne = pk.Nedtrekk(vindu,MENY_X,MENY_Y,KNAPP_BREDDE,KNAPP_HOYDE,MENY_FARGE,titler[0],font_knapp,["M","K"],NEDTREKK_FARGE,True)
kolonne.lag_alt_obj(NEDTREKK_BREDDE,NEDTREKK_HOYDE,font_nedtrekk)
nedtrekk = [kolonne]

#### LAG OVERSKRIFTER FOR TABELL ####

overskrift_obj = []
for i in range(len(overskrifter)):
  overskrift_obj.append(pk.Knapp(vindu,2*MENY_X+KNAPP_BREDDE+i*NEDTREKK_BREDDE_2D,MENY_Y,NEDTREKK_BREDDE_2D,NEDTREKK_HOYDE_2D,"yellow",overskrifter[i],font_nedtrekk))

###########################
# WHILE                   #
###########################

# Gjenta helt til brukeren lukker vinduet

# Globale variabler - status-sjekk
klikk = False   # Har brukeren klikket med musepekeren?
tabell = []
        
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
  pg.display.set_caption("Oppgave a og b")
  overskrift = font_overskrift.render("Oversikt over kontoer og sparing", True, "black")
  vindu.blit(overskrift,(10,10))

  #### VELG KOLONNE ####
  if klikk and kolonne.obj.collidepoint(x,y):
    tabell = []
    if not(kolonne.vis):
      kolonne.tekst = titler[0]
    kolonne.vis = not(kolonne.vis)
    klikk = False
  else:
    for n in kolonne.alt_obj:
      if klikk and n.obj.collidepoint(x,y) and kolonne.vis:
        kolonne.tekst = n.tekst
        kolonne.vis = False
        klikk = False
        
        #### LAG TABELL ####
        k=0
        for i in range(len(innhold)):
            if innhold[i][1] == n.tekst:
                k += 1
                tabell.append([])
                for j in range(len(innhold[i])):
                    tabell[-1].append(pk.Knapp(vindu,2*MENY_X+KNAPP_BREDDE+j*NEDTREKK_BREDDE_2D,MENY_Y+k*NEDTREKK_HOYDE_2D,NEDTREKK_BREDDE_2D,NEDTREKK_HOYDE_2D,"gray",innhold[i][j],font_nedtrekk))
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
  
   #### TEGN TABELL ####
  for kol in overskrift_obj:
    kol.tegn()
    kol.tegn(bredde=1)
    kol.vis_tekst()

  for rad in tabell:
    for i in range(len(rad)):
      rad[i].tegn()
      rad[i].tegn(bredde=1)
      if i == 2 or i == 3 or i == 4:
        rad[i].vis_tekst(align = "h")
      else:
        rad[i].vis_tekst()

  #####################
  # OPPDATER VINDU    #
  #####################
  pg.display.flip()

