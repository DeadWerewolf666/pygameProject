import pygame
import time

# inicializace
pygame.init()

# Okno
width = 800
height = 600
res = (width, height)
sc = pygame.display.set_mode(res)

# Barvy
gray = (100, 100, 100)
black = (0, 0, 0)
white = (255, 255, 255)

# Barva obrazu
sc.fill(gray)

# Text
text1_font = pygame.font.Font("Fonts/AlteSchwabacher-lgw0.ttf", 50)
text1 = text1_font.render("Deutchland", True, black)
text1_rect = text1.get_rect()
text1_rect.midtop = (width // 2, 0)

# Obrázek
distance = 7
fps = 60
clock = pygame.time.Clock()

all_side = [
    pygame.image.load("img/Character1/Character1_front_side.png"),
    pygame.image.load("img/Character1/Character1_back_side.png"),
    pygame.image.load("img/Character1/Character1_left_side.png"),
    pygame.image.load("img/Character1/Character1_right_side.png"),

]
front_side = [
    pygame.image.load("img/Character1/Character1_front_side.png"),
    pygame.image.load("img/Character1/front_side/Character1_front_side_walk1.png"),
    pygame.image.load("img/Character1/front_side/Character1_front_side_walk2.png"),
    pygame.image.load("img/Character1/front_side/Character1_front_side_walk3.png"),
    pygame.image.load("img/Character1/front_side/Character1_front_side_walk4.png"),
    pygame.image.load("img/Character1/front_side/Character1_front_side_walk5.png"),
    pygame.image.load("img/Character1/front_side/Character1_front_side_walk6.png")

]
back_side = [
    pygame.image.load("img/Character1/Character1_back_side.png"),
    pygame.image.load("img/Character1/back_side/Character1_back_side_walk1.png"),
    pygame.image.load("img/Character1/back_side/Character1_back_side_walk2.png"),
    pygame.image.load("img/Character1/back_side/Character1_back_side_walk3.png"),
    pygame.image.load("img/Character1/back_side/Character1_back_side_walk4.png"),
    pygame.image.load("img/Character1/back_side/Character1_back_side_walk5.png"),
    pygame.image.load("img/Character1/back_side/Character1_back_side_walk6.png"),
]
left_side = [
    pygame.image.load("img/Character1/Character1_left_side.png"),
    pygame.image.load("img/Character1/left_side/Character1_left_side_walk1.png"),
    pygame.image.load("img/Character1/left_side/Character1_left_side_walk2.png"),
    pygame.image.load("img/Character1/left_side/Character1_left_side_walk3.png"),
    pygame.image.load("img/Character1/left_side/Character1_left_side_walk4.png"),
    pygame.image.load("img/Character1/left_side/Character1_left_side_walk5.png"),
    pygame.image.load("img/Character1/left_side/Character1_left_side_walk6.png"),
]
right_side = [
    pygame.image.load("img/Character1/Character1_right_side.png"),
    pygame.image.load("img/Character1/right_side/Character1_right_side_walk1.png"),
    pygame.image.load("img/Character1/right_side/Character1_right_side_walk2.png"),
    pygame.image.load("img/Character1/right_side/Character1_right_side_walk3.png"),
    pygame.image.load("img/Character1/right_side/Character1_right_side_walk4.png"),
    pygame.image.load("img/Character1/right_side/Character1_right_side_walk5.png"),
    pygame.image.load("img/Character1/right_side/Character1_right_side_walk6.png"),

]

char1_actual_img = front_side[0]
char1_actual_rect = char1_actual_img.get_rect()
char1_actual_rect.center = (width // 2, height // 2)


def indexer(x):
    if x <= 5:
        x += 1
        return x
    else:
        return 0


# Hudba na pozadí
pygame.mixer.music.load("sounds/Serbia Strong- 8 bit.mp3")
pygame.mixer.music.play()
# Hlavní cyklus
actual_side = char1_actual_img
lets_continue = True
stop_side = 0
left_index = 0
right_index = 0
front_index = 0
back_index = 0
while lets_continue:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            lets_continue = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        stop_side = 1
        back_index = indexer(back_index)
        char1_actual_img = back_side[back_index]
        pygame.time.delay(50)
        if char1_actual_rect.y - distance > 0:
            char1_actual_rect.y -= distance

    elif keys[pygame.K_s]:
        stop_side = 0
        front_index = indexer(front_index)
        char1_actual_img = front_side[front_index]
        pygame.time.delay(50)
        if char1_actual_rect.y + distance + 50 < height:
            char1_actual_rect.y += distance

    elif keys[pygame.K_a]:
        stop_side = 2
        left_index = indexer(left_index)
        char1_actual_img = left_side[left_index]
        pygame.time.delay(50)
        if char1_actual_rect.x - distance > 0:
            char1_actual_rect.x -= distance

    elif keys[pygame.K_d]:
        stop_side = 3
        right_index = indexer(right_index)
        char1_actual_img = right_side[right_index]
        pygame.time.delay(50)
        if char1_actual_rect.x + distance + 30 < width:
            char1_actual_rect.x += distance
    else:
        char1_actual_img = all_side[stop_side]

    # Vyplnění obrazovky
    sc.fill(gray)

    # Zobrazení
    sc.blit(text1, text1_rect)
    sc.blit(char1_actual_img, char1_actual_rect)

    # Update obrazu
    pygame.display.update()

    # tikání hodin
    clock.tick(fps)

# ukončení
pygame.quit()
