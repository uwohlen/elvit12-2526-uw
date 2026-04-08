import pygame as pg
import random as rd
from pygame.locals import (K_UP, K_DOWN, K_LEFT, K_RIGHT, K_w, K_a, K_s, K_d)

# Initialiserer pygame
pg.init()
VINDU_BREDDE = 630
VINDU_HOYDE  = 630
vindu = pg.display.set_mode([VINDU_BREDDE, VINDU_HOYDE])

# Konstanter 
KVADRAT = 30 # bredde og høyde på firkantene
STARTFART = 0.15 # farten til spillerne

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
            if self.x < 0: # utenfor rammen
                self.x += self.fart
            else:
                self.obj = pg.Rect(self.x, self.y, self.side, self.side)
                if pg.Rect.collidelist(self.obj, hindringer) != -1: # inni en vegg
                    self.x += self.fart    
        if taster[self.styring[3]]: #høyre
            self.x += self.fart
            if self.x + self.side > self.vindusobjekt.get_width(): # utenfor rammen
                self.x -= self.fart
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
            self.fart = 0

    def energi(self, juice, hindringer):
        """
        Drikk nektar, øk fart, ny nektar på ledig plass
        
        Parametre:
            juice (Firkant): nektarobjektet
            hindringer (list): liste med rektangelobjekter for veggene

        """
        if self.obj.colliderect(juice.obj): # treffer nektarfirkant
            self.fart *= 1.05 # øk fart
            # Ny plassering av nektar
            juice.x = rd.randint(0,20)*30 # innenfor den ytre rammen
            juice.y = rd.randint(0,20)*30
            juice.obj = pg.Rect(juice.x, juice.y, juice.side, juice.side)
            nektar_i_vegg = False
            if pg.Rect.collidelist(juice.obj, hindringer) != -1: # inni vegg
                nektar_i_vegg = True
            while nektar_i_vegg: # må velge ny plassering til den er utenfor vegg
                #print(juice.x, juice.y)
                juice.x = rd.randint(0,20)*30
                juice.y = rd.randint(0,20)*30
                juice.obj = pg.Rect(juice.x, juice.y, juice.side, juice.side)
                nektar_i_vegg = False
                if pg.Rect.collidelist(juice.obj, hindringer) != -1:
                    nektar_i_vegg = True
            
        


# Lager objektene
har_n = Spiller(0, 0, KVADRAT, (0,0,255), vindu, STARTFART,[K_w,K_s,K_a,K_d])
jaget = Spiller(600, 600, KVADRAT, (255,0,0), vindu, STARTFART,[K_UP,K_DOWN,K_LEFT,K_RIGHT])
nektar = Firkant(300, 300, KVADRAT, (255,255,0), vindu)

# Posisjon til vegg, delt i firkanter:
veggplass = [
    [],
    [],
    [2,3,4,5,6,7,8,12,13,14,15,16,17,18],
    [],
    [],
    [5],
    [5],
    [5],
    [5,8,9,10,11,12,15],
    [5,15],
    [5,15],
    [5,15],
    [5,8,9,10,11,12,15],
    [15],
    [15],
    [15],
    [],
    [],
    [2,3,4,5,6,7,8,12,13,14,15,16,17,18],
    [],
    []
]

# Lager vegg-objekter til hver posisjon

vegger = [] # liste med vegg-firkanter som kan tegnes
veggerobj = [] # liste med vegg-Rect-objekter for kollisjonsdeteksjon

for i in range(len(veggplass)):
    for j in range(len(veggplass[i])):
        vegg = Firkant(veggplass[i][j]*KVADRAT, i*KVADRAT, KVADRAT, (0,0,0), vindu)
        vegger.append(vegg)
        veggerobj.append(vegg.obj)


# Gjenta helt til brukeren lukker vinduet
fortsett = True
teller = 0
while fortsett:

    # Spilleren som blir jaget mister fart
    # justeres til et nivå som passer maskinen det spilles på
    teller += 1
    if teller % 10000 == 0: # for hver 10 000 gang while-løkken kjører
                            # tiden det tar vil variere med hvor travel maskinen er
                            # justeres manuelt til man er fornøyd med utviklingen
        jaget.fart *= 0.95 # mister 5 %


    # Sjekker om brukeren har lukket vinduet
    for event in pg.event.get():
        if event.type == pg.QUIT:
            fortsett = False

    # Henter en ordbok med status for alle tastatur-taster
    trykkede_taster = pg.key.get_pressed()
    
    # Farger hele spillebrettet grått
    vindu.fill((200, 200, 200))

    # Tegner vegger
    for i in range(len(vegger)):
        vegger[i].tegn()

    # Tegner og flytter spillerne
    har_n.tegn()
    har_n.flytt(trykkede_taster, veggerobj)
    jaget.tegn()
    jaget.flytt(trykkede_taster, veggerobj)

    # Behandler nektar
    nektar.tegn()
    jaget.energi(nektar, veggerobj)
    har_n.energi(nektar, veggerobj)
    
    # Sjekker kollisjon mellom spillere
    har_n.kollisjonsdeteksjon(jaget)
    
    # Oppdaterer alt innholdet i vinduet
    pg.display.flip()

# Avslutter pygame
pg.quit()
