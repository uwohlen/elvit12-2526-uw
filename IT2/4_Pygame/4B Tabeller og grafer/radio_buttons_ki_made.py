"""
Lager tre radiobuttons og tilhørende tekst som kan klikkes på
- kan bare klikke på teksten, ikke sirklene - det bør endres
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

# Definer skjermstørrelse
screen_size = (400, 300)
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("Radio Buttons Example")

# Definer radio-knappene
options = ["Alternativ 1", "Alternativ 2", "Alternativ 3"]
selected_option = -1
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
                    selected_option = i
                    klikk = True

    # Tegn skjermen
    screen.fill(WHITE)
    
    for i, option in enumerate(options):
        if i == selected_option:
            color = BLACK
            if klikk:
              print(options[i])
            klikk = False
        else:
            color = GRAY
            
        # Tegn radio-knappen
        pygame.draw.circle(screen, color, (30, 62 + i * 50), 10)
        # Tegn teksten for alternativet
        font = pygame.font.Font(None, 36)
        text_surface = font.render(option, True, BLACK)
        screen.blit(text_surface, (50, 50 + i * 50))

    # Oppdater skjermen
    pygame.display.flip()