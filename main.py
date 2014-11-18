import pygame
from pygame.locals import *

from gamelib import Board
from elements import *

class DarkBomb2Game(Board):
    BLACK = pygame.Color('black')
    GREEN  = pygame.Color('green')
    YELLOW = pygame.Color('yellow')
    RED = pygame.Color('red')

    def __init__(self):
        super(DarkBomb2Game, self).__init__('DarkBomb_2', DarkBomb2Game.BLACK, (440,400), 15)
        self.player = Player(radius = 20, color = DarkBomb2Game.GREEN, pos = (20,20))

    def update(self):
        if self.is_key_pressed(K_UP):
            self.player.move_up()
        if self.is_key_pressed(K_DOWN):
            self.player.move_down()
        if self.is_key_pressed(K_RIGHT):
            self.player.move_rigth()
        if self.is_key_pressed(K_LEFT):
            self.player.move_left()

    def render(self, surface):
        self.player.render(surface)

def main():
    game = DarkBomb2Game()
    game.run()

if __name__ == "__main__":
    main()
