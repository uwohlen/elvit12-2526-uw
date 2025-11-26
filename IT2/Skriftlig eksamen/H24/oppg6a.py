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
        energikapasitet: float - maks energinivå, endres ikke
    """
    Batteri.batteriID_nr += 1
    self.__batteriID:str = "B" + str(Batteri.batteriID_nr)
    self.__energinivaa = energinivå
    self.__energikapasitet = energikapasitet

  def ladOpp(self, energi:float) -> None:
    """
    Endre energinivået opp
      Parametre
        energi: float - energimengden som batteriet lades med
    """
    self.__energinivaa += energi

  def brukEnergi(self, energi:float) -> None:
    """
    Endre energinivået ned
      Parametre
        energi: float - energimengden som batteriet tappes med
    """
    self.__energinivaa -= energi

  def visEnerginivå(self) -> float:
    """
    Vis nåværende energinivå
    """
    return self.__energinivaa
  


