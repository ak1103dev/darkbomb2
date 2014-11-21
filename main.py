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

    game_over = False
    game_finish = False

    def __init__(self):
        super(DarkBomb2Game, self).__init__('DarkBomb_2', DarkBomb2Game.BLACK, (440,440), 12)
        self.reinit()

    def init(self):
        super(DarkBomb2Game, self).init()

    def reinit(self):
        self.player = Player(radius = 20, color = DarkBomb2Game.GREEN, pos = (20,20))
        self.bomb = Bomb(radius = 20,
                        color = DarkBomb2Game.WHITE, 
                        pos = (self.window_size[0]/2,self.window_size[1]/2))



    def update(self):
        """ Player can't go out of screen """
        if self.player.x <= 20:
            self.player.x = 20
        if self.player.x >= self.window_size[0]-20:
            self.player.x = self.window_size[0]-20
        if self.player.y <= 20:
            self.player.y = 20
        if self.player.y >= self.window_size[1]-20:
            self.player.y = self.window_size[1]-20

        """ Player's Movement """
        if self.is_key_pressed(K_UP):
            self.player.move_up()
        elif self.is_key_pressed(K_DOWN):
            self.player.move_down()
        elif self.is_key_pressed(K_RIGHT):
            self.player.move_rigth()
        elif self.is_key_pressed(K_LEFT):
            self.player.move_left()

        """ Check Hit """
        if self.bomb.check_hit(self.player):
            DarkBomb2Game.game_over = True

        """ Check Finished """
        if (self.player.x+20, self.player.y+20) == self.window_size:
            DarkBomb2Game.game_finish = True

        """ Restart When Game Over """
        if DarkBomb2Game.game_over:
            print 'game over' 
            self.reinit()
            DarkBomb2Game.game_over = False

        """ Add Bomb When Game Finished """    
        if DarkBomb2Game.game_finish:
            print 'you win'
            self.bomb.number += 1
            DarkBomb2Game.game_finish = False

        self.score_image = self.font.render('Bomb = %d' % self.bomb.number, 0, DarkBomb2Game.WHITE)

    def render(self, surface):
        self.bomb.render(surface)
        self.player.render(surface)
        surface.blit(self.score_image, (self.window_size[0] - 120,10))

def main():
    game = DarkBomb2Game()
    game.run()

if __name__ == "__main__":
    main()
