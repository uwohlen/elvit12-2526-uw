import pygame as pg
import random as rd

class Firkant:
  """
  Firkanter blir objekter og kan tegnes
  Klasse jeg lagde da jeg øvde på eksamen V24 oppgave 10, men tegn-funksjonen er utvidet

    Egenskaper
      vindu (Surface):      spillets vindu
      x, y (int):           plassering i vindu
      bredde, høyde (int):  størrelse på firkanten
      farge (str):          fargekode eller fargenavn
      obj (Rect):           objekt for interaksjon, f.eks. kollisjoner

    Metoder
      tegn: None            tegner firkanten i vinduet 
      __str__: str          for utskrift av sentrale egenskaper

  """
  def __init__(self,vindu:pg.surface.Surface,x:int,y:int,bredde:int,hoyde:int,farge:str) -> None:
    self.vindu = vindu
    self.x = x
    self.y = y
    self.bredde = bredde
    self.hoyde = hoyde
    self.farge = farge
    self.obj:pg.rect.Rect = pg.Rect(self.x, self.y, self.bredde, self.hoyde)

  def tegn(self,bredde:int=0,farge:str="",radius:int=-1) -> None:
    """
    Tegner firkanten i vinduet

      bredde (int):   angis om det er kantstrek (default svart), ellers blir det heldekkende farge
      farge (str):    kan angi nye farger, fargekode eller fargenavn
      radius (int):   kan angi runde hjørner
    """
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
      

  def __str__(self) -> str:
    return f"Posisjon: ({self.x},{self.y})\nStørrelse: ({self.bredde},{self.hoyde})\nFarge: {self.farge}"


class Person(Firkant):
  """
  Personer er kvadrater med varierende grafikk, 
           arver fra klassen Firkant

    Nye definisjoner av egenskaper
      side (int):           både bredde og høyde av kvadratene
      farge (str):          helsetilstand
      dag (int):            antall dager som smittet eller antall dager som syk
      dod_prosent (float):  sannsynlighet for å dø når man er syk
      nysmittet (bool)      smittet men enda ikke smittsom
      PADDING (int):        spesialverdi for tegning av spesialutseende på kvadratene (luft og diameter)

    Redigert metode:
      tegn: None            verdi av tilstand påvirker grafikken

    Nye metoder:
      bli_smittet: None     smitten fra naboer setter seg som farge, telling fra dag 1
      sjekk_tilstand: None  oppdaterer sykdomsforløp fra smitte dag 2 til frisk eller død
      
  """
  def __init__(self,vindu:pg.surface.Surface,x:int,y:int,side:int=15,farge:str="gray",dag:int=0,dod_prosent:float=0.01) -> None:
    super().__init__(vindu,x,y,side,side,farge)
    self.side = side
    self.dag = dag
    self.dod_prosent = dod_prosent
    self.nysmittet:bool = False
    self.PADDING:int = 4

  def __str__(self) -> str:
    return super().__str__() + f"\nDag: {self.dag}\nNysmittet: {self.nysmittet}"

  
  def sjekk_tilstand(self) -> None:
    """
    Utviklingen av sykdomsforløpet
      Dagene øker med 1
      Smitte kan utvikles til sykdom
      Sykdom kan utvikles til frisk eller død
      Bare avhengig av seg selv, ikke personene rundt
    """
    # Gjelder bare når smittet eller syk: farge = pink / red
    # Kjøres FØR oppdatering av ny smitte (bli_smittet()), 
    # slik at tilstand bare endres
    # for de som har vært smittet minst 1 dag
    if self.nysmittet:
      self.farge = "pink"
      self.nysmittet = False
    elif self.farge == "pink" or self.farge == "red":
      self.dag += 1 # tiden går, hva er tilstanden neste dag?

    # smittet i 3 dager blir syk
    if self.farge == "pink" and self.dag > 3:
      self.farge = "red"
      self.dag = 1
    # syk kan dø
    elif self.farge == "red" and self.dag in [2,3,4]:
      if rd.random() < self.dod_prosent:
        self.farge = "black"
    # syk i 4 dager blir frisk (eller død)
    elif self.farge == "red" and self.dag > 4:
      if rd.random() < self.dod_prosent:
        self.farge = "black"
      else:
        self.farge = "darkgray"

  def tegn(self,bredde:int=0,farge="",radius:int=-1) -> None:
    """
    Tegner firkanten i vinduet

      bredde (int):   angis om det er kantstrek (default svart), ellers blir det heldekkende farge
      farge (str):    kan angi nye farger, fargekode eller fargenavn
      radius (int):   kan angi runde hjørner
    
    """
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
      # slutt på spesialkode for Person-klassen
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
      vindu (Surface):            spillets vindu
      antall (int):               bredden av rutenettet, befolkningens størrelse er antall ** 2 
      befolkning (list[Person]):  2D-liste med firkanter av klassen Person
      smitte_prosent (float):     sannsynlighet for at en smittet eller syk person smitter en frisk nabo uten immunitet

    Metoder:
      skap_ny_befolkning: None    sett personer inn i lista befolkning, alle er friske uten immunitet
      smitt_naboer: None          sjekk om smittet/syk har friske naboer å smitte
      oppdater_tilstand: None     følg sykdomsforløpet dag for dag
      smitten_tar_tak: None       smitten fester seg i nysmittede fra befolkningen
  """
  def __init__(self,vindu:pg.surface.Surface,antall:int=48) -> None:
    self.vindu = vindu
    self.antall = antall
    self.befolkning:list[Person] = []
    self.smitte_prosent:float = 0.3

  def skap_ny_befolkning(self) -> None:
    """
    Sett personer inn i lista befolkning
      alle er friske uten immunitet, bruker default-verdier fra Person-klassen
    """
    # rutestørrelse gitt av vindu-størrelse og antall ruter i bredden
    person_side = round(self.vindu.get_width()/self.antall)
    for i in range(self.antall): # rader
      self.befolkning.append([])
      for j in range(self.antall): # kolonner
        self.befolkning[i].append(Person(self.vindu,j*person_side,i*person_side,person_side))

  def smitt_naboer(self) -> None:
    """
    Sjekk om smittet/syk har friske naboer å smitte
      Marker naboer som smittet, uten at de kan smitte andre samme dag
      Smitte er avhengig av sannsynlighet, rd.random() gir et tall mellom 0 og 1
      Personer i kanten av rutenettet kan ikke smitte noen utenfor rutenettet
    """
    # for hver person
    for i in range(self.antall):
      for j in range(self.antall):
        # hvis jeg selv er syk
        if self.befolkning[i][j].farge == "pink" or self.befolkning[i][j].farge == "red" or self.befolkning[i][j].nysmittet:
          # smitter jeg personen over?
          if i > 0 and rd.random() < self.smitte_prosent:
            if self.befolkning[i-1][j].farge == "gray":
              self.befolkning[i-1][j].nysmittet = True
              self.befolkning[i-1][j].dag += 1
          # smitter jeg personen til høyre?
          if j < self.antall - 1 and rd.random() < self.smitte_prosent:
            if self.befolkning[i][j+1].farge == "gray":
              self.befolkning[i][j+1].nysmittet = True
              self.befolkning[i][j+1].dag += 1
          # smitter jeg personen under?
          if i < self.antall - 1 and rd.random() < self.smitte_prosent:
            if self.befolkning[i+1][j].farge == "gray":
              self.befolkning[i+1][j].nysmittet = True
              self.befolkning[i+1][j].dag += 1
          # smitter jeg personen til venstre?
          if j > 0 and rd.random() < self.smitte_prosent:
            if self.befolkning[i][j-1].farge == "gray":
              self.befolkning[i][j-1].nysmittet = True
              self.befolkning[i][j-1].dag += 1
          
  def oppdater_tilstand(self) -> None:
    """
    Følg sykdomsforløpet dag for dag
      Gå gjennom hver person i befolkningen
      Kjør metoden sjekk_tilstand fra Person-klassen
    """
    for i in range(self.antall):
      for j in range(self.antall):
        self.befolkning[i][j].sjekk_tilstand()

  def smitten_tar_tak(self) -> None:
    """
    Smitten fester seg i nysmittede fra befolkningen
      Gå gjennom hver person i befolkningen
      Nye personer blir smittsomme
      Kjøres etter at personer har blitt smittet fra sine naboer
    """
    for i in range(self.antall):
      for j in range(self.antall):
        self.befolkning[i][j].bli_smittet()