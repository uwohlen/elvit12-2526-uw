import pygame as pg

class Firkant:
  def __init__(self,vindu,x,y,bredde,hoyde,farge):
    self.vindu = vindu
    self.x = x
    self.y = y
    self.bredde = bredde
    self.hoyde = hoyde
    self.farge = farge
    self.obj = pg.Rect(self.x, self.y, self.bredde, self.hoyde)

  def tegn(self):
    pg.draw.rect(self.vindu, self.farge, self.obj)

  def __str__(self):
    return f"Posisjon: ({self.x},{self.y})\nStørrelse: ({self.bredde},{self.hoyde})\nFarge: {self.farge}"



class Knapp(Firkant):
  def __init__(self,vindu,x,y,bredde,hoyde,farge,tekst):
    super().__init__(vindu,x,y,bredde,hoyde,farge)
    self.tekst = tekst

  def __str__(self):
    return f"Posisjon: ({self.x},{self.y})\nStørrelse: ({self.bredde},{self.hoyde})\nFarge: {self.farge}\nTekst: {self.tekst}"

  def vis_tekst(self):
    pass

  def klikk(self):
    pass


class Nedtrekk(Knapp):
  def __init__(self,vindu,x,y,bredde,hoyde,farge,tekst,alternativer):
    super().__init__(vindu,x,y,bredde,hoyde,farge,tekst)
    self.alternativer = alternativer
    self.alt_obj = [] 
  
  def lag_alt_obj(self):
    # lag liste med objekter, ett objekt for hvert alternativ
    pass

  def klikk(self):
    # vis alternativer
    pass

  def __str__(self):
    return f"Posisjon: ({self.x},{self.y})\nStørrelse: ({self.bredde},{self.hoyde})\nFarge: {self.farge}\nTekst: {self.tekst}\nAlternativer: {self.alternativer}"

