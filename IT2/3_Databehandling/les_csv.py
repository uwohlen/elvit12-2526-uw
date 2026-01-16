import csv
import matplotlib.pyplot as plt

filnavn = "kvadrater_utf8.csv"

alt = []
x = []
y = []

with open(filnavn,encoding="utf-8-sig") as fil:
  hele_filen = csv.reader(fil,delimiter=";")
  overskrifter = next(hele_filen)

  for linje in hele_filen:
    alt.append(linje)
    x.append(int(linje[0]))
    y.append(int(linje[1]))

print(overskrifter)
print(alt)
print(x)
print(y)

plt.plot(x,y)
plt.show()