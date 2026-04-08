"""
Lager en firkant man kan klikke på - for deretter å skrive tekst
- mangler en blinkende cursor for brukervennlighet
Lagd av Osloskolen-GPT, ki.osloskolen.no 
"""

import pygame
import sys

# Initialiser Pygame
pygame.init()

# Sett opp vindu
screen = pygame.display.set_mode((400, 300))
pygame.display.set_caption('Inntastingsfelt i Pygame')

# Farger
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Tekstvariabler
font = pygame.font.Font(None, 32)
input_box = pygame.Rect(100, 100, 200, 32)
color_inactive = pygame.Color('lightskyblue3')
color_active = pygame.Color('dodgerblue2')
color = color_inactive
active = False
text = ''

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            if input_box.collidepoint(event.pos):
                active = not active
            else:
                active = False
            color = color_active if active else color_inactive
        
        if event.type == pygame.KEYDOWN:
            if active:
                if event.key == pygame.K_RETURN:
                    print(f'Du skrev: {text}')
                    text = ''  # Tømmer inntastingfeltet etter enter
                elif event.key == pygame.K_BACKSPACE:
                    text = text[:-1]
                else:
                    text += event.unicode

    # Tegn alt
    screen.fill(WHITE)
    txt_surface = font.render(text, True, color)
    width = max(200, txt_surface.get_width()+10)
    input_box.w = width
    screen.blit(txt_surface, (input_box.x+5, input_box.y+5))
    pygame.draw.rect(screen, color, input_box, 2)

    pygame.display.flip()