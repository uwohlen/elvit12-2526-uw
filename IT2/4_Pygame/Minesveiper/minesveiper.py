import pygame as pg
import sys
pg.init()

from pygame.locals import (K_q, K_x)
import minesveiper_klasser as pk

# Spillebrettets størrelse og konstanter
ANTALLX = 9
ANTALLY = 9
ANTALL_MINER = 10
RUTE_SIDE = 30 # NB! Bildene er 30x30 piksler, hvis denne endres på bildene skaleres
VINDU_BREDDE = ANTALLX*RUTE_SIDE
VINDU_HOYDE = ANTALLY*RUTE_SIDE

vindu = pg.display.set_mode((VINDU_BREDDE,VINDU_HOYDE))

pg.display.set_caption("Oppgave animasjon")
font_knapp = pg.font.SysFont("Arial",20,bold=True)

farger = ["lightgray","blue","darkgreen","red","darkblue","brown","cyan","black","gray"]


# Objektene
spillebrett = pk.Rutenett(vindu,ANTALLX,ANTALLY,ANTALL_MINER)
spillebrett.lag_nytt_rutenett(font_knapp,farger[0])
spillebrett.lag_miner()
spillebrett.tell_nabo_miner()


#### Sjekker at startverdiene er på plass ####
def vis_miner():
  for i in range(len(spillebrett.ruter)):
    for j in range(len(spillebrett.ruter[0])):
      #print(f"{spillebrett.ruter[i][j].farge:9}",end=" ")
      print(f"{spillebrett.ruter[i][j].mine:9}",end=" ")
      #print(f"{spillebrett.ruter[i][j].tekst:9}",end=" ")
    print()
  print()

def vis_tekst():
  for i in range(len(spillebrett.ruter)):
    for j in range(len(spillebrett.ruter[0])):
      #print(f"{spillebrett.ruter[i][j].farge:9}",end=" ")
      #print(f"{spillebrett.ruter[i][j].mine:9}",end=" ")
      print(f"{spillebrett.ruter[i][j].tekst:9}",end=" ")
    print()
  print()

#vis_miner()
#vis_tekst()


# Spill-løkka

klikk = False
fortsett = True

while True:

  # Hendelser
  for event in pg.event.get():
    if event.type == pg.QUIT:
      pg.quit()
      sys.exit()
    elif event.type == pg.MOUSEBUTTONDOWN:
      if fortsett:
        x, y = pg.mouse.get_pos()
        klikk = True

  trykkede_taster = pg.key.get_pressed()
  if trykkede_taster[K_q] or trykkede_taster[K_x]:
    pg.quit()
    sys.exit()

  # Oppdateringer

  vindu.fill("white")
  pg.display.set_caption("Minesveiper")
  

  # Sjekker hver rute for klikk
  for i in range(ANTALLY):
    for j in range(ANTALLX):
      if klikk and spillebrett.ruter[i][j].obj.collidepoint(x,y):
        spillebrett.ruter[i][j].visning = True
        # Traff mine - stopp spillet
        if spillebrett.ruter[i][j].mine:
          spillebrett.ruter[i][j].farge = "red"
          fortsett = False
        else:
          # Traff ikke mine - tell antall viste ruter
          # Hvis man har funnet alle uten mine: stopp spillet
          if spillebrett.ruter[i][j].farge == "lightgray":
            spillebrett.ruter[i][j].farge = "darkgray"
            spillebrett.vist += 1
            if spillebrett.vist == spillebrett.antall_x*spillebrett.antall_y - spillebrett.antall_miner:
              fortsett = False
        klikk = False
      
      # Oppdater tegningen av ruter og innskriving av antall miner
      spillebrett.ruter[i][j].tegn()
      if spillebrett.ruter[i][j].visning and spillebrett.ruter[i][j].tekst != 0:
        farge = farger[spillebrett.ruter[i][j].tekst]
        spillebrett.ruter[i][j].vis_tekst(farge)

      # Rutenett
      spillebrett.ruter[i][j].tegn(bredde=1,farge="gray")
  
  # Visning av mine-plasseringene
  if fortsett == False:
    for i in range(ANTALLY):
      for j in range(ANTALLX):
        if spillebrett.ruter[i][j].mine:
          # Vant
          if spillebrett.vist == spillebrett.antall_x*spillebrett.antall_y - spillebrett.antall_miner:
            bilde = pg.image.load("mineflagg.png")
          # Tapte
          elif spillebrett.ruter[i][j].farge == "red":
            bilde = pg.image.load("bombe_rod.png")
          else:
            bilde = pg.image.load("bombe_graa.png")
          vindu.blit(bilde,(spillebrett.ruter[i][j].x,spillebrett.ruter[i][j].y))
  
  pg.display.flip()

