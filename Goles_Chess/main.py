import pygame
import sys

from const import *
from chessGame import ChessGame, calculate_moves, inCheck
from chessEngine import ChessEngine


class Main:

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption('Goles Chess')
        self.game = ChessGame()
        self.engine = ChessEngine(RANDOM)

    def mainloop(self):

        screen = self.screen
        game = self.game
        board = self.game.chessBoard
        dragger = self.game.dragger

        while True:
            game.show_bg(screen)
            game.show_moves(screen)
            game.show_pieces(screen)

            if dragger.dragging:
                dragger.update_blit(screen, game.images)

            for event in pygame.event.get():

                # click event
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == LEFT:
                    dragger.update_mouse(event.pos)

                    clicked_row = dragger.mouseY // SQSIZE
                    clicked_col = dragger.mouseX // SQSIZE

                    piece = board.get(clicked_row, clicked_col)

                    if piece != 0 and ((piece > 0 and board.turn == 0) or (piece < 0 and board.turn == 1)):

                        dragger.save_initial(event.pos)
                        dragger.drag_piece(piece)

                        game.show_bg(screen)
                        game.show_moves(screen)
                        game.show_pieces(screen)

                # mouse motion event
                elif event.type == pygame.MOUSEMOTION:
                    if dragger.dragging:
                        dragger.update_mouse(event.pos)
                        game.show_bg(screen)
                        game.show_moves(screen)
                        game.show_pieces(screen)
                        dragger.update_blit(screen, game.images)

                # click release event
                elif event.type == pygame.MOUSEBUTTONUP and event.button == LEFT:
                    if (dragger.initial_row, dragger.initial_col, dragger.mouseY // SQSIZE, dragger.mouseX // SQSIZE) in calculate_moves(board, dragger.piece, dragger.initial_row, dragger.initial_col):
                        board.move((dragger.initial_row, dragger.initial_col, dragger.mouseY // SQSIZE, dragger.mouseX // SQSIZE))

                    dragger.undrag_piece()

                elif event.type == pygame.MOUSEBUTTONUP and event.button == RIGHT:
                    self.engine.move(board.turn, board)
                    #print(inCheck(BLACK, game, board))

                # quit application event
                elif event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            pygame.display.update()


if __name__ == "__main__":
    main = Main()
    main.mainloop()

