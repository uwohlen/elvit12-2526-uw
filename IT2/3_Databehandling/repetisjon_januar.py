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
  
  n = rd.randint(1,6)
  m = rd.randint(1,6)
  it = rd.randint(1,6)
  r = rd.randint(1,6)

  alt.append([nr,kj,kl,n,m,it,r])
  i += 1

print(alt)