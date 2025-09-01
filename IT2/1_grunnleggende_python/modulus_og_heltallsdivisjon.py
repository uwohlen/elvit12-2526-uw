""" a = 17
b = 3

print(a/b)
print(a%b)
print(a//b)
print((a%b)/b+(a//b)) """

x = 1
while x <= 50:
  print(x,end=" ")
  if x % 7 == 0:
    print("er i 7-gangen")
  else:
    print()
  x = x + 1