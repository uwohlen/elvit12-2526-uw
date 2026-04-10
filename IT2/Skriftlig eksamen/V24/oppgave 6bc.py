class Kalkulator:
  """
  Klasse for å lage kalkulator-objekter

  Parametre:
    a (float): første tall i en regneoperasjon
    b (float): andre tall i en regneoperasjon

  Metoder:
    pluss(float): regner ut a + b
    minus(float): regner ut a - b
    gange(float): regner ut a * b
    dele(float):  regner ut a / b     # NB programmet må sjekke om b = 0
  """
  def __init__(self,a,b):
    self.a = a
    self.b = b
  
  def pluss(self):
    return self.a + self.b
  
  def minus(self):
    return self.a - self.b
  
  def gange(self):
    return self.a * self.b
  
  def dele(self):
    return self.a / self.b



# Sjekkprogram - input-verdier
averdier = [-1000,-10, 0,0.25, 5,1000]
bverdier = [  -10,  5, 1,-0.5, 2,1000]
# Gyldige svar
plussverdier = [-1010,-995,-999,-1000.5,-998,0,-20,-5,-9,-10.5,-8,990,-10,5,1,-0.5,2,1000,-9.75,5.25,1.25,-0.25,2.25,1000.25,-5,10,6,4.5,7,1005,990,1005,1001,999.5,1002,2000]
minusverdier = [-990,-1005,-1001,-999.5,-1002,-2000,0,-15,-11,-9.5,-12,-1010,10,-5,-1,0.5,-2,-1000,10.25,-4.75,-0.75,0.75,-1.75,-999.75,15,0,4,5.5,3,-995,1010,995,999,1000.5,998,0]
gangeverdier = [10000,-5000,-1000,500.0,-2000,-1000000,100,-50,-10,5.0,-20,-10000,0,0,0,-0.0,0,0,-2.5,1.25,0.25,-0.125,0.5,250.0,-50,25,5,-2.5,10,5000,-10000,5000,1000,-500.0,2000,1000000]
deleverdier =  [100.0,-200.0,-1000.0,2000.0,-500.0,-1.0,1.0,-2.0,-10.0,20.0,-5.0,-0.01,-0.0,0.0,0.0,-0.0,0.0,0.0,-0.025,0.05,0.25,-0.5,0.125,0.00025,-0.5,1.0,5.0,-10.0,2.5,0.005,-100.0,200.0,1000.0,-2000.0,500.0,1.0]

p = 0
e = 0
for i in range(len(averdier)):
  for j in range(len(bverdier)):
    kalkis = Kalkulator(averdier[i],bverdier[j])
    if kalkis.pluss() != plussverdier[p] or kalkis.minus() != minusverdier[p] or kalkis.gange() != gangeverdier[p] or kalkis.dele() != deleverdier[p]:
      print("error: input",averdier[i],bverdier[j])
      print("pluss",kalkis.pluss(),plussverdier[p])
      print("minus",kalkis.minus(),minusverdier[p])
      print("gange",kalkis.gange(),gangeverdier[p])
      print("dele",kalkis.dele(),deleverdier[p])
      e += 1
    p += 1
if e == 0:
  print("Alle sjekker kjørte ok")



