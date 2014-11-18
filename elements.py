import pygame
from pygame.locals import *

class Player(object):

    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color 
        self.radius = 40
    
    def render(self, surface):
        print "jkljljjljlj"
        pygame.draw.circle(surface, self.color, (self.x,self.y), self.radius, 0)

class Bomb(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
