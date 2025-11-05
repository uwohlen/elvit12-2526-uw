# Problemstilling: Mjau og Voff krever forskjellige metoder
# Vi lager nye klasser, som arver alt fra Dyr, men får MER I TILLEGG

class Dyr:
  def __init__(self,navn,rase,farge,bolig="Inne"):
    self.navn = navn
    self.rase = rase
    self.farge = farge
    self.bolig = bolig

  def dyr_info(self):
    print(self.navn,"er en",self.farge.lower(),self.rase.lower(),"som bor",self.bolig)

# Arv

class Katt(Dyr):   # Legg merke til parentes med navnet på klassen som det arves fra
  def __init__(self,navn,rase,farge,liv,bolig="Inne"):   # Her kan det være flere parametre
    super().__init__(navn,rase,farge,bolig)       # Her starter vi Dyr-klassen med dens parametre
    self.liv = liv                          # Denne egenskapen er ny, kommer i tillegg til de som var i Dyr
  
  def snakk(self):                          # Ny metode for katten
    print(self.navn,'sier "Mjau"')

  def antall_liv(self):
    self.liv += 1
    if self.liv >= 9:
      print(self.navn,"har nå brukt alle sine liv :(")
    else:
      print(self.navn,"har nå brukt",self.liv,"liv.")


class Hund(Dyr):
  def __init__(self,navn,rase,farge):       # Hunden har akkurat de samme parametrene som Dyr
    super().__init__(navn,rase,farge)
  
  def snakk(self):                          # Ny metode for hunden
    print(self.navn,'sier "Voff"')


# kattene har ett argument mer enn hunden... for kattene kan ha 9 liv:
mine_dyr = [
  Katt("Silkesvarten","Norsk skogkatt","Svart",2,"I stallen"),
  Katt("Tigergutt","Norsk skogkatt","Stripete grå-svart",1),
  Hund("Kaisa","Labrador retriever","Svart")
]

for dyr in mine_dyr:
  dyr.dyr_info()
  dyr.snakk()
  print(type(dyr))

for i in range(10):
  mine_dyr[0].antall_liv()