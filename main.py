import pygame
from pygame.locals import *

from gamelib import Board
#from elements import *

class DarkBomb2Game(Board):
    Black = pygame.Color('black')
    Green  = pygame.Color('green')
    Yellow = pygame.Color('yellow')
    Red = pygame.Color('red')

    def __init__(self):
        super(DarkBomb2Game, self).__init__('DarkBomb_2', DarkBomb2Game.Black, (440,400), 100)

    def update(self):
        pass

    def render(self, surface):
        pass

def main():
    game = DarkBomb2Game()
    game.run()

if __name__ == "__main__":
    main()
