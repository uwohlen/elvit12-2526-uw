"""
b=4
c=5
for a in range(2,5):
  print(c)
  b -= 1
  c = c + b



for num in range(-2,3,1):
  if num < 0:
    if num%2 == 0:
      print(num,"er negativt og partall")
    else:
      print(num,"er negativt og oddetall")      
  elif num == 0:
    print(num,"er null")
  else:
    if num%2 == 0:
      print(num,"er positivt og partall")
    else:
      print(num,"er positivt og oddetall")


n = 10
a = []
a.append(0)
a.append(1)
for i in range(2,n+1):
  a.append(a[i-1] + a[i-2])
print(a[n])
"""

a = []
a.append(0)
a.append(1)
p = 0
maxp = 10
i = 2
while p < maxp:
  a.append(a[i-1] + a[i-2])
  #print(a[i])
  if a[i]%2 == 0:
    print(a[i])
    p += 1
  i += 1