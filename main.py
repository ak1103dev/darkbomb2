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
    closed_bomb = False

    def __init__(self):
        super(DarkBomb2Game, self).__init__('DarkBomb_2', DarkBomb2Game.BLACK, (440,440), 12)
        self.init_bombs()
        self.init_player()

    def init(self):
        super(DarkBomb2Game, self).init()

    def reinit(self):
        self.init_bombs()
        self.init_player()

    def init_player(self):
        self.player = Player(radius = 20, color = DarkBomb2Game.GREEN, pos = (20,20))

    def init_bombs(self):
        self.bombs = [] 
        self.bombs.append(Bomb(radius = 20,
                        color = DarkBomb2Game.WHITE, 
                        pos = (self.window_size[0]/2,self.window_size[1]/2))
                        )

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
        for bomb in self.bombs:
            if bomb.check_hit(self.player):
                DarkBomb2Game.game_over = True

        """ Check Finished """
        if (self.player.x+20, self.player.y+20) == self.window_size:
            DarkBomb2Game.game_finish = True

        """ Check Closed """
        for bomb in self.bombs:
            if bomb.check_closed(self.player):
                DarkBomb2Game.closed_bomb = True
                break

        """ Restart When Game Over """
        if DarkBomb2Game.game_over:
            print 'game over' 
            self.reinit()
            DarkBomb2Game.game_over = False

        """ Add Bomb When Game Finished """    
        if DarkBomb2Game.game_finish:
            print 'you win'
            self.init_player()
            self.bombs.append(Bomb(radius = 20,
                        color = DarkBomb2Game.WHITE, 
                        pos = (self.window_size[0]/2,self.window_size[1]/2))
                        )
            DarkBomb2Game.game_finish = False

        """ Warning When Closed """
        if DarkBomb2Game.closed_bomb:
            self.player = Player(radius = 20, color = DarkBomb2Game.YELLOW, 
                                pos = (self.player.x, self.player.y))
            DarkBomb2Game.closed_bomb = False
        else:
            self.player = Player(radius = 20, color = DarkBomb2Game.GREEN, 
                                pos = (self.player.x, self.player.y))

        """ Render Bombs' Number """
        self.score_image = self.font.render('Bomb = %d' % len(self.bombs), 0, DarkBomb2Game.WHITE)

    def render(self, surface):
        for bomb in self.bombs:
            bomb.render(surface)
        self.player.render(surface)
        surface.blit(self.score_image, (self.window_size[0] - 120,10))

def main():
    game = DarkBomb2Game()
    game.run()

if __name__ == "__main__":
    main()
