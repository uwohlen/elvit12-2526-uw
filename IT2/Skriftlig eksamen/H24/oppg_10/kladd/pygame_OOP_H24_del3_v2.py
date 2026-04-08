import pygame as pg
import sys
pg.init()

from pygame.locals import (K_q, K_x)
import pygame_OOP_H24_klasser_del3_v2 as pk

VINDU_SIDE = 720
ANTALL_SIDE = 48
MIDTEN = round(ANTALL_SIDE/2)


vindu = pg.display.set_mode((VINDU_SIDE,VINDU_SIDE))
pg.display.set_caption("Oppgave 10")
klokke = pg.time.Clock()


folka = pk.Populasjon(vindu,ANTALL_SIDE)
folka.skap_ny_befolkning()

startverdier = [
  (MIDTEN,MIDTEN),
  (MIDTEN-1,MIDTEN),
  (MIDTEN+1,MIDTEN),
  (MIDTEN,MIDTEN-1),
  (MIDTEN,MIDTEN+1)
]
for plass in startverdier:
  folka.befolkning[plass[0]][plass[1]].nysmittet = True
  folka.smitten_tar_tak()
folka.befolkning[MIDTEN][MIDTEN].farge = "red"


#### Sjekker at startverdiene er på plass ####
def vis():
  for i in range(10):
    for j in range(10):
      print(f"{folka.befolkning[i][j].farge:9}",end=" ")
    print()
  print()
def dag():
  for i in range(10):
    for j in range(10):
      print(f"{folka.befolkning[i][j].dag:9}",end=" ")
    print()
  print()

#vis()
#dag()

def sjekk_alle():
  folka.smitt_naboer()
  folka.oppdater_tilstand()
  folka.smitten_tar_tak()
  vis()
#sjekk_alle()

while True:
  for event in pg.event.get():
    if event.type == pg.QUIT:
      pg.quit()
      sys.exit()
  
  trykkede_taster = pg.key.get_pressed()
  if trykkede_taster[K_q] or trykkede_taster[K_x]:
    pg.quit()
    sys.exit()

  vindu.fill("white")

  for i in range(ANTALL_SIDE):
    for j in range(ANTALL_SIDE):
      folka.befolkning[i][j].tegn()
      folka.befolkning[i][j].tegn(bredde=1,farge="lightgray")


  folka.smitt_naboer()
  folka.oppdater_tilstand()
  folka.smitten_tar_tak()  

  pg.display.flip()
  klokke.tick(10)

