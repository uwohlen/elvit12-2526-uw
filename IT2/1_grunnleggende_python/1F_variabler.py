# variabler, kapittel 1F
a = 5

if a < 10:
  b = 2
else:
  c = 4

print(b)
#print(c)

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