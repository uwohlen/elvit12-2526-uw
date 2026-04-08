import pygame as pg
import random as rd


VINDU_BREDDE = 720
VINDU_HOYDE = 720
PERSON_BREDDE = 15
PERSON_HOYDE = 15
ANTALL_X = round(VINDU_BREDDE / PERSON_BREDDE)
ANTALL_Y = round(VINDU_HOYDE / PERSON_HOYDE)
SANNSYNLIG_DOD = 0.01
SANNSYNLIG_SMITTE = 0.3
PADDING = 4


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


class Person(Firkant):
  """
  Personer er firkanter med varierende grafikk, arver fra klassen Firkant

    Nye egenskaper
      helsetilstand: farge
      antall dager som smittet/syk: dag
      nysmittet: True/False

    Redigert metode:
      tegn: verdi av tilstand påvirker grafikken

    Nye metoder:
      bli_smittet: smitten fra naboer setter seg som farge, telling fra dag 1
      sjekk_tilstand: oppdaterer sykdomsforløp fra smitte dag 2 til frisk eller død
      
  """
  def __init__(self,vindu,x:int,y:int,bredde:int=PERSON_BREDDE,hoyde:int=PERSON_HOYDE,farge="gray",dag=0):
    super().__init__(vindu,x,y,bredde,hoyde,farge)
    self.dag = dag
    self.nysmittet = False
    self.dod_prosent = SANNSYNLIG_DOD

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
        self.farge = "dimgray"

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
        pg.draw.line(self.vindu,"black",(self.x+PADDING-1,self.y+PADDING),(self.x+PERSON_BREDDE-PADDING-1,self.y+PERSON_HOYDE-PADDING),width=2)
      elif self.farge == "red":
        pg.draw.line(self.vindu,"black",(self.x+PERSON_BREDDE-PADDING-1,self.y+PADDING),(self.x+PADDING-1,self.y+PERSON_HOYDE-PADDING),width=2)
      elif self.farge == "black":
        pg.draw.circle(self.vindu,"white",(self.x+PERSON_BREDDE/2,self.y+PERSON_HOYDE/2),PADDING/2)
      elif self.farge == "dimgray":
        pg.draw.circle(self.vindu,"black",(self.x+PERSON_BREDDE/2,self.y+PERSON_HOYDE/2),PADDING/2)
    else:
      # tegn omriss
      if farge == "":
        # hvis angitt farge mangler, så settes det til svart omriss
        farge = "black"
      pg.draw.rect(self.vindu, farge, self.obj, bredde, radius)





class Populasjon:
  """
  Populasjonen inneholder en 2D-liste med Personer

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
  def __init__(self,vindu,antallx=ANTALL_X,antally=ANTALL_Y,origox=0,origoy=0):
    self.vindu = vindu
    self.antallx = antallx
    self.antally = antally
    self.origox = origox
    self.origoy = origoy
    self.befolkning = []
    self.smitte_prosent = SANNSYNLIG_SMITTE

  def skap_ny_befolkning(self):
    for i in range(self.antally): # rader
      self.befolkning.append([])
      for j in range(self.antallx): # kolonner
        self.befolkning[i].append(Person(self.vindu,self.origox+j*PERSON_BREDDE,self.origoy+i*PERSON_HOYDE,PERSON_BREDDE,PERSON_HOYDE))

  def smitt_naboer(self):
    for i in range(self.antally):
      for j in range(self.antallx):
        if self.befolkning[i][j].farge == "pink" or self.befolkning[i][j].farge == "red":
          # personen over
          if i > 0 and rd.random() < self.smitte_prosent:
            if self.befolkning[i-1][j].farge == "gray":
              self.befolkning[i-1][j].nysmittet = True
          # personen til høyre
          if j < self.antallx - 1 and rd.random() < self.smitte_prosent:
            if self.befolkning[i][j+1].farge == "gray":
              self.befolkning[i][j+1].nysmittet = True
          # personen under
          if i < self.antally - 1 and rd.random() < self.smitte_prosent:
            if self.befolkning[i+1][j].farge == "gray":
              self.befolkning[i+1][j].nysmittet = True
          # personen til venstre
          if j > 0 and rd.random() < self.smitte_prosent:
            if self.befolkning[i][j-1].farge == "gray":
              self.befolkning[i][j-1].nysmittet = True

  def oppdater_tilstand(self):
    for i in range(self.antally):
      for j in range(self.antallx):
        self.befolkning[i][j].sjekk_tilstand()

  def smitten_tar_tak(self):
    for i in range(self.antally):
      for j in range(self.antallx):
        self.befolkning[i][j].bli_smittet()