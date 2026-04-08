import pygame as pg
import random as rd

class Firkant:
  """
  Firkanter blir objekter og kan tegnes
  Klasse lagd da jeg øvde på eksamen V24

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


class Person(Firkant):
  """
  Personer er kvadrater med varierende grafikk, arver fra klassen Firkant

    Nye egenskaper
      helsetilstand: farge
      antall dager som smittet/syk: dag
      sannsynlighet for å dø når man er syk: dod_prosent (float)
      smittet men enda ikke smittsom: nysmittet (True/False) 
      spesialverdi for tegning av spesialutseende på kvadratene: PADDING (luft/diameter)

    Redigert metode:
      tegn: verdi av tilstand påvirker grafikken

    Nye metoder:
      bli_smittet: smitten fra naboer setter seg som farge, telling fra dag 1
      sjekk_tilstand: oppdaterer sykdomsforløp fra smitte dag 2 til frisk eller død
      
  """
  def __init__(self,vindu,x:int,y:int,side:int=15,farge="gray",dag=0,dod_prosent:float=0.01):
    super().__init__(vindu,x,y,side,side,farge)
    self.side = side
    self.dag = dag
    self.dod_prosent = dod_prosent
    self.nysmittet = False
    self.PADDING = 4

  def __str__(self):
    return super().__str__() + f"\nDag: {self.dag}\nNysmittet: {self.nysmittet}"

  def bli_smittet(self):
    # Gjelder bare når frisk uten immunitet: farge == gray
    # Gjelder for de som har blitt smittet etter forrige oppdatering (dag)
    # nysmittet == True
    if self.farge == "gray"and self.nysmittet:
      self.farge = "pink"
      self.dag = 1 # starter tellingen
  
  def sjekk_tilstand(self):
    # Gjelder bare når smittet eller syk: farge = pink / red
    # Kjøres FØR oppdatering av ny smitte (bli_smittet()), 
    # slik at tilstand bare endres
    # for de som har vært smittet minst 1 dag
    if self.farge == "pink" or self.farge == "red":
      self.dag += 1 # tiden går

    if self.farge == "pink" and self.dag > 3:
      self.farge = "red"
      self.dag = 1
    elif self.farge == "red" and self.dag in [2,3,4]:
      if rd.random() < self.dod_prosent:
        self.farge = "black"
    elif self.farge == "red" and self.dag > 4:
      if rd.random() < self.dod_prosent:
        self.farge = "black"
      else:
        self.farge = "darkgray"

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
      
      # Spesialkode for Person-klassen:
      if self.farge == "pink":
        pg.draw.line(self.vindu,"black",(self.x+self.PADDING-1,self.y+self.PADDING),(self.x+self.side-self.PADDING-1,self.y+self.side-self.PADDING),width=2)
      elif self.farge == "red":
        pg.draw.line(self.vindu,"black",(self.x+self.side-self.PADDING-1,self.y+self.PADDING),(self.x+self.PADDING-1,self.y+self.side-self.PADDING),width=2)
      elif self.farge == "black":
        pg.draw.circle(self.vindu,"white",(self.x+self.side/2,self.y+self.side/2),self.PADDING/2)
      elif self.farge == "darkgray":
        pg.draw.circle(self.vindu,"black",(self.x+self.side/2,self.y+self.side/2),self.PADDING/2)
    else:
      # tegn omriss
      if farge == "":
        # hvis angitt farge mangler, så settes det til svart omriss
        farge = "black"
      pg.draw.rect(self.vindu, farge, self.obj, bredde, radius)





class Populasjon:
  """
  Populasjonen inneholder en kvadratisk 2D-liste med Personer

    Egenskaper:
      posisjon: (origox,origoy) plassering av rutenettet
      befolkningens størrelse: antallx * antally 
      befolkning: liste med Personer

    Metoder:
      skap_ny_befolkning: sett personer inn i lista befolkning, alle er friske uten immunitet
      smitt_naboer: sjekk om smittet/syk har friske naboer å smitte
      oppdater_tilstand: følg sykdomsforløpet dag for dag
      smitten_tar_tak: smitten fester seg i nysmittede fra befolkningen
  """
  def __init__(self,vindu,antall:int=48):
    self.vindu = vindu
    self.antall = antall
    self.befolkning = []
    self.smitte_prosent = 0.3

  def skap_ny_befolkning(self):
    person_side = round(self.vindu.get_width()/self.antall)
    for i in range(self.antall): # rader
      self.befolkning.append([])
      for j in range(self.antall): # kolonner
        self.befolkning[i].append(Person(self.vindu,j*person_side,i*person_side,person_side))

  def smitt_naboer(self):
    for i in range(self.antall):
      for j in range(self.antall):
        if self.befolkning[i][j].farge == "pink" or self.befolkning[i][j].farge == "red":
          # personen over
          if i > 0 and rd.random() < self.smitte_prosent:
            if self.befolkning[i-1][j].farge == "gray":
              self.befolkning[i-1][j].nysmittet = True
          # personen til høyre
          if j < self.antall - 1 and rd.random() < self.smitte_prosent:
            if self.befolkning[i][j+1].farge == "gray":
              self.befolkning[i][j+1].nysmittet = True
          # personen under
          if i < self.antall - 1 and rd.random() < self.smitte_prosent:
            if self.befolkning[i+1][j].farge == "gray":
              self.befolkning[i+1][j].nysmittet = True
          # personen til venstre
          if j > 0 and rd.random() < self.smitte_prosent:
            if self.befolkning[i][j-1].farge == "gray":
              self.befolkning[i][j-1].nysmittet = True

  def oppdater_tilstand(self):
    for i in range(self.antall):
      for j in range(self.antall):
        self.befolkning[i][j].sjekk_tilstand()

  def smitten_tar_tak(self):
    for i in range(self.antall):
      for j in range(self.antall):
        self.befolkning[i][j].bli_smittet()