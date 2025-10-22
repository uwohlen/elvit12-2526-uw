alt = [
  ["Nils","Hansen",17183423,[44,25,46,65,96,73,65]],
  ["Kari","Johnsen",18234223,[46,42,13,39,64,35,36]],
  ["Lise","Voll",19123563,[13,34,63,93,84,66,35]],
  ["Inger","Selbakk",17214334,[65,44,36,53,94,65,13]],
  ["Magnus","Kolstad",18133265,[22,55,6,15,26,33,5]],
  ["Morten","Sletten",17233123,[54,64,48,46,59,46,24]],
  ["Else","Kollen",16123141,[41,43,26,38,50,56,54]],
  ["Ole","Gran",18144235,[52,26,19,26,22,16,61]],
  ["Line","Ringen",17122345,[43,25,18,33,61,45,58]]
]

print(alt[0][1])

"""
person = {
  "fornavn": ,
  "etternavn": ,
  "tlf": ,
  "resultater": 
}
"""
person1 = {
  "fornavn": "Nils",
  "etternavn": "Hansen",
  "tlf": 17183423,
  "resultater": [44,25,46,65,96,73,65]
}

print(person1["etternavn"])



personer = [
  {
    "fornavn": "Nils",
    "etternavn": "Hansen",
    "tlf": 17183423,
    "resultater": [44,25,46,65,96,73,65]
  },
  {
    "fornavn": "Kari",
    "etternavn": "Johnsen",
    "tlf": 18234223,
    "resultater": [46,42,13,39,64,35,36]
  },
  {
    "fornavn": "Lise",
    "etternavn": "Voll",
    "tlf": 19123563,
    "resultater": [13,34,63,93,84,66,35]
  },
  {
    "fornavn": "Inger",
    "etternavn": "Selbakk",
    "tlf": 17214334,
    "resultater": [65,44,36,53,94,65,13]
  },
  {
    "fornavn": "Magnus",
    "etternavn": "Kolstad",
    "tlf": 18133265,
    "resultater": [22,55,6,15,26,33,5]
  },
  {
    "fornavn": "Morten",
    "etternavn": "Sletten",
    "tlf": 17233123,
    "resultater": [54,64,48,46,59,46,24]
  },
  {
    "fornavn": "Else",
    "etternavn": "Kollen",
    "tlf": 16123141,
    "resultater": [41,43,26,38,50,56,54]
  },
  {
    "fornavn": "Ole",
    "etternavn": "Gran",
    "tlf": 18144235,
    "resultater": [52,26,19,26,22,16,61]
  },
  {
    "fornavn": "Line",
    "etternavn": "Ringen",
    "tlf": 17122345,
    "resultater": [43,25,18,33,61,45,58]
  },
]

print(personer[0]["etternavn"])


def gjennomsnitt(liste):
  total = 0
  for x in liste:
    total += x
  return total/len(liste)

for person in alt:
  person.append(round(gjennomsnitt(person[3]),1))

print(alt[0][4])

for person in personer:
  person["snitt"] = round(gjennomsnitt(person["resultater"]),1)

print(personer[0]["snitt"])

