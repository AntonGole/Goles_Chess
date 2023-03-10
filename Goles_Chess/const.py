from ctypes import c_ulonglong as U64

# Screen dimensions
WIDTH = 512
HEIGHT = 512

# Board dimensions
COLS = 8
ROWS = 8
SQSIZE = WIDTH // COLS

# Button codes
LEFT = 1
MIDDLE = 2
RIGHT = 3

# Engine modes
RANDOM = 10

# Player colors
WHITE = 0
BLACK = 1

# Pieces
WHITE_PAWN = 1
WHITE_KNIGHT = 2
WHITE_BISHOP = 3
WHITE_ROOK = 4
WHITE_QUEEN = 5
WHITE_KING = 6

BLACK_PAWN = -1
BLACK_KNIGHT = -2
BLACK_BISHOP = -3
BLACK_ROOK = -4
BLACK_QUEEN = -5
BLACK_KING = -6

WHITE_EMPTY = 7
BLACK_EMPTY = -7

# Piece unicodes
unicodes = {
	WHITE_PAWN: "\u265F",
	WHITE_KNIGHT: "\u265E",
	WHITE_BISHOP: "\u265D",
	WHITE_ROOK: "\u265C",
	WHITE_QUEEN: "\u265B",
	WHITE_KING: "\u265A",
	BLACK_PAWN: "\u2659",
	BLACK_KNIGHT: "\u2658",
	BLACK_BISHOP: "\u2657",
	BLACK_ROOK: "\u2656",
	BLACK_QUEEN: "\u2655",
	BLACK_KING: "\u2654",
	WHITE_EMPTY: "\u25FB",
	BLACK_EMPTY: "\u25FC",
}

move_infos = []
