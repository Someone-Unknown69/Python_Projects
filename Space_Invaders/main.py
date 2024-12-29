import pygame
import random
import math
from pygame import KEYDOWN
from pygame import mixer
pygame.init()

screen = pygame.display.set_mode((1000,600))   #Makes the screen width*height
running_bool = True

# Title and caption
pygame.display.set_caption("Space Invaders")

# Changing the icons
icon = pygame.image.load("logo.png")
pygame.display.set_icon(icon)

background = pygame.image.load('background.png')

#Addition of the player image
PlayerImg = pygame.image.load("spaceship.png")
PlayerX = 450
PlayerY = 480
Player_change = 0

#Adding bullets
BulletImg = pygame.image.load('bullet.png')
BulletY = PlayerY
BulletX = PlayerX
Bullet_cond = False
bullet_count = 0

#Addition of an enemy in the game
Enemy_count = 6
EnemyImg = []
EnemyX = []
EnemyY = []
Enemy_change = []
Enemy_movement = []

for i in range(Enemy_count):
    EnemyImg.append(pygame.image.load('enemy.png'))
    EnemyX.append(random.randint(0, 900))
    EnemyY.append(random.randint(0,100))
    Enemy_movement.append(True)
    Enemy_change.append(3)

# Score
score_value = 0
font = pygame.font.Font('New September.otf', 50)
over_font = pygame.font.Font('New September.otf', 80)
textX = 10
textY = 10

def show_score(x,y):
    score = font.render("Score : " + str(score_value), True, (255,255,255))
    screen.blit(score, (x,y))

def game_over_text():
    over_text = over_font.render("GAME OVER", True, (255,255,255))
    screen.blit(over_text, (300,250))

def player(Image,x,y):                         # function for displaying executing blit code
    screen.blit(Image, (x,y))   #blit displays the image on the screen

def fire_bullet(x,y):
    global Bullet_cond
    Bullet_cond = True
    screen.blit(BulletImg,(x + 16,y + 10))

# Function to check collision between bullet and the enemy
def collision(x1,y1,x2,y2):
    distance = math.sqrt(math.pow(x2 - x1 , 2) + math.pow(y2 - y1 , 2))
    if distance < 27:
        return True
    else :
        return False


# Background Music
mixer.music.load('BGM.wav')
mixer.music.play(-1)


      # GAME LOOP #
#Displayin the whole screen
''' Whatever you wanna do , do it within this while window in case of any change in the game screen'''
while running_bool:


    #changing colours in screen            (This shit shall be above everything)
    screen.fill((255,255,255))              # RGB format
    screen.blit(background,(0,0))
    show_score(textX,textY)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running_bool = False


        '''Now let's see how we can manipulate the movement of the object'''
        '''we will use repetitive addition of coordinates in order to change the position of the player
        We will track the keystrokes pressed on the keyboard '''

        if event.type == pygame.KEYDOWN:
            # print("A keystroke is pressed")
            if event.key == pygame.K_LEFT:
                Player_change = -5
            if event.key == pygame.K_RIGHT:
                Player_change = 5
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                Player_change = 0

        if event.type == KEYDOWN and not Bullet_cond:          # For firing of the bullets when space bar is hit
            if event.key == pygame.K_SPACE:
                fire_bullet(PlayerX,BulletY)
                mixer.Sound.play(mixer.Sound('laser.wav'))
                BulletX = PlayerX
                bullet_count += 1


    PlayerX+=Player_change

    # Now adding the legendary map boundaries to our game


    if PlayerX <= 0:           # LHS boundary
        PlayerX = 0

    elif PlayerX >= 936:       # RHS boundary
        PlayerX = 936

    for i in range(Enemy_count):

        # Game Over
        if EnemyY[i] > 400:
            for j in range(Enemy_count):
                EnemyY[j] = 2000
            game_over_text()
            break

        EnemyX[i] += Enemy_change[i]

        # Check enemy boundaries and reverse direction if needed
        if EnemyX[i] <= 0:
            Enemy_change[i] = 3  # Move right
            EnemyY[i] += 40
        elif EnemyX[i] >= 936:
            Enemy_change[i] = -3  # Move left
            EnemyY[i] += 40

        # Check for collision between bullet and enemy
        if collision(EnemyX[i], EnemyY[i], BulletX, BulletY):
            mixer.Sound.play(mixer.Sound('explosion.wav'))
            BulletY = PlayerY  # Reset bullet position
            Bullet_cond = False
            EnemyX[i] = random.randint(0, 900)  # Respawn enemy
            EnemyY[i] = random.randint(0, 100)  # Respawn enemy
            score_value += 1  # Increment score
            # print(f"Score: {score_value}")

        player(EnemyImg[i], EnemyX[i], EnemyY[i])  # The function is called to display the enemy

    if Bullet_cond:
        player(BulletImg,BulletX,BulletY)

    #Bullet movement code
    if Bullet_cond :
        BulletY -= 7

    #condition for respawning the bullet if it hits the top of the map
    if BulletY < 0:
        BulletY = PlayerY
        Bullet_cond = False

    # Calling the player method inside the while loop
    player(PlayerImg,PlayerX,PlayerY)                 #The function is called to display the object

    pygame.display.update()





