print("Velg fra menyen under")
fortsett = True

while fortsett:
  print()
  print("MENY")
  print("a - addisjon")
  print("m - multiplikasjon")
  print("q - quit")
  print()

  svar = input("Ditt valg: ")

  if svar == "q":
    fortsett = False
  elif svar == "a":
    tall1test = True
    while tall1test:
      print()
      a1 = input("Skriv inn et tall: ")
      try:
        tall1 = float(a1)
        tall1test = False
      except:
        print("Du må skrive inn et tall.")
    tall2test = True
    while tall2test:
      print()
      a2 = input("Skriv inn et tall til: ")
      try:
        tall2 = float(a2)
        tall2test = False
      except:
        print("Du må skrive inn et tall.")
    print()
    print(tall1,"+",tall2,"=",tall1+tall2)
  elif svar == "m":
    tall3test = True
    while tall3test:
      print()
      m1 = input("Skriv inn et heltall (1-10): ")
      try:
        tall3 = int(m1)
        if tall3 < 1 or tall3 > 10:
          print("Tallet må være i området 1 til 10")
        else:
          tall3test = False
      except:
        print("Du må skrive inn et heltall (1-10)")
    print()
    plass = " "
    print(f"{plass:5}",end=" ")
    for i in range(1,tall3+1):
      print(f"{i:5}",end=" ")
    print()
    for i in range(0,tall3*6+7):
      print("-",end="")
    print()
    for i in range(1,tall3+1):
      print(f"{i:5}", end=":")
      for j in range(1,tall3+1):
        print(f"{i*j:5}", end=" ")
      print()  
        
  else:
    print("Du må velge fra menyen")

print("Takk for i dag!")
