##################################
# IMPORT. START pygame           #
##################################

import pygame as pg
import sys # brukes for å avslutte med sys.exit()
pg.init()

# Ta med muligheten til interaksjon ved tastaturet
from pygame.locals import (K_q, K_x, K_LEFT, K_RIGHT)

##################################
# KONSTANTER, VINDU              #
##################################
VINDU_BREDDE = 500
VINDU_HOYDE = 700
vindu = pg.display.set_mode([VINDU_BREDDE,VINDU_HOYDE])

##################################
# KLASSER                        #
##################################

class Spill:
  pass

class Firkant:
  pass

class Ball:
  pass

class Padde:
  pass
