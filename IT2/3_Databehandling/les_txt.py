
"""
filnavn = "tekst.txt"

teller = 0
with open(filnavn,encoding="utf-8") as fil: # with fører til: lukkes automatisk
  innhold = fil.read() # les alt på en gang
  teller += 1
  print(teller) 
  
print(innhold)
"""

"""
filnavn = "tekst.txt"
teller = 0
alt = []
with open(filnavn,encoding="utf-8") as fil: # with fører til: lukkes automatisk
  for linje in fil: # les en linje om gangen (kjenner igjen linjeskift i tekstfilen)
    teller += 1
    print(teller, end="") 
    #print(linje,end="") # en linjeskift fra tekst-filen, en linjeskift fra print 
    #print(linje.rstrip(),end=" - ")
    alt.append(linje.rstrip().split(" "))

print()
print(alt)
"""


"""
filnavn = "ny_tekst_v2.txt"

with open(filnavn, "w") as fil:
  fil.write("Hei\n")
  fil.write("Ha det bra\n")
  fil.write("tredje linje\n")

with open(filnavn, "w") as fil:
  fil.write("Linje 3\n")
  fil.write("Linje 4\n")

"""
filnavn = "ny_tekst_v3.txt"
with open(filnavn, "w") as fil:
  for i in range(10):
    tekst = str(i) +  ";" + str(i*i) + "\n"
    fil.write(tekst)

with open(filnavn, "a") as fil:
  for i in range(20,30,1):
    tekst = str(i) +  ";" + str(i*i) + "\n"
    fil.write(tekst)

