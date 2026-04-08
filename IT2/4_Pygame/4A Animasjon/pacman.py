import pygame as pg
import random as rd
from pygame.locals import (K_UP, K_DOWN, K_LEFT, K_RIGHT, K_w, K_a, K_s, K_d)

# Konstanter 
KVADRAT = 20 # bredde og høyde på firkantene
STARTFART = 0.5 # farten til spillerne

# Initialiserer pygame
pg.init()
VINDU_BREDDE = KVADRAT*28
VINDU_HOYDE  = KVADRAT*31
vindu = pg.display.set_mode([VINDU_BREDDE, VINDU_HOYDE])


class Firkant:
    """
    Firkanter kan tegnes på skjermen, står i ro
    
    Parametre:
        x (int): firkantens x-posisjon på spillebrettet
        y (int): firkantens y-posisjon på spillebrettet
        side (int): firkantens bredde og høyde
        farge (RGB-tuppel): firkantens farge
        vindusobjekt (pygame.Surface): spillebrettet
    
    Flere egenskaper:
        obj (pygame.Rect): rektangelobjekt for kollisjonsdeteksjon

    Metoder:
        tegn(self): tegner firkanten i vindusobjektet
        
    """
    def __init__(self, x:int, y:int, side:int, farge, vindusobjekt):
        self.x = x
        self.y = y
        self.side = side # bredde og høyde på firkantene
        self.farge = farge
        self.vindusobjekt = vindusobjekt
        #objekt for kollisjonsdeteksjon:
        self.obj = pg.Rect(self.x, self.y, self.side, self.side)

    def tegn(self):
        """Tegner firkanten"""
        pg.draw.rect(self.vindusobjekt, self.farge, (self.x, self.y, self.side, self.side))

    def tegnsirkel(self, radius):
        pg.draw.circle(self.vindusobjekt,self.farge,(self.x+KVADRAT/2,self.y+KVADRAT/2),radius)

class Spiller(Firkant):
    """
    Spillere kan tegnes på skjermen, flytte på seg og sjekke kollisjoner
    
    Subklasse av Firkant

    Parametre:
        x (int): firkantens x-posisjon på spillebrettet
        y (int): firkantens y-posisjon på spillebrettet
        side (int): firkantens bredde og høyde
        farge (RGB-tuppel): firkantens farge
        vindusobjekt (pygame.Surface): spillebrettet
        fart (float): firkantens fart i x- og y-retning
        styring (list): liste med taster for å styre spilleren [opp,ned,venstre,høyre]
    
    Flere egenskaper:
        obj (pygame.Rect): rektangelobjekt for kollisjonsdeteksjon

    Metoder:
        tegn(self): tegner firkanten i vindusobjektet
        flytt(self, taster, hindringer): flytter firkanten, sjekker mot vegger
        kollisjonsdeteksjon(self, motspiller): stopper spillet ved kollisjon
        energi(self, juice, hindringer): gir større fart ved kollisjon, flytter nektarfirkanten
    
    """
    def __init__(self, x, y, side, farge, vindusobjekt, fart, styring):
        super().__init__(x, y, side, farge, vindusobjekt)
        self.fart = fart  
        self.styring = styring

    def flytt(self, taster, hindringer):
        """
        Flytter spiller, sjekker kollisjon mot vegger
        
        Parametre:
            taster (pygame.key.ScancodeWrapper): tastaturtilstand fra pygame.key.get_pressed()
            hindringer (list): liste med rektangelobjekter for veggene

        """
        if taster[self.styring[0]]: #opp
            # ny posisjon
            self.y -= self.fart
            if self.y < 0: # utenfor rammen
                self.y += self.fart # gå tilbake
            else:
                self.obj = pg.Rect(self.x, self.y, self.side, self.side)
                if pg.Rect.collidelist(self.obj, hindringer) != -1: # inni en vegg
                    self.y += self.fart        
        if taster[self.styring[1]]: #ned
            self.y += self.fart
            if self.y + self.side > self.vindusobjekt.get_height(): # utenfor rammen
                self.y -= self.fart
            else:
                self.obj = pg.Rect(self.x, self.y, self.side, self.side)
                if pg.Rect.collidelist(self.obj, hindringer) != -1: # inni en vegg
                    self.y -= self.fart    
        if taster[self.styring[2]]: #venstre
            self.x -= self.fart
            if self.x < -KVADRAT: # utenfor rammen
                self.x = self.vindusobjekt.get_width() + KVADRAT # kom inn igjen fra motsatt side
            else:
                self.obj = pg.Rect(self.x, self.y, self.side, self.side)
                if pg.Rect.collidelist(self.obj, hindringer) != -1: # inni en vegg
                    self.x += self.fart    
        if taster[self.styring[3]]: #høyre
            self.x += self.fart
            if self.x + self.side > self.vindusobjekt.get_width() + KVADRAT: # utenfor rammen
                self.x = -KVADRAT # kom inn igjen fra motsatt side
            else:
                self.obj = pg.Rect(self.x, self.y, self.side, self.side)
                if pg.Rect.collidelist(self.obj, hindringer) != -1: # inni en vegg
                    self.x -= self.fart    
        self.obj = pg.Rect(self.x, self.y, self.side, self.side)

    def kollisjonsdeteksjon(self, motspiller):
        """
        Sjekker om spillerne krasjer, stopper spillet
        
        Parametre:
            motspiller (Spiller): den andre spilleren
        
        """
        if self.obj.colliderect(motspiller.obj):
            # Stopp all bevegelse
            motspiller.fart = 0 

    def energi(self, juice, juiceobj, motspiller):
        """
        Drikk nektar, øk fart, ny nektar på ledig plass
        
        Parametre:
            juice (Firkant): nektarobjektet
            hindringer (list): liste med rektangelobjekter for veggene

        """
        
        indeks = pg.Rect.collidelist(self.obj, juiceobj)
        if indeks != -1:
            juice.pop(indeks)
            juiceobj.pop(indeks)
        if len(juice) == 0:
            motspiller.fart = 0

           
    def dytt(self, har_n,send_hjem, send_hjem_obj):
        """
        Når pacman spiser den store sirkelen, sendes spøkelset hjem
        """ 
        indeks = pg.Rect.collidelist(self.obj, send_hjem_obj)
        if indeks != -1:
            send_hjem.pop(indeks)
            send_hjem_obj.pop(indeks)
            har_n.x = KVADRAT*13.5
            har_n.y = KVADRAT*13.5


class Monster(Firkant):
    """
    Spillere kan tegnes på skjermen, flytte på seg og sjekke kollisjoner
    
    Subklasse av Firkant

    Parametre:
        x (int): firkantens x-posisjon på spillebrettet
        y (int): firkantens y-posisjon på spillebrettet
        side (int): firkantens bredde og høyde
        farge (RGB-tuppel): firkantens farge
        vindusobjekt (pygame.Surface): spillebrettet
        fart (float): firkantens fart i x- og y-retning
        styring (list): liste med taster for å styre spilleren [opp,ned,venstre,høyre]
    
    Flere egenskaper:
        obj (pygame.Rect): rektangelobjekt for kollisjonsdeteksjon

    Metoder:
        tegn(self): tegner firkanten i vindusobjektet
        flytt(self, taster, hindringer): flytter firkanten, sjekker mot vegger
        kollisjonsdeteksjon(self, motspiller): stopper spillet ved kollisjon
        energi(self, juice, hindringer): gir større fart ved kollisjon, flytter nektarfirkanten
    
    """
    def __init__(self, x, y, side, farge, vindusobjekt, fart, styring):
        super().__init__(x, y, side, farge, vindusobjekt)
        self.fart = fart  
        self.styring = styring

    def flytt(self, taster, hindringer):
        """
        Flytter spiller, sjekker kollisjon mot vegger
        
        Parametre:
            taster (pygame.key.ScancodeWrapper): tastaturtilstand fra pygame.key.get_pressed()
            hindringer (list): liste med rektangelobjekter for veggene

        """
        if taster[self.styring[0]]: #opp
            # ny posisjon
            self.y -= self.fart
            if self.y < 0: # utenfor rammen
                self.y += self.fart # gå tilbake
            else:
                self.obj = pg.Rect(self.x, self.y, self.side, self.side)
                if pg.Rect.collidelist(self.obj, hindringer) != -1: # inni en vegg
                    self.y += self.fart        
        if taster[self.styring[1]]: #ned
            self.y += self.fart
            if self.y + self.side > self.vindusobjekt.get_height(): # utenfor rammen
                self.y -= self.fart
            else:
                self.obj = pg.Rect(self.x, self.y, self.side, self.side)
                if pg.Rect.collidelist(self.obj, hindringer) != -1: # inni en vegg
                    self.y -= self.fart    
        if taster[self.styring[2]]: #venstre
            self.x -= self.fart
            if self.x < -KVADRAT: # utenfor rammen
                self.x = self.vindusobjekt.get_width() + KVADRAT # kom inn igjen fra motsatt side
            else:
                self.obj = pg.Rect(self.x, self.y, self.side, self.side)
                if pg.Rect.collidelist(self.obj, hindringer) != -1: # inni en vegg
                    self.x += self.fart    
        if taster[self.styring[3]]: #høyre
            self.x += self.fart
            if self.x + self.side > self.vindusobjekt.get_width() + KVADRAT: # utenfor rammen
                self.x = -KVADRAT # kom inn igjen fra motsatt side
            else:
                self.obj = pg.Rect(self.x, self.y, self.side, self.side)
                if pg.Rect.collidelist(self.obj, hindringer) != -1: # inni en vegg
                    self.x -= self.fart    
        self.obj = pg.Rect(self.x, self.y, self.side, self.side)

    def kollisjonsdeteksjon(self, motspiller):
        """
        Sjekker om spillerne krasjer, stopper spillet
        
        Parametre:
            motspiller (Spiller): den andre spilleren
        
        """
        if self.obj.colliderect(motspiller.obj):
            # Stopp all bevegelse
            motspiller.fart = 0 

         
    def dytt(self, har_n,send_hjem, send_hjem_obj):
        """
        Når pacman spiser den store sirkelen, sendes spøkelset hjem
        """ 
        indeks = pg.Rect.collidelist(self.obj, send_hjem_obj)
        if indeks != -1:
            send_hjem.pop(indeks)
            send_hjem_obj.pop(indeks)
            har_n.x = KVADRAT*13.5
            har_n.y = KVADRAT*13.5


# Lager objektene
har_n = Monster(KVADRAT*13.5, KVADRAT*13.5, KVADRAT, (255,0,0), vindu, STARTFART*1.2,[K_w,K_s,K_a,K_d])
jaget = Spiller(round(KVADRAT*13.5), round(KVADRAT*23), KVADRAT, (255,255,0), vindu, STARTFART,[K_UP,K_DOWN,K_LEFT,K_RIGHT])

# Posisjon til vegg, delt i firkanter:
# 28 x 31 ruter
r0 = []
for i in range(28):
    r0.append(i)

r1 = [0,13,14,27]
r2 = [0,2,3,4,5,7,8,9,10,11,13,14,16,17,18,19,20,22,23,24,25,27]
r5 = [0,27]
r6 = [0,2,3,4,5,7,8,10,11,12,13,14,15,16,17,19,20,22,23,24,25,27]
r8 = [0,7,8,13,14,19,20,27]
r9 = []
for i in range(28):
    if i not in [6,12,15,21]:
        r9.append(i)
r11 = [0,1,2,3,4,5,7,8,19,20,22,23,24,25,26,27]
r12 = []
for i in range(28):
    if i not in [6,9,13,14,18,21]:
        r12.append(i)
r14 = [10,17]
r15 = []
for i in range(28):
    if i not in [6,9,18,21]:
        r15.append(i)
r18 = []
for i in range(28):
    if i not in [6,9,18,21]:
        r18.append(i)
r23 = [0,4,5,22,23,27]
r24 = []
for i in range(28):
    if i not in [3,6,9,18,21,24]:
        r24.append(i)
r27 = []
for i in range(28):
    if i not in [1,12,15,26]:
        r27.append(i)

veggplass = [r0,r1,r2,r2,r2,r5,r6,r6,r8,r9,r9,r11,r12,r12,r14,r15,r15,r11,r18,r18,r1,r2,r2,r23,r24,r24,r8,r27,r27,r5,r0]

# Lager vegg-objekter til hver posisjon

vegger = [] # liste med vegg-firkanter som kan tegnes
vegger_obj = [] # liste med vegg-Rect-objekter for kollisjonsdeteksjon

for i in range(len(veggplass)):
    for j in range(len(veggplass[i])):
        vegg = Firkant(veggplass[i][j]*KVADRAT, i*KVADRAT, KVADRAT, (0,0,255), vindu)
        vegger.append(vegg)
        vegger_obj.append(vegg.obj)

nektar = []
nektar_obj = []
for i in range(len(veggplass)):
    for j in range(len(veggplass[0])):
        if j not in veggplass[i] and (i < 9 or i > 19) and [j,i] not in [[1,3,],[26,3,],[1,23],[26,23]] or j in [6,21] and i >= 9 and i <= 19 :
            x=KVADRAT*j
            y=KVADRAT*i
            nektarin = Firkant(x+KVADRAT*3/8, y+KVADRAT*3/8, KVADRAT/4, (255,200,200), vindu)
            nektar.append(nektarin)
            nektar_obj.append(nektarin.obj)

send_hjem = []
send_hjem_obj = []
for [i,j] in [[1,3,],[26,3,],[1,23],[26,23]]:
    hjem = Firkant(i*KVADRAT,j*KVADRAT,KVADRAT,(255,150,150), vindu)
    send_hjem.append(hjem)
    send_hjem_obj.append(hjem.obj)



# Gjenta helt til brukeren lukker vinduet
fortsett = True
teller = 0
while fortsett:

    # Sjekker om brukeren har lukket vinduet
    for event in pg.event.get():
        if event.type == pg.QUIT:
            fortsett = False

    # Henter en ordbok med status for alle tastatur-taster
    trykkede_taster = pg.key.get_pressed()
    
    # Farger hele spillebrettet svart
    vindu.fill((0,0,0))

    # Tegner vegger
    for i in range(len(vegger)):
        vegger[i].tegn()

    # Tegner nektar
    for i in range(len(nektar)):
        nektar[i].tegn()
    for i in range(len(send_hjem)):
        send_hjem[i].tegnsirkel(KVADRAT*4/10)
    
    # Tegner og flytter spillerne
    if har_n.fart != 0:
        har_n.tegn()
        har_n.flytt(trykkede_taster, vegger_obj)
        #har_n.energi(nektar,nektar_obj,har_n)
        
    if jaget.fart != 0:
        jaget.tegnsirkel(KVADRAT/2)
        jaget.flytt(trykkede_taster, vegger_obj)
        jaget.energi(nektar,nektar_obj,har_n)
        jaget.dytt(har_n,send_hjem,send_hjem_obj)

    if har_n.fart != 0 and jaget.fart != 0:
        # Sjekker kollisjon mellom spillere
        har_n.kollisjonsdeteksjon(jaget)
        
    # Oppdaterer alt innholdet i vinduet
    pg.display.flip()

# Avslutter pygame
pg.quit()
