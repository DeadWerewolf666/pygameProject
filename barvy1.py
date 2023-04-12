# importujeme pygame
import pygame

# Inicializace pygame
pygame.init()

# Obrazovka
width = 800
height = 600
res = (width, height)

screen = pygame.display
sc = pygame.display.set_mode(res)
screen.set_caption("Hra Harry Potter")

# Barvy
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
gray = (100, 100, 100)

# barva pozadí
sc.fill(gray)

# Hlavní herní cyklus
lets_continue = True
while lets_continue:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            lets_continue = False

    screen.update()
# Ukončení pygame
pygame.quit()
