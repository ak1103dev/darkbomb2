import pygame
from pygame.locals import *

from gamelib import Board
from elements import *

class DarkBomb2Game(Board):
    BLACK = pygame.Color('black')
    WHITE = pygame.Color('white')
    GREEN  = pygame.Color('green')
    YELLOW = pygame.Color('yellow')
    RED = pygame.Color('red')

    def __init__(self):
        super(DarkBomb2Game, self).__init__('DarkBomb_2', DarkBomb2Game.BLACK, (440,440), 15)
        self.player = Player(radius = 20, color = DarkBomb2Game.GREEN, pos = (20,20))
        self.bomb = Bomb(radius = 20,
                        color = DarkBomb2Game.WHITE, 
                        pos = (self.window_size[0]/2,self.window_size[1]/2))

    def update(self):

        if self.is_key_pressed(K_UP):
            self.player.move_up()
        elif self.is_key_pressed(K_DOWN):
            self.player.move_down()
        elif self.is_key_pressed(K_RIGHT):
            self.player.move_rigth()
        elif self.is_key_pressed(K_LEFT):
            self.player.move_left()

    def render(self, surface):
        self.player.render(surface)
        self.bomb.render(surface)

def main():
    game = DarkBomb2Game()
    game.run()

if __name__ == "__main__":
    main()
