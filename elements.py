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

    def in_screen(self, window_size):
        if self.x <= 20:
            self.x = 20
        if self.x >= window_size[0]-20:
            self.x = window_size[0]-20
        if self.y <= 20:
            self.y = 20
        if self.y >= window_size[1]-20:
            self.y = window_size[1]-20

    def render(self, surface):
        pos = (int(self.x), int(self.y))
        pygame.draw.circle(surface, self.color, pos, self.radius, 0)

class Bomb(object):

    def __init__(self, radius, color, pos):
        self.x = pos[0] + 40*randint(-5,5)
        self.y = pos[1] + 40*randint(-5,5)
        self.radius = radius
        self.color = color
        self.number = 1

    def check_hit(self, player):
        return (int(self.x), int(self.y)) == (player.x, player.y)

    def check_closed(self, player):
        a = (abs(self.x-player.x), abs(self.y-player.y)) == (2*self.radius, 2*self.radius) 
        b = (abs(self.x-player.x), abs(self.y-player.y)) == (0, 2*self.radius) 
        c = (abs(self.x-player.x), abs(self.y-player.y)) == (2*self.radius, 0) 
        return a or b or c
    
    def render(self, surface):
        pos = (int(self.x), int(self.y))
        pygame.draw.circle(surface, self.color, pos, self.radius, 0)



