# Initialiserer/starter pygame
import pygame as pg
import sys
pg.init()

# Ta med muligheten til interaksjon ved tastaturet
from pygame.locals import (K_q, K_x)

import random as rd

########################
# KONSTANTER           #
########################

# Størrelse på vindu, alt må forholde seg til det
VINDU_BREDDE = 600
VINDU_HOYDE  = 600

bilder = ["frisk_uten.png","smittet.png","syk.png","frisk_med.png","dod.png"]

########################
# VINDU og FONT        #
########################

# Oppretter et vindu der vi skal "tegne" innholdet vårt
vindu = pg.display.set_mode([VINDU_BREDDE, VINDU_HOYDE])

# Angir hvilken skrifttype og tekststørrelse vi vil bruke på tekst
font = pg.font.SysFont("Arial", 24)

klokke = pg.time.Clock()


###########################
# WHILE                   #
###########################

while True:

  #### BRUKER-INPUT ####
  for event in pg.event.get():
    if event.type == pg.QUIT:
      pg.quit() 
      sys.exit()

  trykkede_taster = pg.key.get_pressed()
  if trykkede_taster[K_q] or trykkede_taster[K_x]: # q for quit, x for eXit
    pg.quit() 
    sys.exit()


  #### BAKGRUNN ####
  vindu.fill("white")



  #### FIGURER OG TEKST ####
  x = 10
  y = 10
  side = 40
  forskyv = 5
  
  
  tilfeldig = rd.randint(1,2)
  if tilfeldig == 1:
    mittBilde = pg.image.load("smittet.png")
    pg.draw.rect(vindu, "pink", (x, y, side, side))
    pg.draw.line(vindu,"black",(x+forskyv,y+forskyv),(x+side-forskyv,y+side-forskyv),3)
  
  else:
    mittBilde = pg.image.load("syk.png")
    pg.draw.rect(vindu, "red", (x, y, side, side))
    pg.draw.line(vindu,"white",(x+forskyv,y+side-forskyv),(x+side-forskyv,y+forskyv),3)
  
  
  x = 100
  pg.draw.rect(vindu, "pink", (x, y, side, side))
  pg.draw.line(vindu,"black",(x+forskyv,y+forskyv),(x+side-forskyv,y+side-forskyv),3)

  x = 200
  pg.draw.rect(vindu, "red", (x, y, side, side))
  pg.draw.line(vindu,"white",(x+forskyv,y+side-forskyv),(x+side-forskyv,y+forskyv),3)

  y = 200
  vindu.blit(mittBilde, (x, y))


  #### OPPDATER VINDU ####
  pg.display.flip()

  klokke.tick(2) #frames per second (fps)