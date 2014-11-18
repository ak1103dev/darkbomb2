import pygame
from pygame.locals import *

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
        (self.x, self.y) = pos
        self.radius = radius
        self.color = color

    def render(self, surface):
        pos = (int(self.x), int(self.y))
        pygame.draw.circle(surface, self.color, pos, self.radius, 0)



