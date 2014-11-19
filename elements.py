import pygame
from pygame.locals import *
from random import randint

class Player(object):

    def __init__(self, radius, color, pos):
        (self.x, self.y) = pos
        self.radius = radius
        self.color = color

    def move_up(self):
        self.y -= 40

    def move_down(self):
        self.y += 40

    def move_left(self):
        self.x -= 40

    def move_rigth(self):
        self.x += 40
    
    def render(self, surface):
        pos = (int(self.x), int(self.y))
        pygame.draw.circle(surface, self.color, pos, self.radius, 0)

class Bomb(object):

    def __init__(self, radius, color, pos):
        self.x = pos[0] + 40*randint(-5,5)
        self.y = pos[1] + 40*randint(-5,5)
        self.radius = radius
        self.color = color

    def check_hit(self, player):
        return (int(self.x), int(self.y)) == (player.x, player.y)
    
    def render(self, surface):
        pos = (int(self.x), int(self.y))
        pygame.draw.circle(surface, self.color, pos, self.radius, 0)



