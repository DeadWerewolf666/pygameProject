import pygame

# inicializace
pygame.init()

# Obrazovka
width = 800
height = 600
res = (width, height)
sc = pygame.display.set_mode(res)

# Barvy
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
gray = (100, 100, 100)

# Barva obrazovky
sc.fill(gray)

# Tvary
# pygame.draw.rect(sc, green, (width//2-50, height//2-50, 100, 100))

# Obrázky
char1_front_image = pygame.image.load("img/Character1/Character1_front_side.png")
char1_front_rect = char1_front_image.get_rect()
char1_front_rect.center = (width//2, height//2)

# Hlavní cikus
lets_continue = True
while lets_continue:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            lets_continue = False

    # Přidání obrázku
    sc.blit(char1_front_image, char1_front_rect)

    # Update obrazovky
    pygame.display.update()

# Ukončení
pygame.quit()
