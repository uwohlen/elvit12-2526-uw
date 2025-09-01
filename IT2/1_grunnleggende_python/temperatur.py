temperatur = input("Oppgi vannets temperatur: ")
temperatur = float(temperatur)

if temperatur > 0:
  print("Vannet er i flytende form.")
elif temperatur > 100:
  print("Vannet koker.")
else:
  print("Vannet fryser til is.")