import pygame as pg
import sys
pg.init()

from pygame.locals import (K_q, K_x)
import pygame_OOP_H24_klasser_del1 as pk

VINDU_BREDDE = 720
VINDU_HOYDE = 720
vindu = pg.display.set_mode((VINDU_BREDDE,VINDU_HOYDE))
pg.display.set_caption("Oppgave 10")
klokke = pg.time.Clock()


person = pk.Person(vindu,0,0)
def sjekk():
  person.farge = "gray"
  person.dag = 0
  person.bli_smittet()
  
  for i in range(9):
    person.sjekk_tilstand()
  
  print(person.farge, person.dag)
for j in range(100):
  sjekk()


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
