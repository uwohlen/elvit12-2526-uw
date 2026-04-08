import pygame as pg

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


class Knapp(Firkant):
  """
  Knapper er firkanter med tekst, 
          arver fra klassen Firkant

    Nye egenskaper
      tekst (str):        tekst som skal stå på knappen
      font (Font):        font brukt på knappen

    Nye metoder:
      vis_tekst: None     setter teksten på knappen, sentrert i høyden

  """
  def __init__(self,vindu:pg.surface.Surface,x:int,y:int,bredde:int,hoyde:int,farge:str,tekst:str,font:pg.font.Font) -> None:
    super().__init__(vindu,x,y,bredde,hoyde,farge)
    self.tekst = tekst
    self.font = font

  def __str__(self) -> str:
    return super().__str__() + f"\nTekst: {self.tekst}"

  def vis_tekst(self,align:str="v") -> None:
    """
    Setter teksten på knappen, sentrert i høyden
      Svart farge
    
      align (str): teksten er venstrestilt (v) eller høyrestilt (h) på knappen
                   NB! brukt i et program med liten plass og lave knapper
                       hardkodet ekstra luft mellom teksten og kanten av knappen i bredden
    """
    # sett teksten sentrert i høyden
    # hvis align = "v": venstrestilt. Ellers høyrestilt.
    knapp_tekst = self.font.render(str(self.tekst),True, "black")
    tekst_hoyde = knapp_tekst.get_height()
    tekst_bredde = knapp_tekst.get_width()
    # luft i høyden bestemt av knappens høyde og tekstens høyde
    forskyvning_y = (self.hoyde - tekst_hoyde)/2
    # luft til venstre settes lik luft i høyden (og litt ekstra)
    if align == "v": # venstrestilt
      forskyvning_x = forskyvning_y + 5 # juster etter behov
    else: # høyrestilt
    # luft til høyre hardkodet inn som tall
      forskyvning_x = self.bredde - tekst_bredde - 5 # juster etter behov
    self.vindu.blit(knapp_tekst,(self.x+forskyvning_x,self.y + forskyvning_y))




class Nedtrekk(Knapp):
  """
  Nedtrekksmeny er en Knapp med en tilhørende liste med Knapper for alternativer
                arver fra klassen Knapp

    Nye egenskaper
      alternativer (list[str]): liste med alternativer for nedtrekksmenyen
      alt_farge (str):          farge til bruk på alternativene
      vis (bool):               visning av alternativene på/av
                                alternativene kan trykkes på når vis er True
      alt_obj (list[Knapp]):    liste med objekter for alternativene

    Nye metoder
      lag_alt_obj: None         fyll listen alt_obj med objekter for alternativene

  """
  def __init__(self,vindu:pg.surface.Surface,x:int,y:int,bredde:int,hoyde:int,farge:str,tekst:str,font:pg.font.Font,alternativer:list,alt_farge:str,vis:bool=False) -> None:
    super().__init__(vindu,x,y,bredde,hoyde,farge,tekst,font)
    self.alternativer = alternativer
    self.alt_farge = alt_farge
    self.vis = vis
    self.alt_obj:list[Knapp] = [] 
  
  def __str__(self) -> str:
    return super().__str__() + f"\nAlternativer: {self.alternativer}\nFarge: {self.alt_farge}"

  def lag_alt_obj(self,bredde:int,hoyde:int,font:pg.font.Font,skift:int=0) -> None:
    """
    Fyll listen alt_obj med objekter for alternativene
              
      Ting som kan være annerledes enn hovedknappen:
          bredde, hoyde (int):  størrelse på nedtrekksalternativene
          font (Font):          om alternativene skal ha en annen (mindre) font
          skift (int):          antall alternativer i høyden 
                                lager flere kolonner med alternativer

    """
    # lag liste med objekter, ett objekt for hvert alternativ
    skift_x = 0
    skift_y = 0
    for i in range(len(self.alternativer)):
      # Alle nedover
      if skift == 0:
        self.alt_obj.append(Knapp(self.vindu,self.x,self.y+self.hoyde+i*hoyde,bredde,hoyde,self.alt_farge,self.alternativer[i],font))
      else:
        # Skifter til ny kolonne etter verdien på skift
        self.alt_obj.append(Knapp(self.vindu,self.x+skift_x*bredde,self.y+self.hoyde+skift_y*hoyde,bredde,hoyde,self.alt_farge,self.alternativer[i],font))
        skift_y += 1
        if skift_y % skift == 0:
          skift_x += 1
          skift_y = 0

