import pygame
import sys

from const import *
from chessGame import ChessGame, calculate_legal_moves, calculate_legal_moves_v2, calculate_pseudo_moves, inCheck, \
    newChessBoard
from chessEngine import ChessEngine, time_function
import time
from bitBoard.bitBoard import BitBoard
from copy import deepcopy

from ctypes import c_ulonglong as U64



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
                    if (dragger.initial_row, dragger.initial_col, dragger.mouseY // SQSIZE, dragger.mouseX // SQSIZE) in calculate_legal_moves(board, board.turn):
                        board.move((dragger.initial_row, dragger.initial_col, dragger.mouseY // SQSIZE, dragger.mouseX // SQSIZE))

                    dragger.undrag_piece()

                elif event.type == pygame.MOUSEBUTTONUP and event.button == RIGHT:
                    #time_function(calculate_legal_moves, board, WHITE)
                    #time_function(calculate_legal_moves_v2, board, WHITE)

                    bitboard = BitBoard(newChessBoard())
                    bitboard.show()
                    print(bitboard.whitePawns)
                    print(bitboard.whiteKnights)
                    print(bitboard.whiteBishops)
                    print(bitboard.whiteRooks)
                    print(bitboard.whiteQueens)
                    print(bitboard.whiteKing)
                    print(bitboard.blackPawns)
                    print(bitboard.blackKnights)
                    print(bitboard.blackBishops)
                    print(bitboard.blackRooks)
                    print(bitboard.blackQueens)
                    print(bitboard.blackKing)


                    for n in range(6):
                        tic = time.perf_counter()
                        print(self.engine.perft_v2(board, board.turn, n))
                        toc = time.perf_counter()
                        print(f"Calculated at depth {n} in {toc - tic:0.9f} seconds")

                    #list_1 = self.engine.perft_2(board, board.turn, 4)
                    #list_2 = self.engine.perft_3(board, board.turn, 4)

                    #print(time_function(self.engine.perft, board, board.turn, 4))

                    #print(len(list_1))
                    #print(len(list_2))

                    #board.print_board()
                    #board.undo_move(board.move_info)
                    #board.test()

                # quit application event
                elif event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            pygame.display.update()


if __name__ == "__main__":
    main = Main()
    main.mainloop()

