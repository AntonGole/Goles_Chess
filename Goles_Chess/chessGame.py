import pygame
from const import *
from dragger import Dragger
from chessBoard import ChessBoard


# Return a new chess board in the form of a 2x2 array

# 0 = Empty piece
# 1, -1 = White pawn, Black pawn
# 2, -2 = White knight, Black knight
# 3, -3 = White bishop, Black bishop
# 4, -4 = White rook, Black rook
# 5, -5 = White queen, Black queen
# 6, -6 = White king, Black king

def newChessBoard():
    return [[-4, -2, -3, -5, -6, -3, -2, -4],
            [-1, -1, -1, -1, -1, -1, -1, -1],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [1, 1, 1, 1, 1, 1, 1, 1],
            [4, 2, 3, 5, 6, 3, 2, 4]]


def testChessBoard():
    return [[-4, 0, 0, 0, -6, 0, 0, -4],
            [-1, -1, -1, -1, -1, -1, -1, -1],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [1, 1, 1, 1, 1, 1, 1, 1],
            [4, 0, 0, 0, 6, 0, 0, 4]]


def in_range(move):
    return max(move[0], move[1]) < 8 and min(move[0], move[1]) > -1


def calculate_diagonal_moves(board, piece, row, col):
    valid_moves = []

    r = row
    c = col

    # NW

    while True:
        r -= 1
        c -= 1

        if not in_range((r, c)):
            break
        # If white piece
        if piece > 0:
            if board.get(r, c) < 0:
                valid_moves.append((row, col, r, c))
                break
            elif board.get(r, c) > 0:
                break

        # If black piece
        elif piece < 0:
            if board.get(r, c) > 0:
                valid_moves.append((row, col, r, c))
                break
            elif board.get(r, c) < 0:
                break

        valid_moves.append((row, col, r, c))

    r = row
    c = col

    # NE

    while True:
        r -= 1
        c += 1

        if not in_range((r, c)):
            break
        # If white piece
        if piece > 0:
            if board.get(r, c) < 0:
                valid_moves.append((row, col, r, c))
                break
            elif board.get(r, c) > 0:
                break

        # If black piece
        elif piece < 0:
            if board.get(r, c) > 0:
                valid_moves.append((row, col, r, c))
                break
            elif board.get(r, c) < 0:
                break

        valid_moves.append((row, col, r, c))

    r = row
    c = col

    # SE

    while True:
        r += 1
        c += 1

        if not in_range((r, c)):
            break
        # If white piece
        if piece > 0:
            if board.get(r, c) < 0:
                valid_moves.append((row, col, r, c))
                break
            elif board.get(r, c) > 0:
                break

        # If black piece
        elif piece < 0:
            if board.get(r, c) > 0:
                valid_moves.append((row, col, r, c))
                break
            elif board.get(r, c) < 0:
                break

        valid_moves.append((row, col, r, c))

    r = row
    c = col

    # SW

    while True:
        r += 1
        c -= 1

        if not in_range((r, c)):
            break
        # If white piece
        if piece > 0:
            if board.get(r, c) < 0:
                valid_moves.append((row, col, r, c))
                break
            elif board.get(r, c) > 0:
                break

        # If black piece
        elif piece < 0:
            if board.get(r, c) > 0:
                valid_moves.append((row, col, r, c))
                break
            elif board.get(r, c) < 0:
                break

        valid_moves.append((row, col, r, c))

    return valid_moves


def calculate_straight_moves(board, piece, row, col):
    valid_moves = []
    r = row

    # N

    while True:
        r -= 1

        if not in_range((r, col)):
            break
        # If white piece
        if piece > 0:
            if board.get(r, col) < 0:
                valid_moves.append((row, col, r, col))
                break
            elif board.get(r, col) > 0:
                break

        # If black piece
        elif piece < 0:
            if board.get(r, col) > 0:
                valid_moves.append((row, col, r, col))
                break
            elif board.get(r, col) < 0:
                break

        valid_moves.append((row, col, r, col))

    c = col

    # E

    while True:
        c += 1

        if not in_range((row, c)):
            break
        # If white piece
        if piece > 0:
            if board.get(row, c) < 0:
                valid_moves.append((row, col, row, c))
                break
            elif board.get(row, c) > 0:
                break

        # If black piece
        elif piece < 0:
            if board.get(row, c) > 0:
                valid_moves.append((row, col, row, c))
                break
            elif board.get(row, c) < 0:
                break

        valid_moves.append((row, col, row, c))

    r = row

    # S

    while True:
        r += 1

        if not in_range((r, col)):
            break
        # If white piece
        if piece > 0:
            if board.get(r, col) < 0:
                valid_moves.append((row, col, r, col))
                break
            elif board.get(r, col) > 0:
                break

        # If black piece
        elif piece < 0:
            if board.get(r, col) > 0:
                valid_moves.append((row, col, r, col))
                break
            elif board.get(r, col) < 0:
                break

        valid_moves.append((row, col, r, col))

    c = col

    # W

    while True:
        c -= 1

        if not in_range((row, c)):
            break
        # If white piece
        if piece > 0:
            if board.get(row, c) < 0:
                valid_moves.append((row, col, row, c))
                break
            elif board.get(row, c) > 0:
                break

        # If black piece
        elif piece < 0:
            if board.get(row, c) > 0:
                valid_moves.append((row, col, row, c))
                break
            elif board.get(row, c) < 0:
                break

        valid_moves.append((row, col, row, c))

    return valid_moves


def calculate_moves(board, piece, row, col):
    """
        Calculate all possible (valid) moves of a piece from a specific position, return type: 4-tuple
    """

    valid_moves = []

    # White pawn moves
    if piece == 1:
        # One step forward
        possible_moves = [(row - 1, col)]

        # Two steps forward
        if row == 6 and board.get(row - 1, col) == 0:
            possible_moves.append((row-2, col))

        # Diagonal steps
        if in_range((row - 1, col - 1)):
            if board.get(row - 1, col - 1) < 0:
                valid_moves.append((row, col, row - 1, col - 1))
        if in_range((row - 1, col + 1)):
            if board.get(row - 1, col + 1) < 0:
                valid_moves.append((row, col, row - 1, col + 1))

        # En passant
        # If the en passant col is 1 step away from pawns col and the en passant row is 1 step above the pawns row
        if board.en_passant is not None:
            if abs(col - board.en_passant[1]) == 1 and row - board.en_passant[0] == 1:
                valid_moves.append((row, col, board.en_passant[0], board.en_passant[1]))

        for possible_move in possible_moves:
            if board.get(possible_move[0], possible_move[1]) == 0:
                # Add the possible move as a 4-tuple to the list of valid moves
                valid_moves.append((row, col, possible_move[0], possible_move[1]))

    # White knight moves
    if piece == 2:
        possible_moves = [
            (row - 2, col + 1),
            (row - 1, col + 2),
            (row + 1, col + 2),
            (row + 2, col + 1),
            (row + 2, col - 1),
            (row + 1, col - 2),
            (row - 1, col - 2),
            (row- 2, col - 1),
        ]
        for possible_move in possible_moves:
            if in_range(possible_move):
                if board.get(possible_move[0], possible_move[1]) < 1:
                    # Add the possible move as a 4-tuple to the list of valid moves
                    valid_moves.append((row, col, possible_move[0], possible_move[1]))

    # White king moves
    if piece == 6:
        possible_moves = [
            (row - 1, col),
            (row - 1, col + 1),
            (row, col + 1),
            (row + 1, col + 1),
            (row + 1, col),
            (row + 1, col - 1),
            (row, col - 1),
            (row - 1, col - 1),
        ]

        # Castling
        if not board.whiteCastled:
            if not board.whiteRook1_moved:
                c = col
                while True:
                    c -= 1

                    if not board.get(row, c) == 0:
                        break

                    if c == 1:
                        valid_moves.append((row, col, row, col-2))

            if not board.whiteRook2_moved:
                c = col
                while True:
                    c += 1

                    if not board.get(row, c) == 0:
                        break

                    if c == 6:
                        valid_moves.append((row, col, row, col + 2))

        for possible_move in possible_moves:
            if in_range(possible_move):
                if board.get(possible_move[0], possible_move[1]) < 1:
                    # Add the possible move as a 4-tuple to the list of valid moves
                    valid_moves.append((row, col, possible_move[0], possible_move[1]))

    # Black pawn moves
    if piece == -1:
        # One step forward
        possible_moves = [(row + 1, col)]

        # Two steps forward
        if row == 1 and board.get(row + 1, col) == 0:
            possible_moves.append((row + 2, col))

        # Diagonal steps
        if in_range((row + 1, col - 1)):
            if board.get(row + 1, col - 1) > 0:
                valid_moves.append((row, col, row + 1, col - 1))
        if in_range((row + 1, col + 1)):
            if board.get(row + 1, col + 1) > 0:
                valid_moves.append((row, col, row + 1, col + 1))

        # En passant
        # If the en passant col is 1 step away from pawns col and the en passant row is 1 step below the pawns row
        if board.en_passant is not None:
            if abs(col - board.en_passant[1]) == 1 and row - board.en_passant[0] == -1:
                valid_moves.append((row, col, board.en_passant[0], board.en_passant[1]))

        for possible_move in possible_moves:
            if board.get(possible_move[0], possible_move[1]) == 0:
                # Add the possible move as a 4-tuple to the list of valid moves
                valid_moves.append((row, col, possible_move[0], possible_move[1]))

    # Black knight moves
    if piece == -2:
        possible_moves = [
            (row - 2, col + 1),
            (row - 1, col + 2),
            (row + 1, col + 2),
            (row + 2, col + 1),
            (row + 2, col - 1),
            (row + 1, col - 2),
            (row - 1, col - 2),
            (row - 2, col - 1),
        ]
        for possible_move in possible_moves:
            if in_range(possible_move):
                if board.get(possible_move[0], possible_move[1]) > -1:
                    # Add the possible move as a 4-tuple to the list of valid moves
                    valid_moves.append((row, col, possible_move[0], possible_move[1]))

    # Black king moves
    if piece == -6:
        possible_moves = [
            (row - 1, col),
            (row - 1, col + 1),
            (row, col + 1),
            (row + 1, col + 1),
            (row + 1, col),
            (row + 1, col - 1),
            (row, col - 1),
            (row - 1, col - 1),
        ]

        # Castling
        if not board.blackCastled:
            if not board.blackRook1_moved:
                c = col
                while True:
                    c -= 1

                    if not board.get(row, c) == 0:
                        break

                    if c == 1:
                        valid_moves.append((row, col, row, col - 2))

            if not board.blackRook2_moved:
                c = col
                while True:
                    c += 1

                    if not board.get(row, c) == 0:
                        break

                    if c == 6:
                        valid_moves.append((row, col, row, col + 2))

        for possible_move in possible_moves:
            if in_range(possible_move):
                if board.get(possible_move[0], possible_move[1]) > -1:
                    # Add the possible move as a 4-tuple to the list of valid moves
                    valid_moves.append((row, col, possible_move[0], possible_move[1]))

    # White + Black bishop moves
    if abs(piece) == 3:
        return calculate_diagonal_moves(board, piece, row, col)

    # White + Black rook moves
    if abs(piece) == 4:
        return calculate_straight_moves(board, piece, row, col)

    # White + Black queen moves
    if abs(piece) == 5:
        return calculate_diagonal_moves(board, piece, row, col) + calculate_straight_moves(board, piece, row, col)

    return valid_moves


def inCheck(color, game, board):
    if color == WHITE:
        for r, row in enumerate(board):
            for c, col in enumerate(row):
                if board[r][c] < 0:
                    new_moves = calculate_moves(game, board[r][c], r, c)
                    if not len(new_moves) == 0:
                        for move in new_moves:
                            if board[move[2]][move[3]] == 6:
                                return True
        return False

    if color == BLACK:
        for r, row in enumerate(board):
            for c, col in enumerate(row):
                if board[r][c] > 0:
                    new_moves = calculate_moves(game, board[r][c], r, c)
                    if not len(new_moves) == 0:
                        for move in new_moves:
                            if board[move[2]][move[3]] == -6:
                                return True
        return False


def loadImages():
    img_list = []
    pieceCodes = [1, 2, 3, 4, 5, 6, -1, -2, -3, -4, -5, -6]
    pieceNames = ['wP', 'wN', 'wB', 'wR', 'wQ', 'wK', 'bP', 'bN', 'bB', 'bR', 'bQ', 'bK']

    for name in pieceNames:
        img_list.append(pygame.image.load(f'images/{name}.png'))

    return dict(zip(pieceCodes, img_list))


class ChessGame:

    def __init__(self):
        self.chessBoard = ChessBoard(newChessBoard(), WHITE, False, False, None, False, False, False, False, None)
        self.images = loadImages()
        self.dragger = Dragger()

    def __copy__(self):
        board_copy = self.chessBoard.board

        return ChessGame()

    # Show methods

    def show_bg(self, surface):
        for row in range(ROWS):
            for col in range(COLS):
                if (row + col) % 2 == 0:
                    color = (238, 238, 210)
                else:
                    color = (118, 150, 86)

                rect = (col * SQSIZE, row * SQSIZE, SQSIZE, SQSIZE)

                pygame.draw.rect(surface, color, rect)

    def show_pieces(self, surface):
        for row in range(ROWS):
            for col in range(COLS):
                if self.chessBoard.board[row][col] == 0:
                    continue
                if self.dragger.dragging:
                    if self.dragger.initial_col == col and self.dragger.initial_row == row:
                        continue
                piece = self.chessBoard.board[row][col]
                img_center = col * SQSIZE + SQSIZE // 2, row * SQSIZE + SQSIZE // 2
                texture_rect = self.images.get(piece).get_rect(center=img_center)
                surface.blit(self.images.get(piece), texture_rect)

    def show_moves(self, surface):
        if self.dragger.dragging:
            piece = self.dragger.piece

            moves = calculate_moves(self.chessBoard, piece, self.dragger.initial_row, self.dragger.initial_col)

            for move in moves:
                # color
                color = '#D6D6BD' if (move[2] + move[3]) % 2 == 0 else '#6A874D'

                # position of circle
                if self.chessBoard.board[move[2]][move[3]] == 0:
                    circle_pos = (move[3] * SQSIZE + SQSIZE // 2, move[2] * SQSIZE + SQSIZE // 2)
                    pygame.draw.circle(surface, color, circle_pos, 10)
                else:
                    circle_pos = (move[3] * SQSIZE + SQSIZE // 2, move[2] * SQSIZE + SQSIZE // 2)
                    pygame.draw.circle(surface, color, circle_pos, SQSIZE//2, width=4)
