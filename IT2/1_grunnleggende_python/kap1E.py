tall = [1,2,3]
bokstaver = ["a","b","c"]


# når ting skal skje basert på posisjon (eller verdi)
# og/eller vi ønsker å gjøre endringer i original-lista
for i in range(len(tall)):
  if (i == 0):
    tall[i] = tall[i] * 10
    print(tall[i],"første")
  elif (tall[i] == 3):
    print(tall[i],"her er 3'ern")
  else:
    print(tall[i])
print(tall)