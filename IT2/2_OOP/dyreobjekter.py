import dyreklasser as dk

# dk.  VSC gir meg valg mellom Dyr, Hund og Katt - den har lest dyreklasser.py
#help(dk.Katt)

# legg merke til at jeg skriver liv=2, ikke bare 2, siden jeg hopper over hale:
mine_dyr = [
  dk.Katt("Silkesvarten","Norsk skogkatt","Svart",liv=2),
  dk.Katt("Tigergutt","Norsk skogkatt","Stripete grå-svart",liv=1),
  dk.Hund("Kaisa","Labrador retriever","Svart"),
  dk.Hund("Rita","Schäferhund","Svart og brun"),
  dk.Hund("Heidi","Norsk buhund","Svart og hvit")
]

print(mine_dyr[0].hale)   # Halen får standardverdien
mine_dyr[0].antall_liv()  # Antall liv har verdi liv=2, og får +1 fra metoden

for dyr in mine_dyr:
  dyr.__str__()
  dyr.aldring(3)
  dyr.snakk()
  print(type(dyr))        # dyreklasser.Katt viser at klassen er definert i filen dyreklasser.py

mine_dyr[2].aldring(5)

for i in range(6):
  mine_dyr[0].antall_liv()