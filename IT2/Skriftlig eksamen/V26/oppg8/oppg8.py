import sys
import os
print()
print("Filen ligger her:",sys.path[0])
print()
print("Mappa over filen (parent):",os.path.dirname(sys.path[0]))
print()
print("Mappa over mappa over filen (grandparent):",os.path.dirname(os.path.dirname(sys.path[0])))
# osv...

# Legger til en referanse til biblioteksmappa, slik at filene der finnes av programmet
sys.path.append(os.path.join(os.path.dirname(sys.path[0]),"bibliotek"))
print()
print("Funksjonsbiblioteket:",sys.path[-1])
print()

# FJERN # I LINJEN UNDER FØR KJØRING
# import funksjon_bibliotek as fb # VSC reagerer på denne måten å skrive det på (men det virker!)

# VSC ville ha skrevet det slik (men det virker ikke!):
# SETT PÅ # I LINJEN UNDER FØR KJØRING
from ..bibliotek import funksjon_bibliotek as fb 

liste = [['M', 178], ['K', 176], ['K', 171], ['K', 163], ['M', 187], ['K', 170], ['M', 172], ['K', 168], ['M', 169], ['K', 161], ['K', 174], ['M', 206], ['M', 180], ['K', 165], ['K', 180], ['K', 174], ['K', 167], ['K', 170], ['K', 177], ['M', 193], ['M', 188], ['K', 162], ['K', 165], ['K', 166], ['M', 174], ['K', 177], ['K', 182], ['K', 171], ['K', 169], ['K', 174]]

v1 = fb.bytt2D_kol(liste,0,"M","Mann")
v2 = fb.bytt2D_kol(v1,0,"K","Kvinne")
v3 = fb.bytt2D_kol(v2,1,178,190)

print(v3)

