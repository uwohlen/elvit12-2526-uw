# Oppgave 6a
class Batteri:
  def __init__(self, batteriID: str, energikapasitet: float):
    self.__batteriID = batteriID
    self.__energikapasitet = energikapasitet
    self.__energimengde = 0.0  # Starter med tomt batteri

  def ladOpp(self, energi: float) -> None:
    """Lader batteriet med en gitt mengde energi."""
    if energi < 0:
      raise ValueError("Energi som lades opp må være positiv.")
    self.__energimengde = min(self.__energimengde + energi, self.__energikapasitet)

  def brukEnergi(self, energi: float) -> None:
    """Bruker en gitt mengde energi fra batteriet."""
    if energi < 0:
      raise ValueError("Energiforbruk må være positivt.")
    if energi > self.__energimengde:
      raise ValueError("Ikke nok energi på batteriet.")
    self.__energimengde -= energi

  def visEnerginivå(self) -> float:
    """Viser hvor mye energi som er igjen i batteriet."""
    return self.__energimengde
  

# Oppgave 6b og c
#from opg6a import Batteri
def testBatteri():
  # Opprett et batteri
  batteri = Batteri("BAT123", 100.0)
 
  # Test lading
  print("Lader batteriet med 50 enheter...")
  batteri.ladOpp(50.0)
  print(f"Energimengde: {batteri.visEnerginivå()} (forventet: 50.0)")
 
  # Test overfylling
  print("Lader batteriet med 60 enheter (over maks kapasitet)...")
  batteri.ladOpp(60.0)
  print(f"Energimengde: {batteri.visEnerginivå()} (forventet: 100.0)")
 
  # Test forbruk av energi
  print("Bruker 30 enheter energi...")
  batteri.brukEnergi(30.0)
  print(f"Energimengde: {batteri.visEnerginivå()} (forventet: 70.0)")
 
  # Test overforbruk
  try:
    print("Prøver å bruke 80 enheter energi (mer enn tilgjengelig)...")
    batteri.brukEnergi(80.0)
  except ValueError as e:
    print(f"Feil oppdaget: {e}")

  # Test negativ lading
  try:
    print("Prøver å lade med -10 enheter...")
    batteri.ladOpp(-10.0)
  except ValueError as e:
    print(f"Feil oppdaget: {e}")
 
  # Test negativt energiforbruk
  try:
    print("Prøver å bruke -5 enheter energi...")
    batteri.brukEnergi(-5.0)
  except ValueError as e:
    print(f"Feil oppdaget: {e}")

  print("UTEN TRY-EXCEPT")
  print("Prøver å bruke 80 enheter energi (mer enn tilgjengelig)...")
  batteri.brukEnergi(80.0)
  # Dette løsningsforslaget lager klasser med kode som stopper programmet fra å virke når klassen brukes feil

# Kjør testprogrammet
testBatteri()
