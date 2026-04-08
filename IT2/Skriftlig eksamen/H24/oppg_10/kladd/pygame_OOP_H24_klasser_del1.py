import pygame as pg
import random as rd

class Firkant:
  """
  Firkanter blir objekter og kan tegnes

    Egenskaper
      plassering: x,y i vindu
      størrelse:  bredde, høyde
      farge:      fargekode eller fargenavn
      objekt:     obj

    Metoder
      tegn: bredde: angis om det er kantstrek, ellers blir det heldekkende farge
            farge:  kan angi nye farger
            radius: kan angi runde hjørner
      
      __str__: for utskrift av egenskaper
  """
  def __init__(self,vindu,x:int,y:int,bredde:int,hoyde:int,farge):
    self.vindu = vindu
    self.x = x
    self.y = y
    self.bredde = bredde
    self.hoyde = hoyde
    self.farge = farge
    self.obj = pg.Rect(self.x, self.y, self.bredde, self.hoyde)

  def tegn(self,bredde:int=0,farge="",radius:int=-1):
    # tegn firkanten
    if bredde == 0:
      # heldekkende farge
      if farge == "":
        # bruk firkantens farge
        pg.draw.rect(self.vindu, self.farge, self.obj, bredde, radius)
      else: 
        # bruk en annen farge
        pg.draw.rect(self.vindu, farge, self.obj, bredde, radius)
    else:
      # tegn omriss
      if farge == "":
        # hvis angitt farge mangler, så settes det til svart omriss
        farge = "black"
      pg.draw.rect(self.vindu, farge, self.obj, bredde, radius)
      

  def __str__(self):
    return f"Posisjon: ({self.x},{self.y})\nStørrelse: ({self.bredde},{self.hoyde})\nFarge: {self.farge}"


PERSON_BREDDE = 15
PERSON_HOYDE = 15

class Person(Firkant):
  """
  Personer er firkanter med varierende grafikk, arver fra klassen Firkant

    Nye egenskaper
      helsetilstand: farge
      antall dager som smittet/syk: dager

    Redigert metode:
      tegn: verdi av tilstand påvirker grafikken
      
  """
  def __init__(self,vindu,x:int,y:int,bredde:int=PERSON_BREDDE,hoyde:int=PERSON_HOYDE,farge="gray",dag=0):
    super().__init__(vindu,x,y,bredde,hoyde,farge)
    self.dag = dag

  def __str__(self):
    return super().__str__() + f"\nDag: {self.dag}"

  def bli_smittet(self):
    # Kjøres bare når frisk uten immunitet: farge == gray
    if self.farge == "gray":
      self.farge = "pink"
      self.dag = 1
  
  def sjekk_tilstand(self):
    # Kjøres bare når smittet eller syk: farge = pink / red
    if self.farge == "pink" or self.farge == "red":
      self.dag += 1

    if self.farge == "pink" and self.dag > 3:
      self.farge = "red"
      self.dag = 1
      if rd.random() < 0.01:
        self.farge = "black" # kan dø allerede første dagen
    elif self.farge == "red" and self.dag in [2,3,4]:
      if rd.random() < 0.01:
        self.farge = "black"
    elif self.farge == "red" and self.dag > 4:
      self.farge = "darkgray"


  


