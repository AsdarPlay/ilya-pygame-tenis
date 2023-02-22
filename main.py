import pygame
import random

pygame.init()

pygame.mixer.music.load('Sounds/Background.mp3')
pygame.mixer.music.set_volume(0.03)
pygame.mixer.music.play(-1)

platformS = pygame.mixer.Sound('Sounds/platform.ogg')
platformS.set_volume(0.3)

fallS = pygame.mixer.Sound('Sounds/fall.ogg')
fallS.set_volume(0.3)

wallS = pygame.mixer.Sound('Sounds/walls.ogg')
wallS.set_volume(0.3)

width = 1366
height = 900
fps = 60
gameName = 'First project'
screen = pygame.display.set_mode((width, height))

black = '#000000'
white = '#FFFFFF'
red = '#FF0000'
green = '#008000'
blue = '#0000FF'
cyan = '#00FFFF'

hp = 3
heart1 = pygame.image.load('heart.png')
heart1 = pygame.transform.scale(heart1, (50, 50))
heart1_rect = heart1.get_rect()
heart1_rect.x = width - 50

heart2 = pygame.image.load('heart.png')
heart2 = pygame.transform.scale(heart2, (50, 50))
heart2_rect = heart2.get_rect()
heart2_rect.x = width - 100

heart3 = pygame.image.load('heart.png')
heart3 = pygame.transform.scale(heart3, (50, 50))
heart3_rect = heart3.get_rect()
heart3_rect.x = width - 150

img = pygame.image.load('ball.png')
img = pygame.transform.scale(img, (80, 80))
img_rect = img.get_rect()
img_rect.x = random.randint(5, 1400)

art = pygame.image.load('background.png')
art = pygame.transform.scale(art, (width, height))
art_rect = art.get_rect()

platform = pygame.image.load('platform.png')
platform = pygame.transform.scale(platform, (200, 125))
platform_rect = platform.get_rect()
platform_rect.x = 500
platform_rect.y = 800

speedX = 10
speedY = 10
clock = pygame.time.Clock()
run = True
while run:
    clock.tick(fps)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    key = pygame.key.get_pressed()

    screen.blit(art, art_rect)
    screen.blit(img, img_rect)
    screen.blit(platform, platform_rect)
    screen.blit(heart1, heart1_rect)
    screen.blit(heart2, heart2_rect)
    screen.blit(heart3, heart3_rect)

    img_rect.x += speedX
    img_rect.y += speedY

    if key[pygame.K_LEFT] and platform_rect.left > 0:
        platform_rect.x -= 12
    if key[pygame.K_RIGHT] and platform_rect.right < width:
        platform_rect.x += 12
    if img_rect.bottom > platform_rect.top:
        if img_rect.left < platform_rect.right and img_rect.right > platform_rect.left:
            speedY = -speedY
            platformS.play()

    if img_rect.top < 0:
        speedY = -speedY
        wallS.play()
    if img_rect.left < 0:
        speedX = -speedX
        wallS.play()
    if img_rect.right > width:
        speedX = -speedX
        wallS.play()

    if img_rect.bottom > height:
        if hp > 0:
            fallS.play()
        hp -= 1
        if hp == 2:
            heart3_rect.y = -50
        if hp == 1:
            heart2_rect.y = -50
        if hp > 0:
            img_rect.x = random.randint(5, 1400)
            img_rect.y = 5
        elif hp == 0:
            heart1_rect.y = -50
            fallS.set_volume(0)

    pygame.display.update()

pygame.quit()