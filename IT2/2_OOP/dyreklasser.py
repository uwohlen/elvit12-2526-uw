class Dyr:
  """
  Klasse for å lage dyr
  Parametre:
    navn (str): Dyrets personlige navn
    rase (str): Dyrets rase
    farge (str): Dyrets farge
    hale="Lang" (str): Beskrivelse av dyrets hale

  Intern variabel
    alder=0 (int): Dyrets alder i antall år. Endres med metoden aldring()

  Klassevariabel
    dyr_nr (int): Unikt identitetsnummer for hvert dyr
  """
  dyr_nr = 0                    # verdien 0 vil ikke bli brukt
  
  def __init__(self,navn:str,rase:str,farge:str,hale:str="Lang"):
    """
    Konstruktør
    """
    self.navn = navn
    self.rase = rase
    self.farge = farge
    self.hale = hale
    self.alder = 0
    self.barn = []
    Dyr.dyr_nr += 1             # starter med å endre verdien, så alle blir unike
    self.dyr_nr = Dyr.dyr_nr    # legger variabelen til alle nye dyreobjekter når de opprettes

  def __str__(self):            # slipper å skrive et metodenavn for standard utskrift
    """
    Metode for utskrift
    """
    tekst = f"{self.dyr_nr}: {self.navn} er en {self.farge.lower()} {self.rase.lower()}"
    if (self.barn != []):       # skrives bare ut hvis den har verdier
      tekst += f", avkom: {self.barn}"
    try:                        # skrives bare ut hvis den har verdier
      tekst += f", mor: {self.mor.navn}"
    except:
      pass
    try:                        # skrives bare ut hvis den har verdier
      tekst += f", far: {self.far.navn}"
    except:
      pass
    return tekst
  
  def __add__(self,dyr2):       # hva skjer om man skriver dyr3 = dyr1 + dyr2
    """
    Lage avkom fra foreldredyrene
    """
    navn = "Nytt dyr"           # dyret må få nytt navn, finnes ikke i dyr1 og dyr2
    if self.rase == dyr2.rase:  # renraset eller blandingsrase?
      rase = self.rase
    else:
      rase = "Blanding av " + self.rase.lower() + " og " + dyr2.rase.lower()
    if self.farge == dyr2.farge:  # samme farge eller blandingsfarge? 
      farge = self.farge
    else:
      farge = self.farge + ", " + dyr2.farge.lower()
    return Dyr(navn,rase,farge) # lag et nytt objekt med disse verdiene basert på dyr1 og dyr2

  def aldring(self,antall:int=1):
    """
    Metode for å øke dyrets alder med et gitt antall år
    Parametre:
      antall (int): Antall år som har gått siden siste oppdatering
    Output:
      Skriver ut ny beregnet alder
    """
    self.alder += antall
    print(f"{self.navn} er nå {self.alder} år")

  def avkom(self,barnenavn:str):
    """
    Metode for å legge til et barn i en liste
    Parametre:
      barnenavn(str): Navnet på barnet
    Output:
      Skriver ut listen med barn
    """
    self.barn.append(barnenavn)
    
  def sett_mor(self,dyreobjekt:object):
    """
    Metode for å legge til foreldre - mor
    Parametre:
      dyreobjekt: objektvariabel av klassen Dyr eller underklasser
    """
    self.mor = dyreobjekt

  def sett_far(self,dyreobjekt:object):
      """
      Metode for å legge til foreldre - far
      Parametre:
        dyreobjekt: objektvariabel av klassen Dyr eller underklasser
      """
      self.far = dyreobjekt


class Katt(Dyr):
  """
  Klasse for å lage katter
  Parametre:
    navn (str): Kattens personlige navn
    rase (str): Kattens rase
    farge (str): Kattens farge
    hale="Lang" (str): Beskrivelse av kattens hale
    liv=0 (int): Antall liv katten har brukt (av 9). Endres med metoden antall_liv()

  Intern variabel
    alder=0 (int): Kattens alder i antall år. Endres med metoden aldring()
  """ 
  def __init__(self,navn,rase,farge,hale="Lang",liv=0):
    """
    Konstruktør
    """
    super().__init__(navn,rase,farge,hale)
    self.liv = liv    

  def __str__(self):        # bruker __str__() fra Dyr-klassen, med et tillegg for attributten liv
    """
    Metode for utskrift
    """
    return super().__str__() + f", antall liv brukt: {self.liv}"                 
  
  def snakk(self):
    """
    Metode for at katten snakker
    Output:
      Skriver ut at katten sier Mjau
    """
    print(f'{self.navn} sier "Mjau"')

  def antall_liv(self):
    """
    Metode for å øke antall brukte liv med 1.
    Output:
      Skriver ut hvor mange liv som er brukt. Eller at det er alle hvis antallet er 9 eller mer.
    """
    self.liv += 1
    if self.liv >= 9:
      print(f"{self.navn} har nå brukt alle sine liv :(")
    else:
      print(f"{self.navn} har nå brukt {self.liv} liv.")


class Hund(Dyr):
  """
  Klasse for å lage hunder
  Parametre:
    navn (str): Hundens personlige navn
    rase (str): Hundens rase
    farge (str): Hundens farge
    hale="Lang" (str): Beskrivelse av hundens hale

  Intern variabel
    alder=0 (int): Hundens alder i antall år. Endres med metoden aldring()
  """ 
  def __init__(self,navn,rase,farge,hale="Lang"):
    """
    Konstruktør
    """
    super().__init__(navn,rase,farge,hale)
  
  def snakk(self):
    """
    Metode for at hunden snakker
    Output:
      Skriver ut at hunden sier Voff
    """
    print(f'{self.navn} sier "Voff"')


