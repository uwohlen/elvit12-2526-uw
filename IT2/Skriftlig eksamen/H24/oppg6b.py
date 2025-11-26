#import oppg6a as bk
import oppg6c as bk


print()
print("Riktig bruk skal virke uten feilmeldinger")
print("Lager et batteri med energinivå 20 og kapasitet 100")
batteri1 = bk.Batteri(20,100)
print("Lader opp med 50")
batteri1.ladOpp(50)
print("Skal ende opp med energinivå på 70")
print(batteri1.visEnerginivå())
print("Lager et batteri med energinivå 20 og kapasitet 100")
batteri1 = bk.Batteri(20,100)
print("Forbruker 15")
batteri1.brukEnergi(15)
print("Skal ende opp med energinivå på 5")
print(batteri1.visEnerginivå())

# To mulige feil og ett unntak 
# 1. lading over kapasitet
# 2. forbruk utover energinivået
# 3. feil type input, f.eks. tekst

print()
print("Feil bruk skal flagges og motvirkes")
print("Feil nr 1: lading over kapasiteten")
print("Lager et batteri med energinivå 20 og kapasitet 100")
batteri1 = bk.Batteri(20,100)
print("Lader med 90, havner over maksverdi 100")
batteri1.ladOpp(90)
print("Skal få en advarsel, om at energinivået ikke kan gå over 100")
print(batteri1.visEnerginivå())

print()
print("Feil nr 2: forbruk utover energinivået")
print("Lager et batteri med energinivå 20 og kapasitet 100")
batteri1 = bk.Batteri(20,100)
print("Forbruker 30, havner under minimumsverdi 0")
batteri1.brukEnergi(30)
print("Skal få en advarsel, om at energinivået ikke kan gå under 0")
print(batteri1.visEnerginivå())

print()
print("Feil nr 3: Unntak - Kan ikke bruke tekstverdier")
print("Lager et batteri med energinivå A og kapasitet B, skal få en advarsel om at det ikke går an")
batteri1 = bk.Batteri("A","B")
print("Lader med C, skal få en advarsel om at det ikke går an")
batteri1.ladOpp("C")
print("Forbruker med D, skal få en advarsel om at det ikke går an")
try:
  batteri1.brukEnergi("D")
except:
  print("Exception error: Kan ikke bruke -= på tekst")
print("Energinivå etter forsøk på endringer")
print(batteri1.visEnerginivå())

print(batteri1)

print("6. Flere feil ved opprettelse av objekt")
batteri1 = bk.Batteri(-3,150)
print(batteri1)

batteri1 = bk.Batteri(150,-3)
print(batteri1)

batteri1 = bk.Batteri(40,20)
print(batteri1)

batteri1 = bk.Batteri(100,99)
print(batteri1)