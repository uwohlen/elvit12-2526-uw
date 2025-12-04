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
      farge:                fargekode eller fargenavn
      objekt:               obj (Rect)

    Metoder
      tegn:                 tegner firkanten i vinduet 
      
      __str__:              for utskrift av sentrale egenskaper
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
    """
    Tegner firkanten i vinduet

      bredde (int):   angis om det er kantstrek, ellers blir det heldekkende farge
      farge:          kan angi nye farger, fargekode eller fargenavn
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
      

  def __str__(self):
    return f"Posisjon: ({self.x},{self.y})\nStørrelse: ({self.bredde},{self.hoyde})\nFarge: {self.farge}"


class Knapp(Firkant):
  """
  Knapper er firkanter med tekst, arver fra klassen Firkant
  Klasse jeg lagde da jeg øvde på eksamen H24 oppgave 9
  Endret til å passe til Minesveiper
  Teksten har blitt til tall

    Nye egenskaper
      tekst(int):           antall miner
      font
      mine (True/False):    om firkanten skjuler en mine
      visning (True/False): om firkanten har blitt trykket på

    Nye metoder:
      vis_tekst:            setter teksten på midten av knappen

  """
  def __init__(self,vindu,x:int,y:int,bredde:int,hoyde:int,farge,font,tekst:int=0):
    super().__init__(vindu,x,y,bredde,hoyde,farge)
    self.tekst = tekst
    self.font = font
    self.mine = False
    self.visning = False

  def __str__(self):
    return super().__str__() + f"\nTekst: {str(self.tekst)}\nMine: {str(self.mine)}\nVisning: {str(self.visning)}"

  def vis_tekst(self,farge="black"):
    """
    Setter teksten midt på knappen

      farge: om teksten skal ha en annen farge enn svart
    """
    knapp_tekst = self.font.render(str(self.tekst),True, farge)
    tekst_hoyde = knapp_tekst.get_height()
    tekst_bredde = knapp_tekst.get_width()
    forskyvning_y = (self.hoyde - tekst_hoyde)/2
    forskyvning_x = (self.bredde - tekst_bredde)/2
    self.vindu.blit(knapp_tekst,(self.x+forskyvning_x,self.y + forskyvning_y))




class Rutenett:
  """
  Rutenettet inneholder en 2D-liste med knapper
  Klasse jeg lagde da jeg øvde på eksamen H24 oppgave 10 (Populasjon)
  Endret til å passe til Minesveiper

    Egenskaper:
      vindu (Surface):          spillets vindu
      antall_x, antall_y (int): rutenettets bredde og høyde
      antall_miner (int):       antall miner som skal gjemmes i rutenettet
      ruter (list(Knapp)):      2D-liste med ruter av klassen Knapp
      vist (int):               antall ruter uten miner på rutenettet som er vist fram
      
    Metoder:
      lag_nytt_rutenett:        sett knapper inn i lista ruter, alle uten miner
      lag_miner:                fordel minene utover rutenettet
      tell_nabo_miner:          sjekk om naborutene har miner
  """
  def __init__(self,vindu,antall_x:int=9,antall_y:int=9,antall_miner=10):
    self.vindu = vindu
    self.antall_x = antall_x
    self.antall_y = antall_y
    self.antall_miner = antall_miner
    self.ruter = []
    self.vist = 0

  def lag_nytt_rutenett(self,font,farge):
    """
    Danner et 2D rutenett av ruter

      font
      farge: firkantens startfarge
    """
    rute_bredde = round(self.vindu.get_width()/self.antall_x)
    rute_hoyde = round(self.vindu.get_height()/self.antall_y)
    for i in range(self.antall_y): # rader
      self.ruter.append([])
      for j in range(self.antall_x): # kolonner
        self.ruter[i].append(Knapp(self.vindu,j*rute_bredde,i*rute_hoyde,rute_bredde,rute_hoyde,farge,font))

  def lag_miner(self):
    """
    Velger tilfeldige tall i forhold til rutenettets størrelse
    Sjekker at vi ikke velger samme rute om igjen
    Plasserer minen i forhold til rad og kolonne i rutenettet
    """
    verdier = self.antall_x * self.antall_y # antall ruter
    valgte = []
    while len(valgte) < self.antall_miner: # holder på til vi har nok miner
      valg = rd.randint(0,verdier-1) # alle ruter nummerert mellom 0 og verdier-1
      if valg not in valgte: # legg til hvis den ikke er valgt før
        valgte.append(valg)
    for verdi in valgte:
      # Når hver rute er nummerert fra 0 til x*y-1
      # finn rad og kolonne for hvert nummer
      rad = verdi // self.antall_x  # heltallsdivisjon
      kol = verdi % self.antall_x   # modulus, rest etter heltallsdivisjon
      #print(verdi,rad,kol)
      self.ruter[rad][kol].mine = True


  def tell_nabo_miner(self):
    """
    Går gjennom rutenettet og teller antall miner rundt hver rute
      Hopper over ruter som har mine, siden de ikke skal oppgi antall
    """
    for i in range(self.antall_y):
      for j in range(self.antall_x):
        # Teller hvor mange miner som ligger rundt hver rute
        # Trenger ikke sjekke feltene som har en mine selv
        if self.ruter[i][j].mine == False:
          # er det en mine over?
          if i > 0:
            if self.ruter[i-1][j].mine:
              self.ruter[i][j].tekst += 1
          # er det en mine til høyre?
          if j < self.antall_x - 1:
            if self.ruter[i][j+1].mine:
              self.ruter[i][j].tekst += 1
          # er det en mine under?
          if i < self.antall_y - 1:
            if self.ruter[i+1][j].mine:
              self.ruter[i][j].tekst += 1
          # er det en mine til venstre?
          if j > 0:
            if self.ruter[i][j-1].mine:
              self.ruter[i][j].tekst += 1
          # er det en mine over til venstre?
          if i > 0 and j > 0:
            if self.ruter[i-1][j-1].mine:
              self.ruter[i][j].tekst += 1
          # er det en mine over til høyre?
          if i > 0 and j < self.antall_x - 1:
            if self.ruter[i-1][j+1].mine:
              self.ruter[i][j].tekst += 1
          # er det en mine under til høyre?
          if i < self.antall_y - 1 and j < self.antall_x - 1:
            if self.ruter[i+1][j+1].mine:
              self.ruter[i][j].tekst += 1
          # er det en mine under til venstre?
          if i < self.antall_y - 1 and j > 0:
            if self.ruter[i+1][j-1].mine:
              self.ruter[i][j].tekst += 1
