import pygame
import random
import math

#Run pygame
pygame.init()


#Screen

screen = pygame.display.set_mode((1100, 733))

#Background
background = pygame.image.load('background.png')


#Caption and Icon (which isn't working)
pygame.display.set_caption("Run!")
icon = pygame.image.load('run_icon.png')
pygame.display.set_icon(icon)

#Player

playerImg = pygame.image.load('player.png')
playerX = 550
playerY = 366.5
playerX_change = 0
playerY_change = 0

#Family

familyImg = pygame.image.load('family.png')
familyX = random.randint(0, 1024)
familyY = random.randint(0, 657)
familyX_change = 1.6
familyY_change = 1.6

#Habits

bulletImg = pygame.image.load('weed.png')
bulletX = 0
bulletY = 550
bulletX_change = 0
bulletY_change = 2.2
bullet_state = "Ready"

score = 0

def player(X, Y):
  screen.blit(playerImg, (playerX, playerY))

def family(X, Y):
  screen.blit(familyImg, (familyX, familyY))

def fire_bullet(x, y):
  global bullet_state
  bullet_state = "Fire"
  screen.blit(bulletImg, (x, y - 10))

def isCollision(familyX, familyY, bulletX, bulletY):
  distance = math.sqrt((math.pow(familyX - bulletX, 2)) + (math.pow(familyY - bulletY, 2)))
  if distance < 50:
    return True
  else:
    return False  

running = True
while running:

  #RGB (Red, Green, Blue)
  screen.fill((255, 255, 255))
  screen.blit(background, (0, 0))
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False

    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_LEFT:
        playerX_change = -1.6
      if event.key == pygame.K_RIGHT:
        playerX_change = 1.6
      if event.key == pygame.K_UP:
        # print("Up was clicked")
        playerY_change = -1.6
        #Used the == instead of =
      if event.key == pygame.K_DOWN:
        # print("down was clicked")
        playerY_change = 1.6
      if event.key == pygame.K_SPACE:
        if bullet_state == "Ready":
          bulletX = playerX
          bulletY = playerY
          fire_bullet(bulletX, bulletY)

    if event.type == pygame.KEYUP:
      if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
        playerX_change = 0
      if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
        playerY_change = 0

  # Can draw creatures
  # pygame.draw.circle(screen, (0, 0, 255), (250, 250), 75)

  #Player Movement
  playerX += playerX_change
  if playerX <= 0:
    playerX = 0
  elif playerX >= 1024:
    playerX = 1024

  playerY += playerY_change
  if playerY <= 0:
    playerY = 0
  elif playerY >= 657:
    playerY = 657

  #Family Movement
  familyX += familyX_change

  if familyX <= 0:
    familyX_change = 1.6
  elif familyX >= 1024:
    familyX_change = -1.6

  familyY += familyY_change

  if familyY <= 0:
    familyY_change = 1.6
  elif familyY >= 657:
    familyY_change = -1.6

  #Bullet Movement
  if bulletY <= 0:
    bulletY = 550
    bullet_state = "Ready"
  if bullet_state == "Fire":
    fire_bullet(bulletX, bulletY)
    bulletY -= bulletY_change

  #Collision
  collision = isCollision(familyX, familyY, bulletX, bulletY)
  if collision:
    bulletY = 550
    bullet_state = "Ready"
    score += 1
    print(score)
    familyX = random.randint(0, 1024)
    familyY = random.randint(0, 657)


  player(playerX, playerY)
  family(familyX, familyY)
  pygame.display.update()
  # pygame.quit()