##################################
# IMPORT. START pygame           #
##################################

import pygame as pg
import sys
import math
pg.init()

from pygame.locals import (K_q, K_x)
import minesveiper_klasser_v2 as pk

######################################
# KONSTANTER, VINDU og FONT          #
######################################

# Spillebrettets størrelse og konstanter
# 9x9 med 10 miner
# 16x16 med 40 miner
# 30x16 med 99 miner

ANTALLX = 9
ANTALLY = 9
ANTALL_MINER = 10
RUTE_SIDE = 30 # NB! Bildene er 30x30 piksler, hvis denne endres må bildene skaleres
MENY_HOYDE = 100 # for nedtelling og klokke
VINDU_BREDDE = ANTALLX*RUTE_SIDE
VINDU_HOYDE = ANTALLY*RUTE_SIDE + MENY_HOYDE
FARGER = ["lightgray","blue","darkgreen","red","darkblue","brown","cyan","black","gray"]

vindu = pg.display.set_mode((VINDU_BREDDE,VINDU_HOYDE))

pg.display.set_caption("Oppgave animasjon")
font_knapp = pg.font.SysFont("Arial",20,bold=True)
klokke = pg.time.Clock()
tid = -1



###########################
# OBJEKTER                #
###########################

spillebrett = pk.Rutenett(vindu,ANTALLX,ANTALLY,ANTALL_MINER)
spillebrett.lag_nytt_rutenett(font_knapp,FARGER[0])
spillebrett.lag_miner()
spillebrett.tell_nabo_miner()

meny = pk.Firkant(vindu,0,0,VINDU_BREDDE,100,"lightgray")
nedtelling = pk.Knapp(vindu,20,30,60,40,"black",font_knapp,ANTALL_MINER)
tidsrute = pk.Knapp(vindu,VINDU_BREDDE-80,30,60,40,"black",font_knapp,tekst=0)
restart = pk.Firkant(vindu,VINDU_BREDDE/2-22,28,44,44,"lightgray")



#### Sjekker at startverdiene er på plass ####
def vis_miner():
  for i in range(len(spillebrett.ruter)):
    for j in range(len(spillebrett.ruter[0])):
      #print(f"{spillebrett.ruter[i][j].farge:9}",end=" ")
      print(f"{spillebrett.ruter[i][j].mine:9}",end=" ")
      #print(f"{spillebrett.ruter[i][j].tekst:9}",end=" ")
    print()
  print()

def vis_tekst():
  for i in range(len(spillebrett.ruter)):
    for j in range(len(spillebrett.ruter[0])):
      #print(f"{spillebrett.ruter[i][j].farge:9}",end=" ")
      #print(f"{spillebrett.ruter[i][j].mine:9}",end=" ")
      print(f"{spillebrett.ruter[i][j].tekst:9}",end=" ")
    print()
  print()

#vis_miner()
#vis_tekst()

###########################
# WHILE                   #
###########################

def tell_denne(brett,xpos,ypos):
  """
  Funksjon for gjentakende kode: endring av farge og telling av viste ruter
  """
  if brett.ruter[xpos][ypos].farge == "lightgray" and brett.ruter[xpos][ypos].status == "":
    brett.ruter[xpos][ypos].farge = "darkgray"
    brett.ruter[xpos][ypos].visning = True
    brett.vist += 1

# Startverdier
klikk = False
rklikk = False
flat = False
fortsett = True


# Spill-løkka

while True:

  ###################
  # TID             #
  ###################

  # Tiden går med 10 frames pr sekund, dvs. legger til 0.1 sekund hver runde.
  # Teller ikke tider over 999 sekunder
  # Tiden starter når man klikker på noe første gang
  if fortsett and tid >= 0 and tid <= 999:
    tid += 0.1
    tidsrute.tekst = str(round(tid,0))[:-2]

  ###################
  # BRUKER-INPUT    #
  ###################

  # Hendelser
  for event in pg.event.get():
    if event.type == pg.QUIT:
      pg.quit()
      sys.exit()

    elif event.type == pg.MOUSEBUTTONDOWN:
      # Starter tiden
      # posisjon for 3D-effekt av å trykke på knapp, ikke aktiv for høyreklikk
      if fortsett:
        if tid == -1:
          tid = 0
 
        #print(event.button)
        # venstre: 1, midten/musehjul: 2, høyre: 3
        if event.button == 1:
          p, q = pg.mouse.get_pos()
          flat = True

    elif event.type == pg.MOUSEBUTTONUP:
      # posisjon for visning av valgte knapp
      flat = False
      if event.button == 1: # mus venstreklikk, touchpad-klikk med en finger
        x, y = pg.mouse.get_pos()
        klikk = True
      elif event.button == 3: # mus høyreklikk, touchpad-høyre-klikk med to fingre
        w, z = pg.mouse.get_pos()
        rklikk = True
      else:
        print("Ikke riktig type klikk")

  trykkede_taster = pg.key.get_pressed()
  if trykkede_taster[K_q] or trykkede_taster[K_x]:
    pg.quit()
    sys.exit()

  #####################
  # OPPDATERINGER     #
  #####################

  vindu.fill("lightgray")
  pg.display.set_caption("Minesveiper")

  ################################################################
  # LAR EFFEKTEN AV Å TRYKKE PÅ EN TOM RUTE SPRE SEG UTOVER      #
  ################################################################
  for i in range(ANTALLY):
    for j in range(ANTALLX):
      # ruten vises, det er ikke en mine, den har ingen miner rundt seg, og den er ikke markert som "her er det en mine" eller ?
      if spillebrett.ruter[i][j].visning and spillebrett.ruter[i][j].mine == False and spillebrett.ruter[i][j].tekst == 0 and spillebrett.ruter[i][j].status == "":
        # er det en uklikket over?
          if i > 0:
            tell_denne(spillebrett,i-1,j) # vis ruten over, hvis den ikke allerede er vist eller markert
          # er det en tomt til høyre?
          if j < spillebrett.antall_x - 1:
            tell_denne(spillebrett,i,j+1)
          # er det en tomt under?
          if i < spillebrett.antall_y - 1:
            tell_denne(spillebrett,i+1,j)
          # er det en tomt til venstre?
          if j > 0:
            tell_denne(spillebrett,i,j-1)
          # er det en tomt over til venstre?
          if i > 0 and j > 0:
            tell_denne(spillebrett,i-1,j-1)
          # er det en tomt over til høyre?
          if i > 0 and j < spillebrett.antall_x - 1:
            tell_denne(spillebrett,i-1,j+1)
          # er det en tomt under til høyre?
          if i < spillebrett.antall_y - 1 and j < spillebrett.antall_x - 1:
            tell_denne(spillebrett,i+1,j+1)
          # er det en tomt under til venstre?
          if i < spillebrett.antall_y - 1 and j > 0:
            tell_denne(spillebrett,i+1,j-1)
          
  ##################################
  # SJEKKER HVER RUTE FOR KLIKK    #
  ##################################
  for i in range(ANTALLY):
    for j in range(ANTALLX):

      #### STOPP ELLER VIS ####
      if klikk and fortsett and spillebrett.ruter[i][j].obj.collidepoint(x,y):
        # Traff mine - stopp spillet (markerte ruter reagerer ikke på klikk)
        if spillebrett.ruter[i][j].mine and spillebrett.ruter[i][j].status == "":
          spillebrett.ruter[i][j].farge = "red"
          fortsett = False
        else:
          tell_denne(spillebrett,i,j) 
        klikk = False
      
      #### MARKER RUTER SOM "HER ER DET EN MINE" ELLER "?" ####
      # høyreklikk på ruta, og den er ikke allerede vanlig klikket på
      elif rklikk and fortsett and spillebrett.ruter[i][j].obj.collidepoint(w,z) and spillebrett.ruter[i][j].visning == False:
        if spillebrett.ruter[i][j].status == "":
          spillebrett.ruter[i][j].status = "mine"
          nedtelling.tekst -= 1
        elif spillebrett.ruter[i][j].status == "mine":
          spillebrett.ruter[i][j].status = "?"
          nedtelling.tekst += 1
        elif spillebrett.ruter[i][j].status == "?":
          spillebrett.ruter[i][j].status = ""
        rklikk = False
        
      ##############################################################
      # OPPDATER TEGNINGEN AV RUTER OG VISNING AV ANTALL MINER     #
      ##############################################################
      if spillebrett.ruter[i][j].farge == "lightgray":
        # 3D-effekt når man trykker knappen ned så er den flat, helt til man slipper knappen opp igjen
        if flat and fortsett and spillebrett.ruter[i][j].obj.collidepoint((p,q)):
          spillebrett.ruter[i][j].tegn()
        else:
          # 3D-visning når knappen ikke er trykket på
          spillebrett.ruter[i][j].tegn3D("gray50","gray95",kant=4)
      else: # ikke lysegrå
        # ferdigtrykte knapper er flate
        spillebrett.ruter[i][j].tegn()
      
      # Vis antall miner som ligger rundt for åpna ruter
      if spillebrett.ruter[i][j].visning and spillebrett.ruter[i][j].tekst != 0:
        farge = FARGER[spillebrett.ruter[i][j].tekst]
        spillebrett.ruter[i][j].vis_tekst(farge)

      # tegn mineflagg eller ? for markerte ruter
      if spillebrett.ruter[i][j].status == "mine":
        bilde = pg.image.load("mineflagg.png")
        vindu.blit(bilde,(spillebrett.ruter[i][j].x,spillebrett.ruter[i][j].y))
      elif spillebrett.ruter[i][j].status == "?":
        spillebrett.ruter[i][j].vis_tekst(tekst="?")

      # Rutenett - kantstreker i kontrastfarge som viser rutene også når de er flate
      spillebrett.ruter[i][j].tegn(bredde=1,farge="gray")
  
  #######################################################################
  # RESTART-KNAPPEN (gul sirkel, skal egentlig være animert smilefjes)  #
  #######################################################################
  if klikk and restart.obj.collidepoint((x,y)):
    # Fjern rutene og lag spillebrettet på nytt
    spillebrett.ruter = []
    spillebrett.lag_nytt_rutenett(font_knapp,FARGER[0])
    spillebrett.lag_miner()
    spillebrett.tell_nabo_miner()
    # sett alle variabler til startverdiene
    spillebrett.vist = 0
    tid = -1
    tidsrute.tekst = 0
    nedtelling.tekst = ANTALL_MINER
    fortsett = True
    klikk = False
    rklikk = False
    flat = False
  
  ###########################
  # VANT                    #
  ###########################
  # Hvis man har funnet alle ruter uten mine: stopp spillet
  if spillebrett.vist == spillebrett.antall_x*spillebrett.antall_y - spillebrett.antall_miner:
    fortsett = False
  
  ###########################
  # SLUTT                   #
  ###########################
  # Visning av mine-plasseringene
  if fortsett == False:
    for i in range(ANTALLY):
      for j in range(ANTALLX):
        if spillebrett.ruter[i][j].mine:
          # Vant (eller korrekt merket som mine)
          if spillebrett.vist == spillebrett.antall_x*spillebrett.antall_y - spillebrett.antall_miner or spillebrett.ruter[i][j].status == "mine":
            bilde = pg.image.load("mineflagg.png")
            nedtelling.tekst = 0
          # Tapte
          elif spillebrett.ruter[i][j].farge == "red":
            bilde = pg.image.load("bombe_rod.png")
          else:
            bilde = pg.image.load("bombe_graa.png")
          vindu.blit(bilde,(spillebrett.ruter[i][j].x,spillebrett.ruter[i][j].y))
        # Feilaktig markert som mine: vis bombe med rødt kryss over
        elif spillebrett.ruter[i][j].status == "mine":
          bilde = pg.image.load("bombe_graa.png")
          vindu.blit(bilde,(spillebrett.ruter[i][j].x,spillebrett.ruter[i][j].y))
          pg.draw.line(vindu,"red",(spillebrett.ruter[i][j].x,spillebrett.ruter[i][j].y),(spillebrett.ruter[i][j].x+spillebrett.ruter[i][j].bredde,spillebrett.ruter[i][j].y+spillebrett.ruter[i][j].hoyde),width=4)
          pg.draw.line(vindu,"red",(spillebrett.ruter[i][j].x,spillebrett.ruter[i][j].y+spillebrett.ruter[i][j].hoyde),(spillebrett.ruter[i][j].x+spillebrett.ruter[i][j].bredde,spillebrett.ruter[i][j].y),width=4)
  
  #########################################################
  # MENY: ANTALL MINER SOM GJENSTÅR, TID I SEKUNDER       #
  #########################################################
  # Meny-rute, 3D-effekt motsatt vei (innover, hvis knappene står utover)
  pg.draw.rect(vindu,"gray95",(5,5,VINDU_BREDDE-10,90))
  pg.draw.polygon(vindu,"gray50",((5,5),(VINDU_BREDDE-5,5),(VINDU_BREDDE-10,10),(10,90),(5,95)))
  pg.draw.rect(vindu,"lightgray",(11,10,VINDU_BREDDE-20,80))

  nedtelling.tegn()
  nedtelling.vis_tekst(farge="red")
  tidsrute.tegn()
  tidsrute.vis_tekst(farge="red")

  restart.tegn3D("gray50","gray95",kant=4)
  # Skal egentlig være et animert smilefjes
  pg.draw.circle(vindu,"yellow",(VINDU_BREDDE/2,50),15)
  pg.draw.circle(vindu,"black",(VINDU_BREDDE/2,50),15,width=1)
  # Pil
  pg.draw.arc(vindu,"black",(VINDU_BREDDE/2-7,43,14,14),3*math.pi/2,7*math.pi/6,1)
  pg.draw.line(vindu,"black",(VINDU_BREDDE/2-7,53),(VINDU_BREDDE/2-4,48))
  pg.draw.line(vindu,"black",(VINDU_BREDDE/2-7,53),(VINDU_BREDDE/2-10,48))

  #####################
  # OPPDATER VINDU    #
  #####################
  pg.display.flip()
  klokke.tick(10) # 10 fps
