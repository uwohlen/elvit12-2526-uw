import pygame as pg
import sys
pg.init()

from pygame.locals import (K_q, K_x)
import pygame_OOP_H24_klasser_del2 as pk

VINDU_BREDDE = 720
VINDU_HOYDE = 720
vindu = pg.display.set_mode((VINDU_BREDDE,VINDU_HOYDE))
pg.display.set_caption("Oppgave 10")
klokke = pg.time.Clock()

"""
person = pk.Person(vindu,0,0)
def sjekk():
  person.farge = "gray"
  person.nysmittet = True
  person.dag = 0
  person.smitten_tar_tak()
  
  for i in range(9):
    person.sjekk_tilstand()
  
  print(person.farge, person.dag)
for j in range(100):
  sjekk()
"""

folka = pk.Populasjon(vindu,10,10)
folka.skap_ny_befolkning()
print(len(folka.befolkning), len(folka.befolkning[0]))

def vis():
  for i in range(10):
    for j in range(10):
      print(f"{folka.befolkning[i][j].farge:9}",end=" ")
    print()
  print()

def ny():
  for i in range(10):
    for j in range(10):
      print(folka.befolkning[i][j].nysmittet,end=" ")
    print()
  print()

folka.befolkning[5][5].nysmittet = True
#ny()
#vis()
folka.smitten_tar_tak()
vis()
def sjekk_alle():
  folka.smitt_naboer()
  folka.oppdater_tilstand()
  folka.smitten_tar_tak()
  vis()
for k in range(100):
  sjekk_alle()


pg.quit()
sys.exit()
"""
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
  
  pg.display.flip()
  klokke.tick(1)
"""
