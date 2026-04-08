"""
Lager tre check boxes og tilhørende tekst som kan klikkes på
- kan bare klikke på teksten, ikke firkantene - det bør endres
- firkanter og tekst står skjevt på - det bør endres
Lagd av Osloskolen-GPT, ki.osloskolen.no 
"""

import pygame
import sys

# Initialiser Pygame
pygame.init()

# Definer farger
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
LIGHT_GRAY = (230, 230, 230)

# Definer skjermstørrelse
screen_size = (400, 300)
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("Check Box Example")

# Definer alternativer
options = ["Alternativ 1", "Alternativ 2", "Alternativ 3"]
checked = [False] * len(options)
klikk = False
# Hovedløkke
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            for i in range(len(options)):
                if 50 <= mouse_x <= 350 and 50 + i * 50 <= mouse_y <= 75 + i * 50:
                    checked[i] = not checked[i]  # Slå av/på avmerkingsboksen
                    klikk = True

    # Tegn skjermen
    screen.fill(WHITE)
    
    for i, option in enumerate(options):
        # Tegn avmerkingsboksen
        pygame.draw.rect(screen, LIGHT_GRAY if not checked[i] else BLACK, (30, 62 + i * 50, 20, 20), 2)
        if checked[i]:
            pygame.draw.line(screen, BLACK, (30, 62 + i * 50), (50, 82 + i * 50), 2)
            pygame.draw.line(screen, BLACK, (30, 82 + i * 50), (50, 62 + i * 50), 2)

            

        # Tegn teksten for alternativet
        font = pygame.font.Font(None, 36)
        text_surface = font.render(option, True, BLACK)
        screen.blit(text_surface, (60, 50 + i * 50))

    print(checked)

    # Oppdater skjermen
    pygame.display.flip()