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

# Ghost class

class Ghost:
    def __init__(self, x_coord, y_coord, target, speed, img, direct, dead, box, id):
        self.x_pos = x_coord
        self.y_pos = y_coord
        self.center_x = self.x_pos + 22
        self.center_y = self.y_pos + 22
        self.target = target
        self.speed = speed
        self.img = img
        self.direction = direct
        self.dead = dead
        self.in_box = box
        self.id = id
        self.turns, self.in_box = self.check_collisions()
        self.rect = self.draw()

    def draw(self):
        if (not powerup and not self.dead) or (eaten_ghost[self.id] and powerup and not self.dead):
            screen.blit(self.img, (self.x_pos, self.y_pos))
        elif powerup and not self.dead and not eaten_ghost[self.id]:
            screen.blit(spooked_img, (self.x_pos, self.y_pos))
        else:
            screen.blit(dead_img, (self.x_pos, self.y_pos))
        ghost_rect = pygame.rect.Rect((self.center_x - 18, self.center_y - 18), (36, 36))
        return ghost_rect

    def check_collisions(self):
        pass

    def move_clyde(self):
        pass

    def move_blinky(self):
        pass

    def move_inky(self):
        pass

    def move_pinky(self):
        pass  