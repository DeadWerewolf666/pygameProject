import pygame

# Inicializace hry
pygame.init()

# Obrazovka
width = 600
height = 300
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Harry Potter Game")

# Definujeme barvy
gray = (100, 100, 100)
red = (255, 0, 0)
black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 255)

# Barva pozadí
screen.fill(gray)

# Tvary
pygame.draw.line(screen, red, (0, 0), (width//2, height//2), 5)
pygame.draw.circle(screen, green, (width//2, height//2), 100)
pygame.draw.rect(screen, blue, (width//2 - 50, height//2 - 50, 100, 100))

# Hlavní cyklus
lets_continue = True

while lets_continue:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            lets_continue = False

    # Updatujeme obrazovku
    pygame.display.update()

# Ukončení hry
pygame.quit()
