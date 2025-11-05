
# Lister blir fort uoversiktlige - hva betyr egentlig 2007 og 2003 her?
person1 = ["Unni",54,175,2007,2003]

# Ordbøker er bedre variabler, for de forklarer hva hver verdi betyr
person2 = {
  "navn" : "Unni",
  "alder" : 54,
  "hoyde" : 175,
  "ansatt" : 2007,
  "klatret_siden" : 2003
}



# Med flere variabler av typen ordbøker så kan det være fort gjort å 
# få noen skrivefeil, f.eks her har katt1 nøkkelordet "type", mens
# katt2 har nøkkelordet "rase"
katt1 = {
  "navn" : "Silkesvarten",
  "type" : "Norsk skogkatt",
  "farge" : "Svart"
}

katt2 = {
  "navn" : "Tigergutt",
  "rase" : "Norsk skogkatt",
  "farge" : "Stripete grå-svart"
}

hund1 = {
  "navn" : "Kaisa",
  "rase" : "Labrador retriever",
  "farge" : "Svart"
}

# For enklere behandling med løkker, så tar vi gjerne ordbøker inn i en liste
mine_dyr = [katt1, katt2, hund1]


# Funksjoner kalles også prosedyrer, derav prosedyreorientert programmering
def snakk_katt(dyr):
  print(dyr["navn"],'sier "Mjau"')

def snakk_hund(dyr):
  print(dyr["navn"],'sier "Voff"')

def dyr_info(dyr):
  print(dyr["navn"],"er en",dyr["farge"].lower(),dyr["rase"].lower())


# Noen funksjoner kan brukes for alle dyrene:
for dyr in mine_dyr:
  dyr_info(dyr)

# Noen funksjoner virker bare for enkelte dyr, kan ikke bruke løkke her:
snakk_katt(mine_dyr[0])
snakk_hund(mine_dyr[2])
