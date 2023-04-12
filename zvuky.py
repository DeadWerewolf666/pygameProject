import pygame

# Inicializace
pygame.init()

# Obraz
width = 800
height = 600
res = (width, height)
sc = pygame.display.set_mode(res)

# Barvy
gray = (100, 100, 100)
black = (0, 0, 0)
white = (255, 255, 255)

# Obarvení obrazovky
sc.fill(gray)

# Font a text
custom_font = pygame.font.Font("Fonts/AlteSchwabacher-lgw0.ttf", 60)

custom_text = custom_font.render("Deutchland", True, black)
custom_text_rect = custom_text.get_rect()
custom_text_rect.midtop = (width//2, 0)

# Obrázek
char1_front_img = pygame.image.load("img/Character1/Character1_front_side.png")
char1_front_rect = char1_front_img.get_rect()
char1_front_rect.center = (width//2, height//2)

# Čára
line1 = pygame.draw.line(sc, black, (0, 70), (width, 70), 5)

# Hudba v pozadí
pygame.mixer.music.load("sounds/Serbia Strong- 8 bit.mp3")
pygame.mixer.music.play()

# Zvuky
serbia = pygame.mixer.Sound("sounds/Serbia Strong- 8 bit.mp3")
gun = pygame.mixer.Sound("sounds/bbc_antique-fi_07019171.mp3")

# Přehrání zvuku
gun.play()
# pygame.time.delay(1000)
# serbia.play()

# Hlavní cyklus
lets_continue = True
while lets_continue:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            lets_continue = False

    # Zobrazení obrazu
    sc.blit(custom_text, custom_text_rect)
    sc.blit(char1_front_img, char1_front_rect)

    # Update obrazu
    pygame.display.update()

# Ukončení
pygame.quit()
