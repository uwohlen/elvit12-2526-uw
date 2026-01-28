tall = [4,7,2,4,8,10,9,1]

# sortering

# standard funksjon
tall_kopi = sorted(tall)
print(tall_kopi)


# liste - metode
tall_kopi2 = tall.copy()
tall_kopi2.sort()
print(tall_kopi2)


# standard funksjon og liste-metode

tall_kopi3 = list(tall)
tall_kopi3.sort()
print(tall_kopi3)


# egen programmering av kopi og sortering, bruker noen andre liste-metoder

tall_kopi4 = []
for verdi in tall:
  tall_kopi4.append(verdi)

tall_kopi5 = []
for i in range(len(tall)):
  minst = tall_kopi4[0]
  for j in range(1,len(tall_kopi4)):
    if tall_kopi4[j] < minst:
      minst = tall_kopi4[j]
  tall_kopi5.append(minst)
  tall_kopi4.remove(minst)



print(tall_kopi5)

print(tall)


# standard funksjon gir feil resultat

tekst = ["b","u","æ","r","å","a","ø","f"]
tekst_kopi = sorted(tekst)
print(tekst_kopi)

# egen programmering for sortering (men fremdeles feil resultat)... dessuten er koden lite effektiv (bruker n!*n runder)
tekst_kopi2 = list(tekst)
tekst_kopi3 = []

for i in range(len(tekst)):
  minst = tekst_kopi2[0]
  for j in range(1,len(tekst_kopi2)):
    if tekst_kopi2[j] < minst:
      minst = tekst_kopi2[j]
  tekst_kopi3.append(minst)
  tekst_kopi2.remove(minst)

print(tekst_kopi3)


# egen programmering - en mulig løsning på problemet (tar ikke hensyn til store bokstaver, og fremdeles lite effektiv kode (n+n!*n runder))
tekst_kopi4 = list(tekst)
tekst_kopi5 = []
bokstav_vekt = []

for bokstav in tekst_kopi4:
  if bokstav == "æ":
    bokstav_vekt.append(1)
  elif bokstav == "ø":
    bokstav_vekt.append(2)
  elif bokstav == "å":
    bokstav_vekt.append(3)
  else:
    bokstav_vekt.append(0)

for i in range(len(tekst)):
  minst = tekst_kopi4[0]
  minst_vekt = bokstav_vekt[0]
  minst_indeks = 0
  for j in range(1,len(tekst_kopi4)):
    if bokstav_vekt[j] < bokstav_vekt[minst_indeks] or bokstav_vekt[j] == bokstav_vekt[minst_indeks] and tekst_kopi4[j] < minst:
      minst = tekst_kopi4[j]
      minst_vekt = bokstav_vekt[j]
      minst_indeks = j
  tekst_kopi5.append(minst)
  tekst_kopi4.remove(minst)
  bokstav_vekt.pop(minst_indeks)


print(tekst_kopi5)



print(tekst)