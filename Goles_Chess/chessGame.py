import pygame
from const import *
from dragger import Dragger


# Return a new chess board in the form of a 2x2 array

# 0 = Empty piece
# 1, -1 = White pawn, Black pawn
# 2, -2 = White knight, Black knight
# 3, -3 = White bishop, Black bishop
# 4, -4 = White rook, Black rook
# 5, -5 = White queen, Black queen
# 6, -6 = White king, Black king

def newChessBoard():
    return [[10, 8, 9, 11, 12, 9, 8, 10],
            [7, 7, 7, 7, 7, 7, 7, 7],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [1, 1, 1, 1, 1, 1, 1, 1],
            [4, 2, 3, 5, 6, 3, 2, 4]]


def loadImages():
    img_list = []
    pieceNames = ['wP', 'wN', 'wB', 'wR', 'wQ', 'wK', 'bP', 'bN', 'bB', 'bR', 'bQ', 'bK']
    for name in pieceNames:
        img_list.append(pygame.image.load(f'images/{name}.png'))

    return img_list


class ChessGame:

    def __init__(self):
        self.board = newChessBoard()
        self.images = loadImages()
        self.dragger = Dragger()

    # Show methods

    def show_bg(self, surface):
        for row in range(ROWS):
            for col in range(COLS):
                if (row + col) % 2 == 0:
                    color = (234, 235, 200)
                else:
                    color = (119, 154, 88)

                rect = (col * SQSIZE, row * SQSIZE, SQSIZE, SQSIZE)

                pygame.draw.rect(surface, color, rect)

    def show_pieces(self, surface):
        for row in range(ROWS):
            for col in range(COLS):
                if self.board[row][col] == 0:
                    continue
                if self.dragger.dragging:
                    if self.dragger.initial_col == col and self.dragger.initial_row == row:
                        continue
                img_center = col * SQSIZE + SQSIZE // 2, row * SQSIZE + SQSIZE // 2
                texture_rect = self.images[self.board[row][col] - 1].get_rect(center=img_center)
                surface.blit(self.images[self.board[row][col] - 1], texture_rect)

