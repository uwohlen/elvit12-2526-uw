def test1():
  print("fullført")

test1()

def test2(param1,param2=4):
  total = param1 + param2
  return total

print(test2(1,3))
print(test2("a","b"))

var1 = test2(6)
var2 = var1*4
print(var2)

def dumfunk():
  print("utskrift")
  return "verdi"

print(dumfunk())
a = dumfunk() 


def test3():
  pass

print("programmet går")
print(test3())
print("videre")