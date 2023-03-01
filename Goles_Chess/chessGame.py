import copy

import pygame
from const import *
from dragger import Dragger
from chessBoard import ChessBoard


# Return a new chess board in the form of a 2x2 array

# 0 = Empty piece
# 1, -1 = White Pawn, Black Pawn
# 2, -2 = White Knight, Black Knight
# 3, -3 = White Bishop, Black Bishop
# 4, -4 = White Rook, Black Rook
# 5, -5 = White Queen, Black Queen
# 6, -6 = White King, Black King

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
    return [[0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, -4, 0, 0, 0],
            [0, 0, 0, 6, 0, 0, 0, 0],
            [0, 0, -5, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0]]


def in_range(move):
    return max(move[0], move[1]) < 8 and min(move[0], move[1]) > -1


def calculate_pseudo_moves(chessBoard, color):
    """
    calculate_pseudo_moves calculates all possible moves for the given color without considering checks and pins

    :param chessBoard: An instance of ChessBoard that contains relevant information about the game
    :param color: Which color to calculate
    """

    board = chessBoard.board
    whiteCastled = chessBoard.whiteCastled
    blackCastled = chessBoard.blackCastled

    whiteRook1_moved = chessBoard.whiteRook1_moved
    whiteRook2_moved = chessBoard.whiteRook2_moved

    blackRook1_moved = chessBoard.blackRook1_moved
    blackRook2_moved = chessBoard.blackRook2_moved

    # Variable that stores all pseudo-moves as 4 tuples (start_row, start_col, end_row, end_col)
    pseudo_moves = []

    # Iterate through all squares
    for row in range(ROWS):
        for col in range(COLS):
            piece = board[row][col]

            # White pieces
            if piece > 0 and color == WHITE:

                # White pawn moves
                if piece == WHITE_PAWN:
                    # One step forward
                    if board[row - 1][col] == 0:
                        pseudo_moves.append((row, col, row - 1, col))

                    # Two steps forward
                    if row == 6 and board[row - 2][col] == 0 and board[row - 1][col] == 0:
                        pseudo_moves.append((row, col, row - 2, col))

                    # Diagonal steps
                    if in_range((row - 1, col - 1)):
                        if board[row - 1][col - 1] < 0:
                            pseudo_moves.append((row, col, row - 1, col - 1))
                    if in_range((row - 1, col + 1)):
                        if board[row - 1][col + 1] < 0:
                            pseudo_moves.append((row, col, row - 1, col + 1))

                    # En passant
                    # If the en passant col is 1 step away from pawns col and the en passant row is 1 step above the
                    # pawns row
                    if chessBoard.en_passant is not None:
                        if abs(col - chessBoard.en_passant[1]) == 1 and row - chessBoard.en_passant[0] == 1:
                            pseudo_moves.append((row, col, chessBoard.en_passant[0], chessBoard.en_passant[1]))

                # White knight moves
                if piece == WHITE_KNIGHT:
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
                            if board[possible_move[0]][possible_move[1]] < 1:
                                pseudo_moves.append((row, col, possible_move[0], possible_move[1]))

                # White king moves
                if piece == WHITE_KING:
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
                    if not whiteCastled:
                        if not whiteRook1_moved:
                            c = col
                            while True:
                                c -= 1

                                if not board[row][c] == 0:
                                    break

                                if c == 1:
                                    pseudo_moves.append((row, col, row, 1))
                                    break

                        if not whiteRook2_moved:
                            c = col
                            while True:
                                c += 1

                                if not board[row][c] == 0:
                                    break

                                if c == 6:
                                    pseudo_moves.append((row, col, row, 6))
                                    break

                    for possible_move in possible_moves:
                        if in_range(possible_move):
                            if board[possible_move[0]][possible_move[1]] < 1:
                                pseudo_moves.append((row, col, possible_move[0], possible_move[1]))

                # Sliding pieces

                # White bishop moves
                if piece == WHITE_BISHOP:
                    pseudo_moves.extend(calculate_diagonal_moves(board, color, row, col))

                # White rook moves
                if piece == WHITE_ROOK:
                    pseudo_moves.extend(calculate_straight_moves(board, color, row, col))

                # White queen moves
                if piece == WHITE_QUEEN:
                    pseudo_moves.extend(calculate_diagonal_moves(board, color, row, col) +
                                        calculate_straight_moves(board, color, row, col))

            # Black pieces
            elif piece < 0 and color == BLACK:

                # BLACK pawn moves
                if piece == BLACK_PAWN:
                    # One step forward
                    if board[row + 1][col] == 0:
                        pseudo_moves.append((row, col, row + 1, col))

                    # Two steps forward
                    if row == 1 and board[row + 2][col] == 0 and board[row + 1][col] == 0:
                        pseudo_moves.append((row, col, row + 2, col))

                    # Diagonal steps
                    if in_range((row + 1, col - 1)):
                        if board[row + 1][col - 1] > 0:
                            pseudo_moves.append((row, col, row + 1, col - 1))
                    if in_range((row + 1, col + 1)):
                        if board[row + 1][col + 1] > 0:
                            pseudo_moves.append((row, col, row + 1, col + 1))

                    # En passant
                    # If the en passant col is 1 step away from pawns col and the en passant row is 1 step above the
                    # pawns row
                    if chessBoard.en_passant is not None:
                        if abs(col - chessBoard.en_passant[1]) == 1 and row - chessBoard.en_passant[0] == -1:
                            pseudo_moves.append((row, col, chessBoard.en_passant[0], chessBoard.en_passant[1]))

                # Black knight moves
                if piece == BLACK_KNIGHT:
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
                            if board[possible_move[0]][possible_move[1]] > -1:
                                pseudo_moves.append((row, col, possible_move[0], possible_move[1]))

                # White king moves
                if piece == BLACK_KING:
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
                    if not blackCastled:
                        if not blackRook1_moved:
                            c = col
                            while True:
                                c -= 1

                                if not board[row][c] == 0:
                                    break

                                if c == 1:
                                    pseudo_moves.append((row, col, row, 1))
                                    break

                        if not blackRook2_moved:
                            c = col
                            while True:
                                c += 1

                                if not board[row][c] == 0:
                                    break

                                if c == 6:
                                    pseudo_moves.append((row, col, row, 6))
                                    break

                    for possible_move in possible_moves:
                        if in_range(possible_move):
                            if board[possible_move[0]][possible_move[1]] > -1:
                                pseudo_moves.append((row, col, possible_move[0], possible_move[1]))

                # Sliding pieces

                # Black bishop moves
                if piece == BLACK_BISHOP:
                    pseudo_moves.extend(calculate_diagonal_moves(board, color, row, col))

                # Black rook moves
                if piece == BLACK_ROOK:
                    pseudo_moves.extend(calculate_straight_moves(board, color, row, col))

                # Black queen moves
                if piece == BLACK_QUEEN:
                    pseudo_moves.extend(calculate_diagonal_moves(board, color, row, col) +
                                        calculate_straight_moves(board, color, row, col))

    return pseudo_moves


def calculate_legal_moves(chessBoard, color):
    """
    calculate_legal_moves calculates all possible moves for the given color considering checks and pins

    :param chessBoard: An instance of ChessBoard that contains relevant information about the game
    :param color: Which color to calculate
    """

    # Variable that stores all legal moves as 4 tuples (start_row, start_col, end_row, end_col)
    legal_moves = []

    pseudo_moves = calculate_pseudo_moves(chessBoard, color)

    for move in pseudo_moves:
        new_chessBoard = copy.deepcopy(chessBoard)
        new_chessBoard.move(move)

        # Check if white king is in check after making the move, remove the move from the legal_moves list
        if color == WHITE:
            if not inCheck(new_chessBoard, WHITE):
                legal_moves.append(move)

        # Check if black king is in check after making the move, remove the move from the legal_moves list
        else:
            if not inCheck(new_chessBoard, BLACK):
                legal_moves.append(move)

    return legal_moves


def calculate_legal_moves_v2(chessBoard, color):
    """
    calculate_legal_moves calculates all possible moves for the given color considering checks and pins

    :param chessBoard: An instance of ChessBoard that contains relevant information about the game
    :param color: Which color to calculate
    """

    # Variable that stores all legal moves as 4 tuples (start_row, start_col, end_row, end_col)
    legal_moves = []

    pseudo_moves = calculate_pseudo_moves(chessBoard, color)

    for move in pseudo_moves:
        move_info = chessBoard.move(move)

        # Check if white king is in check after making the move, add the move to the legal_moves list
        if color == WHITE:
            if not inCheck(chessBoard, WHITE):
                legal_moves.append(move)
                chessBoard.undo_move(move_info)
            else:
                chessBoard.undo_move(move_info)

        # Check if black king is in check after making the move, ad the move to the legal_moves list
        else:
            if not inCheck(chessBoard, BLACK):
                legal_moves.append(move)
                chessBoard.undo_move(move_info)
            else:
                chessBoard.undo_move(move_info)

    return legal_moves


def calculate_diagonal_moves(board, color, row, col):
    """
        calculate_diagonal_moves calculates all possible diagonal moves from a given position

        :param board: 2D array that represents the game position
        :param color: Which color to calculate
        :param row: Row of square to calculate from
        :param col: Col of square to calculate from
    """

    valid_moves = []

    if color == WHITE:

        r = row
        c = col

        # NW

        while True:
            r -= 1
            c -= 1

            if not in_range((r, c)):
                break

            if board[r][c] < 0:
                valid_moves.append((row, col, r, c))
                break
            elif board[r][c] > 0:
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

            if board[r][c] < 0:
                valid_moves.append((row, col, r, c))
                break
            elif board[r][c] > 0:
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

            if board[r][c] < 0:
                valid_moves.append((row, col, r, c))
                break
            elif board[r][c] > 0:
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
            if color == WHITE:
                if board[r][c] < 0:
                    valid_moves.append((row, col, r, c))
                    break
                elif board[r][c] > 0:
                    break

            # If black piece
            else:
                if board[r][c] > 0:
                    valid_moves.append((row, col, r, c))
                    break
                elif board[r][c] < 0:
                    break

            valid_moves.append((row, col, r, c))

    # If black piece
    else:

        r = row
        c = col

        # NW

        while True:
            r -= 1
            c -= 1

            if not in_range((r, c)):
                break

            if board[r][c] > 0:
                valid_moves.append((row, col, r, c))
                break
            elif board[r][c] < 0:
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

            if board[r][c] > 0:
                valid_moves.append((row, col, r, c))
                break
            elif board[r][c] < 0:
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

            if board[r][c] > 0:
                valid_moves.append((row, col, r, c))
                break
            elif board[r][c] < 0:
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

            if board[r][c] > 0:
                valid_moves.append((row, col, r, c))
                break
            elif board[r][c] < 0:
                break

            valid_moves.append((row, col, r, c))

    return valid_moves


def calculate_straight_moves(board, color, row, col):
    """
        calculate_diagonal_moves calculates all possible straight moves from a given position

        :param board: 2D array that represents the game position
        :param color: Which color to calculate
        :param row: Row of square to calculate from
        :param col: Col of square to calculate from
    """

    valid_moves = []

    # If white piece
    if color == WHITE:

        r = row
        c = col

        # N

        while True:
            r -= 1

            if not in_range((r, c)):
                break

            if board[r][c] < 0:
                valid_moves.append((row, col, r, c))
                break
            elif board[r][c] > 0:
                break

            valid_moves.append((row, col, r, c))

        r = row
        c = col

        # E

        while True:
            c += 1

            if not in_range((r, c)):
                break

            if board[r][c] < 0:
                valid_moves.append((row, col, r, c))
                break
            elif board[r][c] > 0:
                break

            valid_moves.append((row, col, r, c))

        r = row
        c = col

        # S

        while True:
            r += 1

            if not in_range((r, c)):
                break

            if board[r][c] < 0:
                valid_moves.append((row, col, r, c))
                break
            elif board[r][c] > 0:
                break

            valid_moves.append((row, col, r, c))

        r = row
        c = col

        # W

        while True:
            c -= 1

            if not in_range((r, c)):
                break

            if board[r][c] < 0:
                valid_moves.append((row, col, r, c))
                break
            elif board[r][c] > 0:
                break

            valid_moves.append((row, col, r, c))

    # If black piece
    else:

        r = row
        c = col

        # N

        while True:
            r -= 1

            if not in_range((r, c)):
                break

            if board[r][c] > 0:
                valid_moves.append((row, col, r, c))
                break
            elif board[r][c] < 0:
                break

            valid_moves.append((row, col, r, c))

        r = row
        c = col

        # E

        while True:
            c += 1

            if not in_range((r, c)):
                break

            if board[r][c] > 0:
                valid_moves.append((row, col, r, c))
                break
            elif board[r][c] < 0:
                break

            valid_moves.append((row, col, r, c))

        r = row
        c = col

        # S

        while True:
            r += 1

            if not in_range((r, c)):
                break

            if board[r][c] > 0:
                valid_moves.append((row, col, r, c))
                break
            elif board[r][c] < 0:
                break

            valid_moves.append((row, col, r, c))

        r = row
        c = col

        # W

        while True:
            c -= 1

            if not in_range((r, c)):
                break

            if board[r][c] > 0:
                valid_moves.append((row, col, r, c))
                break
            elif board[r][c] < 0:
                break

            valid_moves.append((row, col, r, c))

    return valid_moves


def inCheck(chessBoard, color):

    board = chessBoard.board

    # Calculate attacks from opposing color
    if color == WHITE:
        attacks = calculate_pseudo_moves(chessBoard, BLACK)

        # Search for an attack on the white king square
        for attack in attacks:
            if board[attack[2]][attack[3]] == WHITE_KING:
                return True

        return False

    else:
        attacks = calculate_pseudo_moves(chessBoard, WHITE)

        # Search for an attack on the black king square
        for attack in attacks:
            if board[attack[2]][attack[3]] == BLACK_KING:
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
        self.chessBoard = ChessBoard(newChessBoard(), WHITE, False, False, False, False, False, False, None)
        self.images = loadImages()
        self.dragger = Dragger()

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
            moves = calculate_legal_moves(self.chessBoard, self.chessBoard.turn)

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
