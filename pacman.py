import pygame
import math
from board import boards

pygame.init()


# settings variables: screen, framerates, fonts etc...

# resolution, display
WIDTH = 900
HEIGHT = 950 
screen = pygame.display.set_mode([WIDTH, HEIGHT])

num1 = ((HEIGHT - 50) // 32 ) # column constant
num2 = (WIDTH // 30) # row constant
num3 = 15 # fat factor for the player
font = pygame.font.Font('freesansbold.ttf', 20) # font: default windows
level = boards # board array imported from board.py
color = 'blue' # color variable
PI = math.pi # pi 
flicker = False # blinker variable
turns_allowed = [False, False, False, False] # allowed way to turn
score = 0 # score 
powerup = False # state
power_counter = 0 # timer
eaten_ghost = [False, False, False, False] # ghost states
moving = False # moving state
startup_counter = 0 # counter
lives = 3
blinky_dead = False
inky_dead = False
pinky_dead = False
clyde_dead = False
blinky_box = False
inky_box = False
pinky_box = False
clyde_box = False
ghost_speed = 2
game_over = False
game_won = False

# starting pos, speed
player_x = 450
player_y = 663
player_speed = 2

# targets of ghosts
targets = [
    (player_x, player_y),
    (player_x, player_y),
    (player_x, player_y),
    (player_x, player_y)
]

# other player variables
direction = 0
counter = 0
direction_command = 0

# framerate
timer = pygame.time.Clock()
fps = 60

# animations
player_images = []

for i in range(1, 5): 
    player_images.append(pygame.transform.scale(pygame.image.load(f'./Pacman Python/assets/player_images/{i}.png'), (45, 45)))

# ghost assets
blinky_img = pygame.transform.scale(pygame.image.load("./Pacman Python/assets/ghost_images/red.png"), (45, 45))
blinky_x = 56
blinky_y = 58
blinky_direction = 0

pinky_img = pygame.transform.scale(pygame.image.load("./Pacman Python/assets/ghost_images/pink.png"), (45, 45))
pinky_x = 440
pinky_y = 438
pinky_direction = 2

inky_img = pygame.transform.scale(pygame.image.load("./Pacman Python/assets/ghost_images/blue.png"), (45, 45))
inky_x = 440
inky_y = 388
inky_direction = 2

clyde_img = pygame.transform.scale(pygame.image.load("./Pacman Python/assets/ghost_images/orange.png"), (45, 45))
clyde_x = 440
clyde_y = 438
clyde_direction = 2

spooked_img = pygame.transform.scale(pygame.image.load("./Pacman Python/assets/ghost_images/powerup.png"), (45, 45))
dead_img = pygame.transform.scale(pygame.image.load("./Pacman Python/assets/ghost_images/dead.png"), (45, 45))

ghost_speeds = [2, 2, 2, 2] 

# functions

def draw_board():
    for i in range(len(level)):
        for j in range(len(level[i])):
            if level[i][j] == 1:
                pygame.draw.circle(screen, 'white', (j*num2 + (0.5*num2), i*num1 + (0.5*num1)), 4)
            if level[i][j] == 2 and not flicker:
                pygame.draw.circle(screen, 'white', (j*num2 + (0.5*num2), i*num1 + (0.5*num1)), 10)
            if level[i][j] == 3:
                pygame.draw.line(screen, color, (j*num2 + (0.5*num2), i*num1), (j*num2 + (0.5*num2), i*num1 + num1), 3)
            if level[i][j] == 4:
                pygame.draw.line(screen, color, (j*num2, i*num1 + (0.5*num1)), (j*num2 + num2, i*num1 + (0.5*num1)), 3)
            if level[i][j] == 5:
                pygame.draw.arc(screen, color, [(j*num2 - (num2*0.5)) + 2, (i*num1 + (num1*0.5)), num2, num1], 0, PI/2, 3)
            if level[i][j] == 6:
                pygame.draw.arc(screen, color, [(j*num2 + (num2*0.5)), (i*num1 + (num1*0.5)), num2, num1], PI/2, PI, 3)
            if level[i][j] == 7:
                pygame.draw.arc(screen, color, [(j*num2 + (num2*0.5)), (i*num1 - (num1*0.4)), num2, num1], PI, 3*PI/2, 3)
            if level[i][j] == 8:
                pygame.draw.arc(screen, color, [(j*num2 - (num2*0.4)) - 2, (i*num1 - (num1*0.4)), num2, num1], 3*PI/2, 2*PI, 3) 
            if level[i][j] == 9:
              

# main game loop 

run = True
while run:
    timer.tick(fps)
    if counter < 19:
        counter += 1
        if counter > 3:
            flicker = False
    else:
        counter = 0
        flicker = True
    if powerup and power_counter < 600:
        power_counter += 1
    elif powerup and power_counter >= 600:
        power_counter = 0
        powerup = False
        eaten_ghost = [False, False, False, False]
    if startup_counter < 180 and not game_over and not game_won:
        moving = False
        startup_counter += 1
    else:
        moving = True

    pygame.display.flip()
pygame.quit()