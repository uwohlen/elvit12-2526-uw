import pandas as pd

verdier = [1, 7, 2]

myvar = pd.Series(verdier, index=["a","b","c"])

print(myvar)
print()
print(myvar["b"])
print()



calories = {"day1": 420, "day2": 380, "day3": 390}

myvar = pd.Series(calories)

print(myvar)
print()
print(myvar["day2"])
print()

mydataset = {
  'cars': ["BMW", "Volvo", "Ford"],
  'passings': [3, 7, 2]
}

myvar = pd.DataFrame(mydataset, index=["tysk","svensk","amerikansk"])

print(myvar)
print()
#print(myvar.loc[1])
print(myvar.loc["svensk"])
print()
#print(myvar.loc[[1,2]])
print(myvar.loc[["svensk","amerikansk"]])
print()