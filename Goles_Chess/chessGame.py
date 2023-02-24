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
            if board[r][c] < 0:
                valid_moves.append((row, col, r, c))
                break
            elif board[r][c] > 0:
                break

        # If black piece
        elif piece < 0:
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
        # If white piece
        if piece > 0:
            if board[r][c] < 0:
                valid_moves.append((row, col, r, c))
                break
            elif board[r][c] > 0:
                break

        # If black piece
        elif piece < 0:
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
        # If white piece
        if piece > 0:
            if board[r][c] < 0:
                valid_moves.append((row, col, r, c))
                break
            elif board[r][c] > 0:
                break

        # If black piece
        elif piece < 0:
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
        # If white piece
        if piece > 0:
            if board[r][c] < 0:
                valid_moves.append((row, col, r, c))
                break
            elif board[r][c] > 0:
                break

        # If black piece
        elif piece < 0:
            if board[r][c] > 0:
                valid_moves.append((row, col, r, c))
                break
            elif board[r][c] < 0:
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
            if board[r][col] < 0:
                valid_moves.append((row, col, r, col))
                break
            elif board[r][col] > 0:
                break

        # If black piece
        elif piece < 0:
            if board[r][col] > 0:
                valid_moves.append((row, col, r, col))
                break
            elif board[r][col] < 0:
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
            if board[row][c] < 0:
                valid_moves.append((row, col, row, c))
                break
            elif board[row][c] > 0:
                break

        # If black piece
        elif piece < 0:
            if board[row][c] > 0:
                valid_moves.append((row, col, row, c))
                break
            elif board[row][c] < 0:
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
            if board[r][col] < 0:
                valid_moves.append((row, col, r, col))
                break
            elif board[r][col] > 0:
                break

        # If black piece
        elif piece < 0:
            if board[r][col] > 0:
                valid_moves.append((row, col, r, col))
                break
            elif board[r][col] < 0:
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
            if board[row][c] < 0:
                valid_moves.append((row, col, row, c))
                break
            elif board[row][c] > 0:
                break

        # If black piece
        elif piece < 0:
            if board[row][c] > 0:
                valid_moves.append((row, col, row, c))
                break
            elif board[row][c] < 0:
                break

        valid_moves.append((row, col, row, c))

    return valid_moves


def calculate_moves(game, piece, row, col):
    """
        Calculate all possible (valid) moves of a piece from a specific position, return type: 4-tuple
    """

    board = game.board

    valid_moves = []

    # White pawn moves
    if piece == 1:
        # One step forward
        possible_moves = [(row - 1, col)]

        # Two steps forward
        if row == 6 and board[row - 1][col] == 0:
            possible_moves.append((row-2, col))

        # Diagonal steps
        if in_range((row - 1, col - 1)):
            if board[row - 1][col - 1] < 0:
                valid_moves.append((row, col, row - 1, col - 1))
        if in_range((row - 1, col + 1)):
            if board[row - 1][col + 1] < 0:
                valid_moves.append((row, col, row - 1, col + 1))

        # En passant
        # If the en passant col is 1 step away from pawns col and the en passant row is 1 step above the pawns row
        if game.en_passant is not None:
            if abs(col - game.en_passant[1]) == 1 and row - game.en_passant[0] == 1:
                valid_moves.append((row, col, game.en_passant[0], game.en_passant[1]))

        for possible_move in possible_moves:
            if board[possible_move[0]][possible_move[1]] == 0:
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
                if board[possible_move[0]][possible_move[1]] < 1:
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
        if not game.whiteCastled:
            if not game.whiteRook1_moved:
                c = col
                while True:
                    c -= 1

                    if not board[row][c] == 0:
                        break

                    if c == 1:
                        valid_moves.append((row, col, row, col-2))

            if not game.whiteRook2_moved:
                c = col
                while True:
                    c += 1

                    if not board[row][c] == 0:
                        break

                    if c == 6:
                        valid_moves.append((row, col, row, col + 2))

        for possible_move in possible_moves:
            if in_range(possible_move):
                if board[possible_move[0]][possible_move[1]] < 1:
                    # Add the possible move as a 4-tuple to the list of valid moves
                    valid_moves.append((row, col, possible_move[0], possible_move[1]))

    # Black pawn moves
    if piece == -1:
        # One step forward
        possible_moves = [(row + 1, col)]

        # Two steps forward
        if row == 1 and board[row + 1][col] == 0:
            possible_moves.append((row + 2, col))

        # Diagonal steps
        if in_range((row + 1, col - 1)):
            if board[row + 1][col - 1] > 0:
                valid_moves.append((row, col, row + 1, col - 1))
        if in_range((row + 1, col + 1)):
            if board[row + 1][col + 1] > 0:
                valid_moves.append((row, col, row + 1, col + 1))

        # En passant
        # If the en passant col is 1 step away from pawns col and the en passant row is 1 step below the pawns row
        if game.en_passant is not None:
            if abs(col - game.en_passant[1]) == 1 and row - game.en_passant[0] == -1:
                valid_moves.append((row, col, game.en_passant[0], game.en_passant[1]))

        for possible_move in possible_moves:
            if board[possible_move[0]][possible_move[1]] == 0:
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
                if board[possible_move[0]][possible_move[1]] > -1:
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
        if not game.blackCastled:
            if not game.blackRook1_moved:
                c = col
                while True:
                    c -= 1

                    if not board[row][c] == 0:
                        break

                    if c == 1:
                        valid_moves.append((row, col, row, col - 2))

            if not game.blackRook2_moved:
                c = col
                while True:
                    c += 1

                    if not board[row][c] == 0:
                        break

                    if c == 6:
                        valid_moves.append((row, col, row, col + 2))

        for possible_move in possible_moves:
            if in_range(possible_move):
                if board[possible_move[0]][possible_move[1]] > -1:
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


def loadImages():
    img_list = []
    pieceCodes = [1, 2, 3, 4, 5, 6, -1, -2, -3, -4, -5, -6]
    pieceNames = ['wP', 'wN', 'wB', 'wR', 'wQ', 'wK', 'bP', 'bN', 'bB', 'bR', 'bQ', 'bK']

    for name in pieceNames:
        img_list.append(pygame.image.load(f'images/{name}.png'))

    return dict(zip(pieceCodes, img_list))


class ChessGame:

    def __init__(self):
        self.board = newChessBoard()
        self.images = loadImages()
        self.dragger = Dragger()

        self.turn = WHITE

        self.whiteCastled = False
        self.blackCastled = False
        self.lastMove = None

        self.whiteRook1_moved = False
        self.whiteRook2_moved = False
        self.blackRook1_moved = False
        self.blackRook2_moved = False

        self.en_passant = None

    def swap_turn(self):
        self.turn = BLACK if self.turn == WHITE else WHITE

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
                if self.board[row][col] == 0:
                    continue
                if self.dragger.dragging:
                    if self.dragger.initial_col == col and self.dragger.initial_row == row:
                        continue
                piece = self.board[row][col]
                img_center = col * SQSIZE + SQSIZE // 2, row * SQSIZE + SQSIZE // 2
                texture_rect = self.images.get(piece).get_rect(center=img_center)
                surface.blit(self.images.get(piece), texture_rect)

    def show_moves(self, surface):
        if self.dragger.dragging:
            piece = self.dragger.piece

            moves = calculate_moves(self, piece, self.dragger.initial_row, self.dragger.initial_col)

            for move in moves:
                # color
                color = '#D6D6BD' if (move[2] + move[3]) % 2 == 0 else '#6A874D'

                # position of circle
                if self.board[move[2]][move[3]] == 0:
                    circle_pos = (move[3] * SQSIZE + SQSIZE // 2, move[2] * SQSIZE + SQSIZE // 2)
                    pygame.draw.circle(surface, color, circle_pos, 10)
                else:
                    circle_pos = (move[3] * SQSIZE + SQSIZE // 2, move[2] * SQSIZE + SQSIZE // 2)
                    pygame.draw.circle(surface, color, circle_pos, SQSIZE//2, width=4)

    def make_move(self, board, move, piece):
        board[move[0]][move[1]] = 0
        board[move[2]][move[3]] = piece

        # Promotion of pawns and en passant
        if piece == 1:
            if move[2] == 0:
                # If white pawn reaches the last row, promote it
                board[move[2]][move[3]] = 5

            # If the end square is the en passant square, do an en passant
            elif (move[2], move[3]) == self.en_passant:
                board[move[2] + 1][move[3]] = 0

        elif piece == -1:
            if move[2] == 7:
                # If black pawn reaches the last row, promote it
                board[move[2]][move[3]] = -5

            # If the end square is the en passant square, do an en passant
            elif (move[2], move[3]) == self.en_passant:
                board[move[2] - 1][move[3]] = 0

        # Castling
        elif abs(piece) == 6 and abs(move[1] - move[3]) == 2:
            # King side castling
            if move[3] == 2:
                board[move[0]][3] = board[move[0]][0]
                board[move[0]][0] = 0
                if piece == 6:
                    self.whiteCastled = True
                else:
                    self.blackCastled = True

            # Queen side castling
            if move[3] == 6:
                board[move[0]][5] = board[move[0]][7]
                board[move[0]][7] = 0
                if piece == 6:
                    self.whiteCastled = True
                else:
                    self.blackCastled = True

        # Castling privileges
        elif piece == 6:
            self.whiteCastled = True

        elif piece == -6:
            self.blackCastled = True

        elif piece == 4 and not self.whiteCastled:
            if (move[0], move[1]) == (7, 0):
                self.whiteRook1_moved = True
            elif (move[0], move[1]) == (7, 7):
                self.whiteRook2_moved = True

        elif piece == -4 and not self.blackCastled:
            if (move[0], move[1]) == (0, 0):
                self.blackRook1_moved = True
            elif (move[0], move[1]) == (0, 7):
                self.blackRook2_moved = True

        # Set and reset en passant square
        if piece == 1 and move[2] - move[0] == -2:
            # If pawn moved 2 steps, set en passant square equal to the skipped square
            self.en_passant = (move[2] + 1, move[3])

        elif piece == -1 and move[2] - move[0] == 2:
            # If pawn moved 2 steps, set en passant square equal to the skipped square
            self.en_passant = (move[2] - 1, move[3])

        else:
            self.en_passant = None

        self.lastMove = move
        self.swap_turn()

        return board
