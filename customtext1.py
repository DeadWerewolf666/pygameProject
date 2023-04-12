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
black = (0, 0, 0)

# barva obrazovky
sc.fill(gray)

# Systemové fonty
# fonty = pygame.font.get_fonts()
# print(fonty)
# linuxbiolinumg
system_font1 = pygame.font.SysFont("Helvetica", 64)
system_font2 = pygame.font.SysFont("linuxbiolinumg", 25)
custom_font = pygame.font.Font("Fonts/AlteSchwabacher-lgw0.ttf", 60)

# Font a text
system_text1 = system_font1.render("Hovnovec", True, blue)
system_text1_rect = system_text1.get_rect()
system_text1_rect.midtop = (width//2, 0)

system_text2 = system_font2.render("Albus Dumbledore", True, green)
system_text2_rect = system_text2.get_rect()
system_text2_rect. center = (width//2, height//2)

custom_text = custom_font.render("Deutchland", True, black)
custom_text_rect = custom_text.get_rect()
custom_text_rect.midbottom = (width//2, height)

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
    sc.blit(system_text1, system_text1_rect)
    sc.blit(system_text2, system_text2_rect)
    sc.blit(custom_text, custom_text_rect)

    # Update obrazovky
    pygame.display.update()

# Ukončení
pygame.quit()
