fortsett = True

while fortsett:
  print("Meny")
  print("a - ananas")
  print("b - banan")
  print("q - quit")
  svar = input("Hva velger du? ")
  if svar == "q":
    fortsett = False
  else:
    print(svar)

    