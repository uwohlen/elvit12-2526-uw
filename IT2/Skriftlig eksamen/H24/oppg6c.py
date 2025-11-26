class Batteri:
  """
  Opprett objekter med nåværende energinivå og batteriets kapasitet
  Batteriene får en unik ID

  Bruk følgende metoder:
    ladOpp(energi:float) -> None
    brukEnergi(energi:float) -> None
    visEnerginivå() -> float 
  """
  batteriID_nr = 0
  def __init__(self,energinivå:float, energikapasitet:float) -> None:
    """
    Konstruktøren
      Parametre
        energinivå: float - nåværende energinivå, oppdateres og vises ved metoder
        energikapasitet: float - maks energinivå, endres ikke, maks verdi 100 (%)

      Feil bruk resulterer i en print-melding
        må angi parametre som desimaltall, verdier 0-100
    """
    Batteri.batteriID_nr += 1
    self.__batteriID:str = "B" + str(Batteri.batteriID_nr)
    try:
      niva = float(energinivå)
    except:
      niva = 0
      print("Energinivået var ikke angitt som et tall, så lagret energinivå er satt til 0")
    try:
      kapasitet = float(energikapasitet)
    except:
      kapasitet = 100
      print("Energikapasiteten var ikke angitt som et tall, så lagret kapasitet er satt til 100")
    
    if kapasitet < 0:
      kapasitet = 0
      print("Energikapasiteten var angitt som et negativt tall, så lagret kapasitet er satt til 0")
    elif kapasitet > 100:
      kapasitet = 100
      print("Energikapasiteten var angitt som større enn 100, så lagret kapasitet er satt til 100")
    
    if niva < 0:
      niva = 0
      print("Energinivået var angitt som et negativt tall, så lagret energi er satt til 0")
    elif niva > kapasitet:
      niva = kapasitet
      print("Energinivået var angitt som større enn kapasiteten, så lagret energi er satt til kapasiteten")

    self.__energiniva = niva
    self.__energikapasitet = kapasitet


  def ladOpp(self, energi:float) -> None:
    """
    Endre energinivået opp
      Parametre
        energi: float - energimengden som batteriet lades med

      Feil bruk resulterer i en print-melding
        må angi energi som positivt tall som ikke bringer en over kapasiteten
    """
    try:
      en = float(energi)
      
      if en < 0:
        print("Ladingen var angitt som et negativt tall, så lagret energinivå ble ikke oppdatert")
      else:
        total = self.__energiniva + en
        if total > self.__energikapasitet:
          self.__energiniva = self.__energikapasitet
          print("Angitt lading ville oversteget kapasiteten til batteriet, så lagret energinivå ble likt kapasiteten")
        else:
          self.__energiniva = total
    except:
      print("Ladingen var ikke angitt som et tall, så lagret energinivå ble ikke oppdatert")
    
  def brukEnergi(self, energi:float) -> None:
    """
    Endre energinivået ned
      Parametre
        energi: float - energimengden som batteriet tappes med

      Feil bruk resulterer i en print-melding
    """
    try:
      en = float(energi)
      
      if en < 0:
        print("Energibruken var angitt som et negativt tall, så lagret energinivå ble ikke oppdatert")
      else:
        total = self.__energiniva - en
        if total < 0:
          self.__energiniva = 0
          print("Angitt energibruk er større en batteriets gjenværende energi, så lagret energinivå ble 0")
        else:
          self.__energiniva = total
    except:
      print("Energibruken var ikke angitt som et tall, så lagret energinivå ble ikke oppdatert")

  def visEnerginivå(self) -> float:
    """
    Vis nåværende energinivå
    """
    return self.__energiniva
  
  def __str__(self) -> str:
    """
    Returnerer en tekst-streng som blir brukt ved print(objekt)
    """
    return f"Batteri ID {self.__batteriID}: Nivå: {self.__energiniva} Kapasitet: {self.__energikapasitet}"

