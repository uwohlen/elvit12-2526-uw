import random as rd

alt = []
kjonn = ["M","K"]
klasse = ["A","B","C","D","E","F","G","I","J","P"]

i=0
while i<300:
  if i<10:
    nr = "ELV00" + str(i)
  elif i<100:
    nr = "ELV0" + str(i)
  else:
    nr = "ELV" + str(i)

  kj = rd.choice(kjonn)
  kl = "3ST" + rd.choice(klasse)
  
  elev = [nr,kj,kl]

  j=0
  while j<20:
   elev.append(rd.randint(1,6))
   j += 1

  alt.append(elev)
  i += 1

print(alt)