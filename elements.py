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
    
    def player_in_windows(self):
        if self.x == 0:
            self.x = 0
        elif self.x == self.window_size[0]:
            self.x = self.window_size[0]
        elif self.y == 0:
            self.y = 0
        elif self.y == self.window_size[1]:
            self.y = self.window_size[1]

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



