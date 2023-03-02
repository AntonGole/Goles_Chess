from ctypes import c_ulonglong as U64
from const import *


class Bitboard:
	def __init__(self, board):
		self.whitePawns = U64(0).value
		self.whiteKnights = U64(0).value
		self.whiteBishops = U64(0).value
		self.whiteRooks = U64(0).value
		self.whiteQueens = U64(0).value
		self.whiteKing = U64(0).value

		self.blackPawns = U64(0).value
		self.blackKnights = U64(0).value
		self.blackBishops = U64(0).value
		self.blackRooks = U64(0).value
		self.blackQueens = U64(0).value
		self.blackKing = U64(0).value

		for row in range(ROWS):
			for col in range(COLS):
				if board[row][col] == 1:
					self.whitePawns |= (U64(1).value << (col + (7 - row) * 8))  # White pawns
				elif board[row][col] == 2:
					self.whiteKnights |= (U64(1).value << (col + (7 - row) * 8))  # White knights
				elif board[row][col] == 3:
					self.whiteBishops |= (U64(1).value << (col + (7 - row) * 8))  # White bishops
				elif board[row][col] == 4:
					self.whiteRooks |= (U64(1).value << (col + (7 - row) * 8))  # White rooks
				elif board[row][col] == 5:
					self.whiteQueens |= (U64(1).value << (col + (7 - row) * 8))  # White queens
				elif board[row][col] == 6:
					self.whiteKing |= (U64(1).value << (col + (7 - row) * 8))  # White king
				elif board[row][col] == -1:
					self.blackPawns |= (U64(1).value << (col + (7 - row) * 8))  # Black pawns
				elif board[row][col] == -2:
					self.blackKnights |= (U64(1).value << (col + (7 - row) * 8))  # Black knights
				elif board[row][col] == -3:
					self.blackBishops |= (U64(1).value << (col + (7 - row) * 8))  # Black bishops
				elif board[row][col] == -4:
					self.blackRooks |= (U64(1).value << (col + (7 - row) * 8))  # Black rooks
				elif board[row][col] == -5:
					self.blackQueens |= (U64(1).value << (col + (7 - row) * 8))  # Black queens
				elif board[row][col] == -6:
					self.blackKing |= (U64(1).value << (col + (7 - row) * 8))  # Black king

		print(self.whitePawns)

	def move(self):
		pass

	def show(self):
		col_strings = []
		for row in range(ROWS):
			row_strings = []
			for col in range(COLS):
				if (self.whitePawns >> (col + row * 8)) & 1:
					row_strings.append(unicodes.get(WHITE_PAWN) + " ")
				elif (self.whiteKnights >> (col + row * 8)) & 1:
					row_strings.append(unicodes.get(WHITE_KNIGHT) + " ")
				elif (self.whiteBishops >> (col + row * 8)) & 1:
					row_strings.append(unicodes.get(WHITE_BISHOP) + " ")
				elif (self.whiteRooks >> (col + row * 8)) & 1:
					row_strings.append(unicodes.get(WHITE_ROOK) + " ")
				elif (self.whiteQueens >> (col + row * 8)) & 1:
					row_strings.append(unicodes.get(WHITE_QUEEN) + " ")
				elif (self.whiteKing >> (col + row * 8)) & 1:
					row_strings.append(unicodes.get(WHITE_KING) + " ")
				elif (self.blackPawns >> (col + row * 8)) & 1:
					row_strings.append(unicodes.get(BLACK_PAWN) + " ")
				elif (self.blackKnights >> (col + row * 8)) & 1:
					row_strings.append(unicodes.get(BLACK_KNIGHT) + " ")
				elif (self.blackBishops >> (col + row * 8)) & 1:
					row_strings.append(unicodes.get(BLACK_BISHOP) + " ")
				elif (self.blackRooks >> (col + row * 8)) & 1:
					row_strings.append(unicodes.get(BLACK_ROOK) + " ")
				elif (self.blackQueens >> (col + row * 8)) & 1:
					row_strings.append(unicodes.get(BLACK_QUEEN) + " ")
				elif (self.blackKing >> (col + row * 8)) & 1:
					row_strings.append(unicodes.get(BLACK_KING) + " ")
				else:
					if (row + col) % 2 == 0:
						row_strings.append(unicodes.get(BLACK_EMPTY) + "\u2006 ")
					else:
						row_strings.append(unicodes.get(WHITE_EMPTY) + "\u2006 ")
			col_strings.append(row_strings)

		for col in range(8):
			print("".join(col_strings[7-col]))
