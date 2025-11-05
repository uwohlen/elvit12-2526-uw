# Klasser har navn som starter med stor forbokstav
# Det betyr at variabler og funksjoner skal IKKE starte med stor forbokstav
# Nye ord: parametrene eller variablene kalles nå egenskaper... self.egenskap (eller attributter)
#          funksjonene kalles nå metoder... self.metode() 
class Dyr:
  def __init__(self,navn,rase,farge,hale="Lang"): # parametre med defaultverdi skrives sist
    self.navn = navn
    self.rase = rase
    self.farge = farge
    self.hale = hale
    self.alder = 0       # kan ha egenskaper som ikke angis som parameter

  def dyr_info(self):    # metoder har alltid parameteren self
    print(self.navn,"er en",self.farge.lower(),self.rase.lower())

  def aldring(self,antall):   # metoder kan ha flere parametre
    self.alder += antall
    print(self.navn,"er nå",self.alder,"år")

# Et OBJEKT er en variabel som bygger på en klasse, det som self viser til:
# Lages ved å kalle opp klassen med tilhørende argumenter for alle parametrene unntatt self

katt1 = Dyr("Pus","Tibetansk nakenkatt","Lysebrun","Kort")

print(katt1.navn)     # refererer til en egenskap
print(katt1.alder)
print(type(katt1))    # __main__ betyr at klassen Dyr ligger i samme program

katt1.dyr_info()      # refererer til en metode 

katt1.aldring(4)      # legg merke til at metoden aldring bare har ett argument,
                      # selv om den er definert med to. Vi oppgir ikke verdi for self.
                      


mine_dyr = [
  Dyr("Silkesvarten","Norsk skogkatt","Svart"),
  Dyr("Tigergutt","Norsk skogkatt","Stripete grå-svart"),
  Dyr("Kaisa","Labrador retriever","Svart")
]

for dyr in mine_dyr:
  dyr.dyr_info()
  dyr.aldring(3)

mine_dyr[2].aldring(5)