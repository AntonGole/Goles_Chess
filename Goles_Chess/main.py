import pygame
import sys

from const import *
from chessGame import ChessGame


class Main:

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption('Goles Chess')
        self.game = ChessGame()

    def mainloop(self):

        screen = self.screen
        game = self.game
        board = self.game.board
        dragger = self.game.dragger

        while True:
            game.show_bg(screen)
            game.show_pieces(screen)

            if dragger.dragging:
                dragger.update_blit(screen, game.images)

            for event in pygame.event.get():

                # click event
                if event.type == pygame.MOUSEBUTTONDOWN:
                    dragger.update_mouse(event.pos)

                    clicked_row = dragger.mouseY // SQSIZE
                    clicked_col = dragger.mouseX // SQSIZE
                    piece = board[clicked_row][clicked_col]
                    if piece != 0:
                        dragger.save_initial(event.pos)
                        dragger.drag_piece(piece)

                # mouse motion event
                elif event.type == pygame.MOUSEMOTION:
                    if dragger.dragging:
                        dragger.update_mouse(event.pos)
                        dragger.update_blit(screen, game.images)

                # click release event
                elif event.type == pygame.MOUSEBUTTONUP:
                    dragger.undrag_piece()

                # quit application event
                elif event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            pygame.display.update()


main = Main()
main.mainloop()
