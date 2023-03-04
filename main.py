import pygame
import random
pygame.init() #Инициализируем pygame, который импортировали стройкой выше

#Загружаем различную музыку:
    #Фоновая музыка
backgroungS = pygame.mixer.Sound('Sounds/Background.ogg')
backgroungS.set_volume(0.1)
backgroungS.play(-1)
    #Стартовая музыка
startS = pygame.mixer.Sound('Sounds/start.ogg')
startS.set_volume(0.1)
    #Проигрыш(звук)
game_overS = pygame.mixer.Sound('Sounds/game_over.ogg')
game_overS.set_volume(0.3)
    #Звук, при попадании мясика на платформу
platformS = pygame.mixer.Sound('Sounds/platform.ogg')
platformS.set_volume(0.3)
    #Звук при выпадании мячика за экран
fallS = pygame.mixer.Sound('Sounds/fall.ogg')
fallS.set_volume(0.3)
    #Звук при отскоке мяча от стен
wallS = pygame.mixer.Sound('Sounds/walls.ogg')
wallS.set_volume(0.3)
#Параметры игры: ширина, высота, количество fps
width = 1366
height = 900
fps = 60
#Задаём имя проекту и создаём экран для игры
gameName = 'First project'
screen = pygame.display.set_mode((width, height))
#добавляем различные цвета
black = '#000000'
white = '#FFFFFF'
red = '#FF0000'
green = '#008000'
blue = '#0000FF'
cyan = '#00FFFF'
#Добавляем три жизни
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
#Добавляем мячик
img = pygame.image.load('ball.png')
img = pygame.transform.scale(img, (80, 80))
img_rect = img.get_rect()
img_rect.x = random.randint(width - (width - 100), width - 100)
#Фон
art = pygame.image.load('background.png')
art = pygame.transform.scale(art, (width, height))
art_rect = art.get_rect()
#Платформа
platform = pygame.image.load('platform.png')
platform = pygame.transform.scale(platform, (200, 125))
platform_rect = platform.get_rect()
platform_rect.x = width / 2 - 50
platform_rect.y = height - 100
#Количество очков в начале игры
score = 0
maxScore = 0
#Шрифт
f1 = pygame.font.Font(None, 46)

#Параметры скорости мяча
speedX = 12
speedY = 12

clock = pygame.time.Clock()

def draw_begin():
    SpeedX = 2
    SpeedY = 2
    f1 = pygame.font.Font(None, 100)
    text_game_begin = f1.render('Press SPACE or ENTER', True, white)
    text_game_begin2 = f1.render('to start game', True, white)
    ball = pygame.image.load('ball.png')
    ball = pygame.transform.scale(ball, (100, 100))
    ball_rect = ball.get_rect()
    ball_rect.x = 0
    start = True
    while start:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.key == pygame.K_RETURN:
                start = False
        startS.play()
        screen.fill(black)
        screen.blit(ball, ball_rect)
        screen.blit(text_game_begin, ((width / 2) - 330, 350))
        screen.blit(text_game_begin2, ((width / 2) - 230, 420))
        ball_rect.x += SpeedX
        ball_rect.y += SpeedY
        pygame.display.update()

        if ball_rect.top < 0:
            SpeedY = -SpeedY
        if ball_rect.left < 0:
            SpeedX = -SpeedX
        if ball_rect.right > width:
            SpeedX = -SpeedX
            wallS.play()
        if ball_rect.bottom > height:
            SpeedY = -SpeedY
        pygame.display.update()


def draw_game_over():
    global score, maxScore
    f1 = pygame.font.Font(None, 100)
    f2 = pygame.font.Font(None, 80)
    text_game_over = f1.render('Game over!', True, white)
    text_game_over2 = f1.render('Your score: ' + str(score), True, white)
    text_game_over3 = f1.render('Your max score: ' + str(maxScore), True, white)
    text_game_over4 = f2.render('To restart game press ENTER', True, white)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        screen.fill(black)
        screen.blit(text_game_over, ((width / 2) - 200, 80))
        screen.blit(text_game_over2, ((width / 2) - 230, 150))
        screen.blit(text_game_over3, ((width / 2) - 285, 220))
        screen.blit(text_game_over4, ((width / 2) - 380, 330))
        pygame.display.update()

#Основной игровой цикл
run = True
while run:
    clock.tick(fps)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    key = pygame.key.get_pressed()

    #Отрисовываем все спрайты, которые добавили ранее
    Score = f1.render('Score: ' + str(score), 50, (white))
    MaxScore = f1.render('Max score: ' + str(maxScore), 50, (white))
    screen.blit(art, art_rect)
    screen.blit(img, img_rect)
    screen.blit(platform, platform_rect)
    if hp >= 1:
        screen.blit(heart1, heart1_rect)
    if hp >= 2:
        screen.blit(heart2, heart2_rect)
    if hp >= 3:
        screen.blit(heart3, heart3_rect)
    screen.blit(Score, (10, 10))
    screen.blit(MaxScore, (10, 60))


    img_rect.x += speedX
    img_rect.y += speedY
    #Физика платформы и её звуки
    if key[pygame.K_LEFT] and platform_rect.left > 0:
        platform_rect.x -= 11
    if key[pygame.K_RIGHT] and platform_rect.right < width:
        platform_rect.x += 11
    if img_rect.bottom > platform_rect.top:
        if img_rect.left < platform_rect.right and img_rect.right > platform_rect.left:
            speedY = -speedY
            platformS.play()
            score += 1
    #Физика мяча и его звуки
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
            img_rect.x = random.randint(width - (width - 50), width - 50)
            img_rect.y = 5
        elif hp == 0:
            heart1_rect.y = -50
            fallS.set_volume(0)
            backgroungS.stop()
            game_overS.play()

            draw_game_over()

    if score > maxScore:
        maxScore += 1

    pygame.display.update()

pygame.quit()