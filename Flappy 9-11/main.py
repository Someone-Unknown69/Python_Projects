import pygame
import random
import math
from pygame import KEYDOWN, MOUSEBUTTONDOWN
from pygame import mixer

pygame.init()

clock = pygame.time.Clock()

screen = pygame.display.set_mode((1000,600))   #Makes the screen width*height
running_bool = True

pygame.display.set_caption("Flappy Osama")
logo = pygame.image.load("logo.png")
pygame.display.set_icon(logo)
background = pygame.image.load("background.png").convert()
bg_width = background.get_width()
x1 = 0
x2 = bg_width



# The Plane
plane_img = pygame.image.load("plane.png")
scaled_image = pygame.transform.scale(plane_img, (100,100))
planeX = 100
planeY = 250
plane_change = 0

# The Buildings

# Generating Buildings at random position

building1 = pygame.image.load("building1.png")
building2 = pygame.image.load("building2.png")

building_scaled_image = [pygame.transform.scale(building1, (350, 450)),
                         pygame.transform.flip(pygame.transform.scale(building2, (350, 450)), False, True),
                         pygame.transform.scale(building1, (350, 450)),
                         pygame.transform.flip(pygame.transform.scale(building2, (350, 450)), False, True)]

building_velocity = 4
building_acceleration = 0.0005
buildingX = []
buildingY = []
building_startX = [False,False,False,False]

for i in range(4):
    buildingX.append(900)
    buildingY.append(random.randint(150,450))


# Score
score_value = 0
font = pygame.font.Font('New September.otf', 50)
over_font = pygame.font.Font('New September.otf', 80)
textX = 10
textY = 10

def game_over_text():
    over_text = over_font.render("GAME OVER", True, (255,255,255))
    screen.blit(over_text, (300,250))

def show_score(x,y):
    score = font.render("Score : " + str(score_value), True, (255,255,255))
    screen.blit(score, (x,y))

def collision(x1,y1,x2,y2):
    distance = math.sqrt(math.pow(x2 - x1 , 2) + math.pow(y2 - y1 , 2))
    if distance < 100:
        return True
    else :
        return False


# The Game loop
while running_bool:
    screen.fill((0,0,0))
    screen.blit(background,(-100, -100))
    # show_score(textX, textY)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running_bool = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                # mixer.Sound.play(mixer.Sound('booster.wav'))
                plane_change -= 5
            elif event.key == pygame.K_UP:
                plane_change -= 5
            elif event.key == pygame.K_DOWN:
                plane_change  += 5
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN or event.key == pygame.K_UP or event.key == pygame.K_SPACE:
                plane_change = 0

    # Scrolling background display
    # Moving the background
    x1 -= 1 # Scroll speed
    x2 -= 1

    if x1 <= -bg_width:
        x1 = bg_width
    if x2 <= -bg_width:
        x2 = bg_width

    # Draw the background
    screen.blit(background,(x1,-10))
    screen.blit(background,(x2,-10))



    # Plane Display and movement
    screen.blit(scaled_image,(planeX,planeY))
    planeY += 1           # Gravity effect on plane
    planeY += plane_change

    # Building Display
    for j in range(4):
        screen.blit(building_scaled_image[j],(buildingX[j],buildingY[j]))

    # Building movement
    building_startX[0] = True
    if buildingX[0] < 550:
        building_startX[1] = True
    if buildingX[1] < 650:
        building_startX[2] = True
    if buildingX[2] < 550:
        building_startX[3] = True

    building_velocity += building_acceleration
    for i in range (0,4):
        if building_startX[i]:
            buildingX[i] -= building_velocity

        if buildingX[i] < -350:
            if i % 2 == 0:
                buildingY[i] = random.randint(150,450)
            else :
                buildingY[i] = random.randint(-300,0)
            buildingX[i] = 900

        # if collision(buildingX[i],buildingY[i],planeX,planeY):
        #     game_over_text()
        #     break


    pygame.display.update()
    clock.tick(60)
