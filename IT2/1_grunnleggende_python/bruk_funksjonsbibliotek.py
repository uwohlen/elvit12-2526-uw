import funksjonsbibliotek as fb
import random as rd

liste = [['M', 178], ['K', 176], ['K', 171], ['K', 163], ['M', 187], ['K', 170], ['M', 172], ['K', 168], ['M', 169], ['K', 161], ['K', 174], ['M', 206], ['M', 180], ['K', 165], ['K', 180], ['K', 174], ['K', 167], ['K', 170], ['K', 177], ['M', 193], ['M', 188], ['K', 162], ['K', 165], ['K', 166], ['M', 174], ['K', 177], ['K', 182], ['K', 171], ['K', 169], ['K', 174]]

"""
e_nr = 0
for rad in liste:
  rad[0] = e_nr
  e_nr += 1
  rad.append(rd.randint(1,6))
  rad.append(rd.randint(1,6))
  rad.append(rd.randint(1,6))
  rad.append(rd.randint(1,6))
print(liste)
"""

v1 = fb.bytt(liste,0,"M","Mann")
v2 = fb.bytt(v1,0,"K","Kvinne")
v3 = fb.bytt(v2,1,178,190)

print(v3)

help(fb.bytt)

print(liste)