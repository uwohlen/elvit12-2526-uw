import pygame as pg
import random as rd
from pygame.locals import (K_q, K_r, K_n)

# Konstanter 
SVART = (0,0,0)
HVIT = (255,255,255)
GRAA = (150,150,150)
FRAMES_PER_SECOND = 3
ANTALL = 20
KVADRAT = 20
VINDU_BREDDE = ANTALL*KVADRAT
VINDU_HOYDE  = VINDU_BREDDE

# Initialiserer pygame
pg.init()
vindu = pg.display.set_mode([VINDU_BREDDE, VINDU_HOYDE])
clock = pg.time.Clock()

class Firkant:
    """
    Firkanter kan tegnes på skjermen, teller nabofarger, skifter farge
    
    Parametre
        i (int): rad (y-retning)
        j (int): kolonne (x-retning)
        side (int): firkantens bredde og høyde
        farge (RGB-tuppel): firkantens farge
        vindusobjekt (pygame.Surface): spillebrettet
        nabotype(int): om firkanten er i et hjørne eller midt på
    
    Flere egenskaper:
        x (int): firkantens x-posisjon på spillebrettet
        y (int): firkantens y-posisjon på spillebrettet
        obj (pygame.Rect): rektangelobjekt
        naboer (int): antall naboer som lever

    Metoder:
        tegn(self): tegner firkanten i vindusobjektet
        
    """
    def __init__(self, i:int, j:int, side:int, farge, vindusobjekt,nabotype):
        self.i = i
        self.j = j
        self.x = j*side
        self.y = i*side
        self.side = side # bredde og høyde på firkantene
        self.farge = farge
        self.vindusobjekt = vindusobjekt
        self.nabotype = nabotype
        self.naboer = 0
        #objekt:
        self.obj = pg.Rect(self.x, self.y, self.side, self.side)

    def tegn(self):
        """Tegner firkanten"""
        pg.draw.rect(self.vindusobjekt, self.farge, (self.x, self.y, self.side, self.side))

    def tellnaboer(self,alle):
        self.naboer = 0
        if self.nabotype == 0:
            for a in range(0,2):
                for b in range(0,2):
                    if alle[self.i+a][self.j +b].farge == SVART:
                        if not(a==0 and b==0):
                            self.naboer += 1

        elif self.nabotype == 1:
            for a in range(0,2):
                for b in range(-1,2):
                    if alle[self.i+a][self.j +b].farge == SVART:
                        if not(a==0 and b==0):
                            self.naboer += 1
            
        elif self.nabotype == 2:
            for a in range(0,2):
                for b in range(-1,1):
                    if alle[self.i+a][self.j +b].farge == SVART:
                        if not(a==0 and b==0):
                            self.naboer += 1

        elif self.nabotype == 3:
            for a in range(-1,2):
                for b in range(0,2):
                    if alle[self.i+a][self.j +b].farge == SVART:
                        if not(a==0 and b==0):
                            self.naboer += 1

        elif self.nabotype == 4:
            for a in range(-1,2):
                for b in range(-1,2):
                    if alle[self.i+a][self.j +b].farge == SVART:
                        if not(a==0 and b==0):
                            self.naboer += 1
        
        elif self.nabotype == 5:
            for a in range(-1,2):
                for b in range(-1,1):
                    if alle[self.i+a][self.j +b].farge == SVART:
                        if not(a==0 and b==0):
                            self.naboer += 1

        elif self.nabotype == 6:
            for a in range(-1,1):
                for b in range(0,2):
                    if alle[self.i+a][self.j +b].farge == SVART:
                        if not(a==0 and b==0):
                            self.naboer += 1

        elif self.nabotype == 7:
            for a in range(-1,1):
                for b in range(-1,2):
                    if alle[self.i+a][self.j +b].farge == SVART:
                        if not(a==0 and b==0):
                            self.naboer += 1

        elif self.nabotype == 8:
            for a in range(-1,1):
                for b in range(-1,1):
                    if alle[self.i+a][self.j +b].farge == SVART:
                        if not(a==0 and b==0):
                            self.naboer += 1

        

    def skiftfarge(self):
        if self.naboer == 3:
            self.farge = SVART
        elif self.naboer != 2:
            self.farge = HVIT


# Lager objektene

ruter = [] # liste med firkanter som kan tegnes
objekter = [] # liste med Rect-objekter

for i in range(ANTALL):
    ruter.append([])
    objekter.append([])
    for j in range(ANTALL):
        if rd.randint(0,2) == 0:
            tilstand = SVART
        else:
            tilstand = HVIT
        if i==0 and j==0:
            ntype = 0
        elif i==0 and j<ANTALL-1:
            ntype = 1
        elif i==0 and j==ANTALL-1:
            ntype = 2
        elif i<ANTALL-1 and j==0:
            ntype = 3
        elif i<ANTALL-1 and j<ANTALL-1:
            ntype = 4
        elif i<ANTALL-1 and j==ANTALL-1:
            ntype = 5
        elif i==ANTALL-1 and j==0:
            ntype = 6
        elif i==ANTALL-1 and j<ANTALL-1:
            ntype = 7
        elif i==ANTALL-1 and j==ANTALL-1:
            ntype = 8
        else:
            print("Feil ntype")
        rute = Firkant(i, j, KVADRAT, tilstand, vindu,ntype)
        ruter[i].append(rute)
        objekter[i].append(rute.obj)

#print(len(ruter),ruter[1][1].farge)

# Farger hele spillebrettet grått
vindu.fill(GRAA)

for i in range(len(ruter)):
    for j in range(len(ruter[i])):
        ruter[i][j].tegn()

for i in range(len(ruter)):
    for j in range(len(ruter[i])):
        ruter[i][j].tellnaboer(ruter)
        #print(ruter[i][j].naboer)

pg.display.flip()



# Gjenta helt til brukeren lukker vinduet
fortsett = True
while fortsett:

    # Sjekker om brukeren har lukket vinduet
    for event in pg.event.get():
        if event.type == pg.QUIT:
            fortsett = False

        elif event.type == pg.KEYUP:

            if event.key == K_q: # quit
                fortsett = False

            elif event.key == K_r: # reset
                vindu.fill(GRAA)
                for i in range(len(ruter)):
                    for j in range(len(ruter[i])):
                        if rd.randint(0,2) == 0:
                            tilstand = SVART
                        else:
                            tilstand = HVIT
                        ruter[i][j].farge = tilstand
                        ruter[i][j].tegn()
                for i in range(len(ruter)):
                    for j in range(len(ruter[i])):
                            ruter[i][j].tellnaboer(ruter)
                            print(ruter[i][j].naboer)

            elif event.key == K_n: # neste generasjon
                vindu.fill(GRAA)

                for i in range(len(ruter)):
                    for j in range(len(ruter[i])):
                            ruter[i][j].skiftfarge()

                for i in range(len(ruter)):
                    for j in range(len(ruter[i])):
                        ruter[i][j].tegn()
                        ruter[i][j].tellnaboer(ruter)

                


    
    # Tegner ruter
    vindu.fill(GRAA)

    for i in range(len(ruter)):
        for j in range(len(ruter[i])):
                ruter[i][j].skiftfarge()

    for i in range(len(ruter)):
        for j in range(len(ruter[i])):
            ruter[i][j].tegn()
            ruter[i][j].tellnaboer(ruter)
            
    # Oppdaterer alt innholdet i vinduet
    #pg.display.flip()
    pg.display.update()

    # 12 - Slow things down a bit
    clock.tick(FRAMES_PER_SECOND)  # make pygame wait


# Avslutter pygame
pg.quit()
