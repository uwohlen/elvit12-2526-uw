# Initialiserer/starter pygame
import pygame as pg
pg.init()

# Ta med muligheten til interaksjon ved tastaturet
from pygame.locals import (K_q,K_RETURN)

########################
# KONSTANTER           #
########################

# Størrelse på vindu, alt må forholde seg til det
VINDU_BREDDE = 600
VINDU_HOYDE  = 600



########################
# VINDU og FONT        #
########################

# Oppretter et vindu der vi skal "tegne" innholdet vårt
vindu = pg.display.set_mode([VINDU_BREDDE, VINDU_HOYDE])

# Angir hvilken skrifttype og tekststørrelse vi vil bruke på tekst
font = pg.font.SysFont("Arial", 24)


###########################
# WHILE                   #
###########################

# Gjenta helt til brukeren lukker vinduet
fortsett = True
enter = False # Har brukeren trykket Enter-tasten?

while fortsett:

  #### BRUKER-INPUT ####
  for event in pg.event.get():
    # Sjekker om brukeren har lukket vinduet (X i øvre høyre hjørne)
    if event.type == pg.QUIT:
      fortsett = False

  # Henter en liste med status for alle tastatur-taster
  trykkede_taster = pg.key.get_pressed()
  # Sjekker om brukeren har trykket på tastaturet og 
  # Behandler forskjellige taster:
  if trykkede_taster[K_q]: # q for quit
    fortsett = False
  if trykkede_taster[K_RETURN]: # Enter-tasten for f.eks. å velge "OK-knappen"
    enter = True

  #### BAKGRUNN ####
  # Farger bakgrunnen hvit
  vindu.fill("white")



  #### FIGURER OG TEKST ####
  # Det som er tegnet sist vil vises, pixel for pixel

  # Tegner et rektangel pg.draw.rect(vindu,farge,(x,y,b,h))
  if enter:
    firkant_farge = "magenta"
  else:
    firkant_farge = "green"
  pg.draw.rect(vindu, firkant_farge, (10, 10, 100, 50))
  
  # Lager en tekst i form av et bilde og legger til bildet i vinduet
  # bilde = font.render(tekst, True, farge)
  # vindu.blit(bilde, (x, y)) for øvre venstre hjørne av teksten
  # teksten legger seg over firkanten

  bilde = font.render("OK", True, "black")
  vindu.blit(bilde, (20, 20))


  #### Tester polygon og fargevalg for 3D-effekt ####

  pg.draw.rect(vindu,"dimgray",(100,100,100,100))
  # må fjerne 1 pixel for "linjebredde"
  pg.draw.polygon(vindu,"lightgray",((100,100),(200-1,100),(100,200-1)))
  pg.draw.rect(vindu,"gray",(110,110,80,80))

  #### OPPDATER VINDU ####
  pg.display.flip()

#### Avslutter pygame når while-løkken er ferdig ####
pg.quit()