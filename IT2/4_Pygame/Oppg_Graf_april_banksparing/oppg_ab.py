import csv

filnavn = "bank.csv"

# legger hele datasettet inn i lista innhold for videre programmering
# og kolonnenavnene inn i lista overskrifter for å ta en kikk
innhold = []
with open(filnavn, encoding="utf-8-sig") as fil:
    filinnhold = csv.reader(fil, delimiter=";")
    overskrifter = next(filinnhold)

    for rad in filinnhold:
        innhold.append(rad)

overskrifter[0] = "ID"
overskrifter[1] = "Kjønn"
overskrifter[2] = overskrifter[2].capitalize() + " (kr)"
overskrifter[3] = "Rente (%)"
overskrifter.append("Etter ti år (kr)")
#print(overskrifter)
for rad in innhold:
    rad[0] = int(rad[0])
    rad[2] = int(rad[2])
    rad[3] = float(rad[3].replace(",","."))
    rad.append(rad[2]*(1+rad[3]/100)**10)

#print(innhold)

print()
print("Oppgave a og b: Tabell over ID, kjønn, innskudd, rente og verdi etter 10 års sparing")
print()

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
for i in range(len(innhold)):
    for j in range(len(innhold[i])):
        if j == 1:
            print(f"{innhold[i][j]:<16}" + " | ", end="")
        elif j == 4:
            print(f"{innhold[i][j]:>16.2f}" + " | ", end="")
        else:
            print(f"{innhold[i][j]:>16}" + " | ", end="")
    print()

# Strek under tabellen
for i in range(19*len(overskrifter)):
    print("-", end="")
print()
