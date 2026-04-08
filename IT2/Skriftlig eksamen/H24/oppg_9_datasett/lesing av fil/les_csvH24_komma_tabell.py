"""
Oppgavetekst: "Programmet du lager i denne oppgaven, skal inneholde en flerlinjekommentar øverst som beskriver de vurderingene og valgene du har gjort for å forberede datasettet til bruk i programmering, hvis du har gjort det."

Behandling av datasett-filen:
-det står at CSV-filen er UTF-8-kodet, men å og ø i overskriftene til de to første kolonnene blir ikke kodet riktig. Jeg har valgt å hardkode overskriftene i programmet under slik at de inneholder å og ø på riktig måte. Dermed vil nye versjoner av data-filen fremdeles kunne leses uten manuelle endringer i datafilen.

Tabellen blir fin hvis skriftstørrelsen ikke er for stor i forhold til terminalvinduet / konsollen.
"""
import csv
filnavn = "Datasett_fodselstall_komma.csv"
alt = []

# Leser med csv.reader for å kunne endre overskriftene som inneholder å og ø
with open(filnavn,encoding="utf-8") as fil:
  hele_filen = csv.reader(fil)

  overskrifter = next(hele_filen)
  overskrifter[0] = "År"
  overskrifter[1] = "Fødselstall"
  overskrifter.append("Netto folkevekst")

  for linje in hele_filen:
    # kan ikke gjøre utregninger hvis vi ikke har alle verdiene
    if linje[1] != "" and linje[2] != "" and linje[3] != "": 
      linje.append(int(linje[1]) + int(linje[2]) - int(linje[3])) # regn ut netto folkevekst
    else:
      linje.append(" ") # legg inn tom verdi om netto folkevekst ikke kan regnes ut
    alt.append(linje)

# Lag overskrifter i tabellen
for i in range(len(overskrifter)):
  print(f"{overskrifter[i]:16}" + " | ", end="") # Bredeste overskrift er 15 bokstaver, +1 for luft
print()

# Strek mellom overskrifter og innhold
for i in range(19*len(overskrifter)): # Kolonnebredden er 19 bokstaver inkludert |
  print("-", end="")
print()

# Skriv ut hele tabellen, årstall er venstrestilt, resten høyrestilt
# Regner med at tabellen skal inneholde årstall selv om det ikke sto i oppgaveteksten.
for i in range(len(alt)):
  for j in range(len(alt[i])):
    if j == 0:
      print(f"{alt[i][j]:<16}" + " | ", end="")
    else:
      print(f"{alt[i][j]:>16}" + " | ", end="")
  print()

# Strek under tabellen
for i in range(19*len(overskrifter)):
  print("-", end="")
print()