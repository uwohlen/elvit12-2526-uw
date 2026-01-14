import matplotlib.pyplot as plt

fig, ax = plt.subplots()

# Skulle vært x-verdier, men er for lange:
utdanningsprogram = [
  "Bygg- og anleggsteknikk", 
  "Elektro og datateknologi",
  "Helse- og oppvekstfag",
  "Naturbruk",
  "Restaurant- og matfag",
  "Teknologi- og industrifag",
  "Håndverk, design og produktutvikling",
  "Frisør, blomster, interiør og eksponeringsdesign",
  "Informasjonsteknologi og medieproduksjon",
  "Salg, service og reiseliv"
]

# Alternative x-verdier, og linken mellom alternativene og listen over:
nr = []
referanse = []
for i in range(len(utdanningsprogram)):
  nr.append(str(i+1))
  referanse.append(str(i+1) + ": " + utdanningsprogram[i])

# y-verdier
antall = [3811, 4168, 8661, 2057, 1484, 5501, 313, 901, 1309, 2061]

# Farger til søylene
bar_colors = ["red", "blue", "orange", "gray", "pink", "purple", "cyan", "olive", "brown", "yellow"]


ax.bar(nr, antall, label=referanse, color=bar_colors)

ax.set_ylabel('Antall søkere')
ax.set_xlabel('Utdanningsprogram, nummerert')
ax.grid(axis="y") # linjer i y-retning
ax.set_title('Søkertall fordelt på yrkesrettede utdanningsprogrammer i 2021')

# Bedre plass med mindre font
# plassering i hjørnene: velg hjørne med loc 1,2,3, ..., 10
ax.legend(title='Yrke',loc=1, prop={'size': 6}) # size er fontstørrelse

# Kan tvinge y-aksen til å bli lengre, dermed blir søylene kortere
# og det blir bedre plass til legend
ax.set_ylim(0,10000)
#ax.set_ylim(0,20000)


plt.show()
