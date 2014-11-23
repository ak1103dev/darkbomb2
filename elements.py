import pygame
from pygame.locals import *
from random import randint

class Player(object):

    def __init__(self, radius, color, pos):
        (self.x, self.y) = pos
        self.radius = radius
        self.color = color

    def move_up(self):
        self.y -= 2*self.radius

    def move_down(self):
        self.y += 2*self.radius

    def move_left(self):
        self.x -= 2*self.radius

    def move_rigth(self):
        self.x += 2*self.radius

    def in_screen(self, window_size):
        if self.x < self.radius:
            self.x = self.radius
        if self.x > window_size[0]-self.radius:
            self.x = window_size[0]-self.radius
        if self.y < self.radius:
            self.y = self.radius
        if self.y > window_size[1]-self.radius:
            self.y = window_size[1]-self.radius

    def check_finished(self, window_size):
        return (self.x+self.radius, self.y+self.radius) == window_size

    def render(self, surface):
        pos = (int(self.x), int(self.y))
        pygame.draw.circle(surface, self.color, pos, self.radius, 0)
        
    def check_line_way(self, window_size):
        x = self.x
        y = self.y
        pos = [(x, y)]
        while (x, y) != (window_size[0] - self.radius, window_size[1] - self.radius):
            if randint(0,1) == 0:
                x += 2*self.radius
                if x > window_size[0]:
                    x -= 2*self.radius
                    y += 2*self.radius
            else:
                y += 2*self.radius
                if y > window_size[1]:
                    y -= 2*self.radius
                    x += 2*self.radius
            pos.append((x, y))
        return pos

class Bomb(object):

    def __init__(self, radius, color, pos):
        self.radius = radius
        self.color = color
        self.number = 1
        self.x = pos[0] + 2*self.radius*randint(-5,5)
        self.y = pos[1] + 2*self.radius*randint(-5,5)
        

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
