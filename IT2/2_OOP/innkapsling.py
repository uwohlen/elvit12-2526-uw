class Test:
  """
  Inneholder attributtene
    x
    public_y
    ekstra

  Endre attributten ekstra ved hjelp av
    set_ekstra(verdi:int)

  Hent attributten ekstra ved hjelp av 
    get_ekstra()
  """
  def __init__(self,privat_x:int,public_y:int):
    self.__privat_x = privat_x
    self.public_y = public_y
    self.__privat_ekstra:int = 0

  def set_ekstra(self,verdi:int) -> None:
    if type(verdi) == int:
      self.__privat_ekstra = verdi
    else:
      print("Feilmelding for ekstra verdi")

  def get_ekstra(self) -> int:
    return self.__privat_ekstra

test_obj = Test(5,10)

#print(test_obj.__privat_x) # feilmelding
print(test_obj.public_y)
#print(test_obj.__privat_ekstra) # feilmelding

test_obj._Test__privat_x = "Hei" # Kan likevel fås tak i, men da skal man virkelig gå inn for å gjøre bøll

print(test_obj._Test__privat_x)

test_obj.set_ekstra("hei") # Funksjon hindrer feil data inn

print(test_obj._Test__privat_ekstra)

test_obj._Test__privat_ekstra = "Hei" # Men kan omgås

print(test_obj._Test__privat_ekstra)

# Setter og getter avslører ikke attributtnavn
test_obj.set_ekstra(100) # Riktig bruk av setter
b = test_obj.get_ekstra() # og getter

print(b)

