import pygame
from pygame.locals import *
from random import randint

from gamelib import Board
from elements import *

class DarkBomb2Game(Board):
    BLACK = pygame.Color('black')
    WHITE = pygame.Color('white')
    BLUE = pygame.Color('blue')
    GREEN  = pygame.Color('green')
    YELLOW = pygame.Color('yellow')
    RED = pygame.Color('red')

    game_over = False
    game_finish = False
    closed_bomb = False

    def __init__(self):
        self.init_board(DarkBomb2Game.BLACK)
        self.init_player(DarkBomb2Game.YELLOW)
        self.init_bombs()

    def init(self):
        super(DarkBomb2Game, self).init()

    def reinit(self):
        self.init_board(DarkBomb2Game.BLACK)
        self.init_bombs()
        self.init_player(DarkBomb2Game.YELLOW)

    def init_board(self, b_color):
        super(DarkBomb2Game, self).__init__('DarkBomb_2', b_color, (440,440), 12)
        
    def init_player(self, p_color):
        self.player = Player(radius = 20, color = p_color, pos = (20,20))

    def init_bombs(self):
        self.bombs = [] 
        self.bombs.append(Bomb(radius = 20,
                        color = DarkBomb2Game.BLACK, 
                        pos = (self.window_size[0]/2,self.window_size[1]/2))
                        )
        while (self.bombs[-1].x, self.bombs[-1].y) in self.player.check_line_way(self.window_size):
            self.bombs[-1].x = self.window_size[0]/2 + 2*self.bombs[-1].radius*randint(-5,5)
            self.bombs[-1].y = self.window_size[1]/2 + 2*self.bombs[-1].radius*randint(-5,5)

    def update(self):

        if not DarkBomb2Game.game_over:
            """ Player can't go out of screen """
            self.player.in_screen(self.window_size)

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
            if self.player.check_finished(self.window_size):
                DarkBomb2Game.game_finish = True

            """ Check Closed """
            for bomb in self.bombs:
                if bomb.check_closed(self.player):
                    DarkBomb2Game.closed_bomb = True
                    break

            """ Restart When Game Over """
            if DarkBomb2Game.game_over:
                print 'game over' 
                self.init_board(DarkBomb2Game.WHITE)
            if self.is_key_pressed(K_SPACE):
                DarkBomb2Game.game_over = False
                self.reinit()

            """ Add Bomb When Game Finished """    
            if DarkBomb2Game.game_finish:
                print 'you win ' + str(len(self.bombs))
                self.init_player(DarkBomb2Game.YELLOW)
                self.bombs.append(Bomb(radius = 20,
                            color = DarkBomb2Game.BLACK, 
                            pos = (self.window_size[0]/2,self.window_size[1]/2))
                            )
                DarkBomb2Game.game_finish = False

            """ Warning When Closed """
            if DarkBomb2Game.closed_bomb:
                self.player = Player(radius = 20, color = DarkBomb2Game.RED, 
                                    pos = (self.player.x, self.player.y))
                DarkBomb2Game.closed_bomb = False
            else:
                self.player = Player(radius = 20, color = DarkBomb2Game.YELLOW, 
                                    pos = (self.player.x, self.player.y))

            """ Render Bombs' Number """
            self.score_image = self.font.render('Bomb = %d' % len(self.bombs), 0, DarkBomb2Game.BLUE)

    def render(self, surface):
        pygame.draw.rect(surface, DarkBomb2Game.GREEN, pygame.Rect(self.window_size[0] - self.player.radius,
                                                                   self.window_size[1] -self.player.radius,
                                                                   2*self.player.x,2*self.player.y))
        for bomb in self.bombs:
            bomb.render(surface)
        self.player.render(surface)
        surface.blit(self.score_image, (self.window_size[0] - 120,10))

def main():
    game = DarkBomb2Game()
    game.run()

if __name__ == "__main__":
    main()
