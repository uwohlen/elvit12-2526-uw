
from random import randint
class Monster:
    def __init__(self,navn,helse,styrke,svakhet):
        self.navn = navn
        self.helse = helse
        self.styrke = styrke
        self.svakhet = svakhet
        self.forfall = 1
    def sloss(self,intensitet):
        self.helse = self.helse - intensitet*self.forfall
        return self.helse
    
    def oppStyrke(self,pluss):
        print("Mat, søvn og trening gjør underverker. Styrken øker for",self.navn)
        self.styrke = self.styrke + pluss
        

monster1 = Monster("Gnarl",100,80,"Pixiedust")
class Spiller(Monster):
    def __init__(self,navn,helse,styrke, svakhet):
        self.utstyr = []
        super().__init__(navn,helse,styrke,svakhet)
    def ting(self,fant):
        #sette inn sjekk på om jeg har det fra før (hvis jeg bare kan ha 1)
        print("Du finner",fant,"og tar det med deg videre")
        self.utstyr.append(fant)
spiller1 = Spiller("Hero",100,50,"Damsels in distress")
print()
print("Vår helt Hero har ankommet Monsterland, hvor monsteret Gnarl har tatt en prinsesse til fange.")
print()
print("Rescue the princess or die trying! Veien framover er klar...")
while (True):
    print()
    print(vars(spiller1))
    print(vars(monster1))
    print()
    print("Mulige handlinger:")
    print("Gå videre og se hva som hender (g)")
    print("Avslutt spillet (q)")
    print()
    svar = input("Hva vil du gjøre? ")
    print()
    if (svar == "q"):
        break
    elif (svar == "g"):
        hendelse = randint(1,4)
        if (hendelse == 1):
            spiller1.oppStyrke(10)
        elif (hendelse == 2):
            spiller1.ting("Pixiedust")
        elif (hendelse == 3):
            monster1.oppStyrke(10)
        else:
            print("En episk kamp finner sted. Det kjempes med alle midler")
            try:
                if (spiller1.utstyr[0] == "Pixiedust"):
                    monster1.forfall = monster1.forfall*1.5
                    spiller1.utstyr.pop()
            except:
                pass
            spillerhelse = spiller1.sloss(monster1.styrke)
            monsterhelse = monster1.sloss(spiller1.styrke)
            if (monsterhelse <= 0):
                print("Gnarl er død, prinsessen er fri! Gratulerer!")
            if (spillerhelse <= 0):
                print("Dessverre døde du under redningsforsøket. Vi møtes igjen i Valhall.")
            if (monsterhelse <= 0 or spillerhelse <= 0):
                print(vars(spiller1))
                print(vars(monster1))
                break
    else:
        print("Ukjent kommando. Prøv igjen.")

print("OK bye!")
"""
print(type(monster1))
print(vars(monster1))
print(type(spiller1))
print(vars(spiller1))
"""
