##################################
# IMPORT. START pygame           #
##################################

import pygame as pg
import sys
pg.init()

from pygame.locals import (K_q, K_x, K_m, K_k)
import pygame_firkant_klasser as pk

import csv

import matplotlib
import matplotlib.pyplot as plt
from io import BytesIO
matplotlib.use("Agg")

################
# LES FIL      #
################

filnavn = "bank.csv"
innhold = []
x_akse = ["Under 500 000 kr","500 000 kr eller mer"]
m = [0,0]
k = [0,0]
y_akse = [m,k]

def tell(liste,verdi,grense=500000):
  if verdi < grense:
    liste[0] += 1
  else:
    liste[1] += 1

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
  rad.append(rad[2]*(1+rad[3]/100)**10)
  if rad[1] == "M":
    tell(m,rad[2])  
  elif rad[1] == "K":
    tell(k,rad[2])

#print(innhold)
#print(x,m,k)

maks = 0
for rad in y_akse:
  for kol in rad:
    if kol > maks:
      maks = kol
#print(maks)

#######################
# GRAF                #
#######################

def graf(xliste,yliste,kjonn):
  #print(xliste,yliste,kjonn)
  tittel = "Kontoer for " + kjonn
  
  fig, ax = plt.subplots()
  ax.bar(xliste, yliste)
  ax.set_xlabel("Verdi på konto")
  ax.set_ylabel("Antall kontoer")
  ax.set_title(tittel)
  ax.set_ylim(0,maks+1)

  buf = BytesIO()
  plt.savefig(buf, format="png")
  buf.seek(0)
  plt.close(fig)
  bilde_av_graf = pg.image.load(buf)
  return bilde_av_graf


#################################
# PYGAME                        #
#################################

#### KONSTANTER ####

VINDU_BREDDE = 1200
VINDU_HOYDE = 700
KNAPP_BREDDE = 100
KNAPP_HOYDE = 40
MENY_X = 50
MENY_Y = 100
MENY_FARGE = "burlywood"

vindu = pg.display.set_mode((VINDU_BREDDE,VINDU_HOYDE))
font_overskrift = pg.font.SysFont("Arial",24)
font_knapp = pg.font.SysFont("Arial",size=20)

#### OBJEKTER ####

menn = pk.Knapp(vindu, MENY_X, MENY_Y, KNAPP_BREDDE, KNAPP_HOYDE, MENY_FARGE, "Menn (m)", font_knapp)
kvinner = pk.Knapp(vindu, 2*MENY_X+KNAPP_BREDDE, MENY_Y, KNAPP_BREDDE, KNAPP_HOYDE, MENY_FARGE, "Kvinner (k)", font_knapp)
knapper = [menn,kvinner]

#### START-VERDIER ####

klikk = False
valg = ""
bilde = ""

#### WHILE-LØKKA ####

while True:

  #### BRUKER-INPUT ####

  for event in pg.event.get():
    if event.type == pg.QUIT:
      pg.quit()
      sys.exit()
    elif event.type == pg.MOUSEBUTTONDOWN:
      x,y = pg.mouse.get_pos()
      klikk = True

  trykkede_taster = pg.key.get_pressed()
  if trykkede_taster[K_q] or trykkede_taster[K_x]:
    pg.quit()
    sys.exit()
  elif trykkede_taster[K_m]:
    bilde = graf(x_akse,y_akse[0],"Menn")
  elif trykkede_taster[K_k]:
    bilde = graf(x_akse,y_akse[1],"Kvinner")

  #### TEKST, FORKLARINGER #### 

  vindu.fill("lemonchiffon")

  pg.display.set_caption("Oppgave d")
  overskrift = font_overskrift.render("Opptelling av antall kontoer med under eller over 500 000 kr",True,"black")
  vindu.blit(overskrift,(10,10))
  
  forklaring = font_knapp.render("Velg kjønn fra kontolista (klikk eller skriv):",True,"black")
  vindu.blit(forklaring,(10,50))

  avslutt = font_knapp.render("Avslutt med q eller x",True,"black")
  vindu.blit(avslutt,(10,VINDU_HOYDE-40))

  #### KNAPPER, LAG GRAF ####
  i = 0
  for knapp in knapper:
    knapp.tegn()
    knapp.tegn(bredde=1)
    knapp.vis_tekst()
    if klikk and knapp.obj.collidepoint(x,y):
      #print(knapp.tekst,y_akse[i])
      bilde = graf(x_akse,y_akse[i],knapp.tekst[:-3])
      klikk = False
    i += 1

  if bilde != "":
    vindu.blit(bilde, (3*MENY_X+2*KNAPP_BREDDE,MENY_Y))
    pg.draw.rect(vindu,"black",(3*MENY_X+2*KNAPP_BREDDE,MENY_Y,bilde.get_width(),bilde.get_height()),width=1)


  pg.display.flip()

