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
      tegn3D: None          tegner kvadrater i vinduet, med 2 ulike farger på kanten for 3D-effekt
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
  

  def tegn3D(self,nedre:str,ovre:str,hoved:str="",kant:int=4) -> None:
    """
    Tegn firkanten med en 3D-effekt, kun for kvadrater
    
      nedre (str): farge nede til høyre
      ovre (str):  farge øverst til venstre
      hoved (str): hovedfargen på knappen
      kant (int):  bredden på 3D-kanten

      NB! Inneholder manuell finjustering på pikselnivå, draw.rect og draw.polygon regner bredde ulikt
    """
    if hoved == "":
      hoved = self.farge
    pg.draw.rect(self.vindu,nedre,(self.x,self.y,self.bredde,self.hoyde)) # hele firkanten
    pg.draw.polygon(self.vindu,ovre,((self.x,self.y),(self.x+self.bredde-1,self.y),(self.x,self.y+self.hoyde-1))) # øverste triangel
    pg.draw.rect(self.vindu,hoved,(self.x+kant,self.y+kant,self.bredde-2*kant,self.hoyde-2*kant)) # mindre firkant foran


  def __str__(self) -> str:
    return f"Posisjon: ({self.x},{self.y})\nStørrelse: ({self.bredde},{self.hoyde})\nFarge: {self.farge}"






class Knapp(Firkant):
  """
  Knapper er firkanter med tekst, 
          arver fra klassen Firkant
  Klasse jeg lagde da jeg øvde på eksamen H24 oppgave 9
  Endret til å passe til Minesveiper
  Teksten har blitt til tall

    Nye egenskaper
      tekst(int):                 antall miner
      font (Font):                font brukt på knappen
      mine (bool):                om firkanten skjuler en mine
      visning (bool):             om firkanten har blitt trykket på
      status ("" / "mine" / "?"): markering av rute for antatt mine ved høyreklikk (to fingre på touchpad på laptop)

    Nye metoder:
      vis_tekst: None             setter teksten på midten av knappen

  """
  def __init__(self,vindu:pg.surface.Surface,x:int,y:int,bredde:int,hoyde:int,farge:str,font:pg.font.Font,tekst:int=0) -> None:
    super().__init__(vindu,x,y,bredde,hoyde,farge)
    self.tekst = tekst
    self.font = font
    self.mine:bool = False
    self.visning:bool = False
    self.status:str = ""

  def __str__(self) -> str:
    return super().__str__() + f"\nTekst: {str(self.tekst)}\nMine: {str(self.mine)}\nVisning: {str(self.visning)}\nStatus: {self.status}"

  def vis_tekst(self,farge:str="black",tekst:str="") -> None:
    """
    Setter teksten midt på knappen

      farge (str): om teksten skal ha en annen farge enn svart
      tekst (str): om man skal skrive noe annet enn knappens egen tekst

    """
    # Lag teksten
    if tekst == "":
      knapp_tekst = self.font.render(str(self.tekst),True, farge)
    else:
      knapp_tekst = self.font.render(str(tekst),True, farge)
    
    # Finn luften rundt teksten
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
      ruter (list[Knapp]):      2D-liste med ruter av klassen Knapp
      vist (int):               antall ruter uten miner på rutenettet som er vist fram / klikket på
      
    Metoder:
      lag_nytt_rutenett: None   sett knapper inn i lista ruter, alle uten miner
      lag_miner: None           fordel minene utover rutenettet
      tell_nabo_miner: None     sjekk om naborutene har miner
  """
  def __init__(self,vindu:pg.surface.Surface,antall_x:int=9,antall_y:int=9,antall_miner:int=10) -> None:
    self.vindu = vindu
    self.antall_x = antall_x
    self.antall_y = antall_y
    self.antall_miner = antall_miner
    self.ruter:list[Knapp] = []
    self.vist:int = 0

  def lag_nytt_rutenett(self,font:pg.font.Font,farge:str) -> None:
    """
    Danner et 2D rutenett av ruter

      font (Font): Font for tallene som viser hvor mange miner som er i naborutene
      farge (str): firkantenes startfarge
    """
    # x-retningen skal bare ha ruter
    # y-retningen må dyttes ned i forhold til meny-høyden
    # alle knappene er kvadratiske
    rute_side = round(self.vindu.get_width()/self.antall_x)
    origo_y = self.vindu.get_height() - self.antall_y * rute_side
    for i in range(self.antall_y): # rader
      self.ruter.append([])
      for j in range(self.antall_x): # kolonner
        self.ruter[i].append(Knapp(self.vindu,j*rute_side,origo_y + i*rute_side,rute_side,rute_side,farge,font))

  def lag_miner(self) -> None:
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


  def tell_nabo_miner(self) -> None:
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
