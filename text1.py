import pygame

# Inicializace
pygame.init()

# Obrazovka
width = 800
height = 600
res = (width, height)
sc = pygame.display.set_mode(res)

# barvy
gray = (100, 100, 100)
blue = (0, 0, 255)
green = (0, 255, 0)

# barva obrazovky
sc.fill(gray)

# Systemové fonty
system_font = pygame.font.SysFont("Helvetica", 64)

# Font a text
system_text = system_font.render("Hovnovec", True, blue)
system_text_rect = system_text.get_rect()
system_text_rect.midtop = (width//2, 0)

# Obrázek
# char1_front_img = pygame.image.load("img/Character1/Character1_front_side.png")
# char1_front_rect = char1_front_img.get_rect()
# char1_front_rect.center = (width//2, height//2)

# Hlavní cyklus
lets_continue = True
while lets_continue:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            lets_continue = False

    # Zobrazení obrázku
    # sc.blit(char1_front_img, char1_front_rect)
    sc.blit(system_text, system_text_rect)

    # Update obrazovky
    pygame.display.update()

# Ukončení
pygame.quit()
