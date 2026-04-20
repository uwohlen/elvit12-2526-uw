"""
Programmet under er basert på en tidlig "kladd" av eksamensoppgaven
så detaljer vil avvike.
"""

import pygame as pg
import random as rd
import sys
from pygame.locals import (K_UP, K_DOWN, K_LEFT, K_RIGHT,K_q,K_x,K_a)

# Initialiserer pygame
pg.init()
VINDU_BREDDE = 600
VINDU_HOYDE  = 500
vindu = pg.display.set_mode([VINDU_BREDDE, VINDU_HOYDE])

# Konstanter 
HOYDE = 20 
BREDDE = 60
STARTFART = 2 # farten til bunndyret
klokke = pg.time.Clock()

class Firkant:
  """
  Firkanter kan tegnes på skjermen, står i ro
  """
  def __init__(self, x:int, y:int, bredde:int, hoyde:int, farge, vindusobjekt):
    self.x = x
    self.y = y
    self.bredde = bredde
    self.hoyde = hoyde
    self.farge = farge
    self.vindusobjekt = vindusobjekt
    #objekt for kollisjonsdeteksjon:
    self.obj = pg.Rect(self.x, self.y, self.bredde, self.hoyde)

  def tegn(self):
    """Tegner firkanten"""
    pg.draw.rect(self.vindusobjekt, self.farge, self.obj)


class Plankton(Firkant):
  """
  Plankton tegnes på skjermen, og beveger seg automatisk etter et mønster
  """
  def __init__(self, x, y, bredde, hoyde, farge, vindusobjekt, fart):
    super().__init__(x, y, bredde, hoyde, farge, vindusobjekt)
    self.fart = fart

  def flytt(self):
    self.y += self.fart 
    self.obj = pg.Rect(self.x, self.y, self.bredde, self.hoyde)



class Bunndyr(Firkant):
  """
  Spillere kan tegnes på skjermen, flytte på seg og sjekke kollisjoner
  """
  def __init__(self, x, y, bredde, hoyde, farge, vindusobjekt, fart, styring):
    super().__init__(x, y, bredde, hoyde, farge, vindusobjekt)
    self.fart = fart  
    self.styring = styring
    self.poeng = 0

  def flytt(self, taster):
    """
    Flytter spiller, sjekker kollisjon mot vegger
    """
    if taster[self.styring[0]]: #venstre
      self.x -= self.fart
      if self.x < 0: # utenfor rammen
        self.x += self.fart
    if taster[self.styring[1]]: #høyre
      self.x += self.fart
      if self.x + self.bredde > self.vindusobjekt.get_width(): # utenfor rammen
        self.x -= self.fart   
    self.obj = pg.Rect(self.x, self.y, self.bredde, self.hoyde)

  def treff(self, planktonvar, ekstravar):
    """
    Treff planktonen
    """
    if self.obj.colliderect(planktonvar.obj): # treffer planktonfirkant
      planktonvar.y += 60
      if planktonvar.farge == (0,255,0):
        self.bredde += 20
        if self.bredde > self.vindusobjekt.get_width():
          print("ferdig")
          print(self.poeng)
          pg.quit()
          sys.exit()
      elif planktonvar.farge == (255,0,0):
        self.bredde -= 20
        if self.bredde <= 20:
          print("ferdig")
          print(self.poeng)
          pg.quit()
          sys.exit()
      elif planktonvar.farge == (255,255,0):
        self.poeng += 1 + ekstra
      if self.x + self.bredde > self.vindusobjekt.get_width(): # utenfor rammen
        self.x = self.vindusobjekt.get_width() - self.bredde

    


# Lager objektene
bunndyr = Bunndyr(200, 470, BREDDE, HOYDE+10 , (200,200,200), vindu, STARTFART,[K_LEFT,K_RIGHT])
farger = [(0,255,0),(255,255,0),(255,0,0)]
farge = rd.choice(farger)
plass_x = rd.randint(0,580)
plass_y = rd.randint(-40,-20)
plankton = Plankton(plass_x, plass_y, HOYDE, HOYDE, farge, vindu,STARTFART*3/2)
liste_med_planktoner = []
liste_med_planktoner.append(plankton)

# Gjenta helt til brukeren lukker vinduet
teller = 0
ekstra = 0
opp = False
ned = False
rate = 10
test = 0

while True:

  # Sjekker om brukeren har lukket vinduet
  for event in pg.event.get():
    if event.type == pg.QUIT:
      pg.quit()
      sys.exit()

# kan sette inn en sjekk her med 
# if event.type == pg.KEYDOWN:
# og 
# if event.key == pg.K_UP
# for å passe på at ting bare skjer EN gang pr trykk
# trenger ikke gå via trykkede_taster og pg.key.get_pressed()
# sjekk oneNote Samarbeidsområde for eksempel

  # Henter en ordbok med status for alle tastatur-taster
  trykkede_taster = pg.key.get_pressed()
  if trykkede_taster[K_q] or trykkede_taster[K_x]:
    pg.quit()
    sys.exit()
  if trykkede_taster[K_UP]:
    if not opp:
      if ekstra < 5:
        ekstra += 1
        rate -=1
        print("Level: ",ekstra)
      opp = True # for at man ikke skal plusse på flere ganger pr trykk
  else:
    opp = False # har sluppet opp tasten, klar for nye trykk
  if trykkede_taster[K_DOWN]:
    if not ned:
      if ekstra > 0:
        ekstra -= 1
        rate += 1
        print("Level: ",ekstra)
      ned = True
  else:
    ned = False
  if trykkede_taster[K_a]:
    test += 1 # telles flere ganger pr runde i while-løkken
    print(test)

  # Farger hele spillebrettet svart
  vindu.fill((0,0,0)) 

  # Tegner og flytter spillerne
  bunndyr.flytt(trykkede_taster)
  bunndyr.tegn()

  for planktoner in liste_med_planktoner:
    # Behandler plankton
    planktoner.flytt()
    planktoner.tegn()

    bunndyr.treff(planktoner,ekstra)

  teller += 1
  #print(rate)
  if teller%rate == 0:
    farger = [(0,255,0),(255,255,0),(255,0,0)]
    for i in range(ekstra):
      farger.append((0,255,0))
    farge = rd.choice(farger)
    plass_x = rd.randint(0,580)
    plass_y = rd.randint(-40,-20)
    nyplankton = Plankton(plass_x, plass_y, HOYDE, HOYDE, farge, vindu,STARTFART*3/2)
    liste_med_planktoner.append(nyplankton)
  
  # Oppdaterer alt innholdet i vinduet
  pg.display.flip()
  klokke.tick(100)