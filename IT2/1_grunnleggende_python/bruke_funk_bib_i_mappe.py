import sys
import os
print(sys.path)

sys.path.append(os.path.join(sys.path[0],"uw_bibliotek"))

print(sys.path)

import uw_funksjonsbibliotek as fb


liste = [['M', 178], ['K', 176], ['K', 171], ['K', 163], ['M', 187], ['K', 170], ['M', 172], ['K', 168], ['M', 169], ['K', 161], ['K', 174], ['M', 206], ['M', 180], ['K', 165], ['K', 180], ['K', 174], ['K', 167], ['K', 170], ['K', 177], ['M', 193], ['M', 188], ['K', 162], ['K', 165], ['K', 166], ['M', 174], ['K', 177], ['K', 182], ['K', 171], ['K', 169], ['K', 174]]

v1 = fb.bytt2D_kol(liste,0,"M","Mann")
v2 = fb.bytt2D_kol(v1,0,"K","Kvinne")
v3 = fb.bytt2D_kol(v2,1,178,190)

print(v3)

