# importujeme pygame
import pygame

# Inicializace pygame
pygame.init()

# Vytvoření obrazovky
width = 800
height = 600
res = (width, height)
screen = pygame.display.set_mode(res)

# Hlavní herní cyklus
lets_continue = True
while lets_continue:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            lets_continue = False

# Ukončení pygame
pygame.quit()
