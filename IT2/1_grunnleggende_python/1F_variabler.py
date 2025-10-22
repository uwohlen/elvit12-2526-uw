tall = 4 

# variabler, kapittel 1F
a = int(input("skriv tall: "))
c = None
if a < 10:
  b = 2
  print(b)
else:
  c = 4

if c != None:
  print(c)

#v1 = 3

def f(x):
  global v1 # men det er bedre å bruke return
  v1 = x
  print(v1)

f(7)

print(v1)

def g(x):
  return x


v4 = g(8)
print(v4)