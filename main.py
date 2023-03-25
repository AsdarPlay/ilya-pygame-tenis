import pygame
import random
pygame.init() #Инициализируем pygame, который импортировали стройкой выше

#Загружаем различную музыку:
    #Фоновая музыка
backgroungS = pygame.mixer.Sound('Sounds/Background.ogg')
backgroungS.set_volume(0.1)

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
width = 1266
height = 800
fps = 60
#Задаём имя проекту и создаём экран для игры
gameName = 'First project'
screen = pygame.display.set_mode((width, height))
#добавляем цвета
black = '#000000'
white = '#FFFFFF'
red = '#FF0000'
green = '#008000'
blue = '#0000FF'
cyan = '#00FFFF'
#Добавляем три жизни
hp = 3
heart = pygame.image.load('heart.png')
heart = pygame.transform.scale(heart, (50, 50))
heart_rect = heart.get_rect()

heart2 = pygame.image.load('heart.png')
heart2 = pygame.transform.scale(heart, (50, 50))
heart2_rect = heart2.get_rect()

heart3 = pygame.image.load('heart.png')
heart3 = pygame.transform.scale(heart, (50, 50))
heart3_rect = heart3.get_rect()

#Фон для паузы
pause_background = pygame.image.load('pause.png')
pause_background = pygame.transform.scale(pause_background, (width, height))
pause_background.set_alpha(80)
pause_background_rect = pause_background.get_rect()
#Добавляем мячик
img = pygame.image.load('ball.png')
img = pygame.transform.scale(img, (70, 70))
img_rect = img.get_rect()
img_rect.x = random.randint(width - (width - 100), width - 150)

img2 = pygame.image.load('ball.png')
img2 = pygame.transform.scale(img2, (70, 70))
img2_rect = img2.get_rect()

#Фон
background = pygame.image.load('background.png')
background = pygame.transform.scale(background, (width, height))
background_rect = background.get_rect()
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
speedX2 = 10
speedY2 = 10
PlatformSpeed = 11

clock = pygame.time.Clock()

def pause():
    global img_rect, img2_rect
    pause = True
    while pause:
        key = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if key[pygame.K_ESCAPE]:
                pause = False
        img_rect.x = img_rect.x
        img2_rect.x = img2_rect.x
        img_rect.y = img_rect.y
        img2_rect.y = img2_rect.y
    pygame.display.update()

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
        key = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if key[pygame.K_RETURN]:
                start = False
            if key[pygame.K_SPACE]:
                start = False
        startS.set_volume(0.05)
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

def game():
    global hp, speedX, speedY, speedX2, speedY2, score, maxScore, PlatformSpeed
    run = True
    backgroungS.play()
    fallS.set_volume(0.3)
    while run:
        clock.tick(fps)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        key = pygame.key.get_pressed()

        if key[pygame.K_TAB]:
            pause()

            # Отрисовываем все спрайты, которые добавили ранее
        Score = f1.render('Score: ' + str(score), 50, (white))
        MaxScore = f1.render('Max score: ' + str(maxScore), 50, (white))
        screen.blit(background, background_rect)
        screen.blit(img, img_rect)
        screen.blit(platform, platform_rect)

        screen.blit(Score, (10, 10))
        screen.blit(MaxScore, (10, 60))

        img_rect.x += speedX
        img_rect.y += speedY

        # Физика платформы и её звуки
        if key[pygame.K_LEFT] and platform_rect.left > 0:
            platform_rect.x -= PlatformSpeed
        if key[pygame.K_RIGHT] and platform_rect.right < width:
            platform_rect.x += PlatformSpeed
        if img_rect.bottom > platform_rect.top:
            if img_rect.left < platform_rect.right and img_rect.right > platform_rect.left:
                speedY = -speedY
                platformS.play()
                score += 1
        if img2_rect.bottom > platform_rect.top:
            if img2_rect.left < platform_rect.right and img2_rect.right > platform_rect.left:
                speedY2 = -speedY2
                platformS.play()
                score += 1
        if score == 10:
            PlatformSpeed = 14.5
        if score >= 10:

            screen.blit(img2, img2_rect)

            img2_rect.x += speedX2
            img2_rect.y += speedY2

            if img2_rect.top < 0:
                speedY2 = -speedY2
                wallS.play()
            if img2_rect.left < 0:
                speedX2 = -speedX2
                wallS.play()
            if img2_rect.right > width:
                speedX2 = -speedX2
                wallS.play()
            if img2_rect.bottom > height:
                if hp > 0:
                    hp -= 1
                    fallS.play()
                    img2_rect.x = random.randint(width - (width - 100), width - 100)
                    img2_rect.y = 0
                elif hp == 0:
                    fallS.set_volume(0)
                    backgroungS.stop()
                    img2_rect.x = random.randint(width - (width - 100), width - 100)
                    img2_rect.y = 0
                    run = False
                    pygame.display.update()

        # Физика мяча и его звуки
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
                hp -= 1
                fallS.play()
                img_rect.x = random.randint(width - (width - 100), width - 100)
                img_rect.y = 0
            elif hp == 0:
                fallS.set_volume(0)
                backgroungS.stop()
                img_rect.x = random.randint(width - (width - 100), width - 100)
                img_rect.y = 0
                run = False
                pygame.display.update()

        if hp == 3:
            screen.blit(heart, heart_rect)
            heart_rect.x = width - 150
            screen.blit(heart2, heart2_rect)
            heart2_rect.x = width - 100
            screen.blit(heart3, heart3_rect)
            heart3_rect.x = width - 50
        if hp == 2:
            screen.blit(heart2, heart2_rect)
            heart2_rect.x = width - 100
            screen.blit(heart3, heart3_rect)
            heart3_rect.x = width - 50
        if hp == 1:
            screen.blit(heart3, heart3_rect)
            heart3_rect.x = width - 50
        if score > maxScore:
            maxScore += 1

        pygame.display.update()

def draw_game_over():
    global score, maxScore, hp
    f1 = pygame.font.Font(None, 100)
    f2 = pygame.font.Font(None, 80)
    text_game_over = f1.render('Game over!', True, white)
    text_game_over2 = f1.render('Your score: ' + str(score), True, white)
    text_game_over3 = f1.render('Your max score: ' + str(maxScore), True, white)
    text_game_over4 = f2.render('To quit game press ESCAPE', True, white)
    text_game_over5 = f2.render('To restart game press ENTER', True, white)
    game_overS.play()
    end = False
    while not end:
        key = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if key[pygame.K_ESCAPE]:
                pygame.quit()
            if key[pygame.K_RETURN]:
                end = True
                score = 0
                hp = 3

        screen.fill(black)
        screen.blit(text_game_over, ((width / 2) - 200, 150))
        screen.blit(text_game_over2, ((width / 2) - 230, 220))
        screen.blit(text_game_over3, ((width / 2) - 285, 290))
        screen.blit(text_game_over4, ((width / 2) - 380, 400))
        screen.blit(text_game_over5, ((width / 2) - 380, 470))
        pygame.display.update()

#Вызов функций игры
draw_begin()
startS.stop()
while True:
    game()
    backgroungS.stop()
    draw_game_over()

pygame.quit()