from const import *


class ChessBoard:
	def __init__(self, board, turn, whiteCastled, blackCastled, lastMove, whiteRook1_moved, whiteRook2_moved,
				 blackRook1_moved, blackRook2_moved, en_passant):

		self.board = board

		self.turn = turn

		self.whiteCastled = whiteCastled
		self.blackCastled = blackCastled
		self.lastMove = lastMove

		self.whiteRook1_moved = whiteRook1_moved
		self.whiteRook2_moved = whiteRook2_moved
		self.blackRook1_moved = blackRook1_moved
		self.blackRook2_moved = blackRook2_moved

		self.en_passant = en_passant

	def __copy__(self):
		return ChessBoard(self.board, self.turn, self.whiteCastled, self.blackCastled, self.lastMove,
						  self.whiteRook1_moved, self.whiteRook2_moved, self.blackRook1_moved, self.blackRook2_moved,
						  self.en_passant)

	def swap_turn(self):
		self.turn = BLACK if self.turn == WHITE else WHITE

	def get(self, row, col):
		return self.board[row][col]

	def set(self, row, col, piece):
		self.board[row][col] = piece

	def swap(self, pos1, pos2):
		piece1 = self.get(pos1[0], pos1[1])
		self.set(pos1[0], pos1[1], self.get(pos2[0], pos2[1]))
		self.set(pos2[0], pos2[1], piece1)

	def move(self, move):
		piece = self.get(move[0], move[1])
		self.set(move[0], move[1], 0)
		self.set(move[2], move[3], piece)

		# Promotion of pawns and en passant
		if piece == 1:
			if move[2] == 0:
				# If white pawn reaches the last row, promote it
				self.set(move[2], move[3], 5)

			# If the end square is the en passant square, do an en passant
			elif (move[2], move[3]) == self.en_passant:
				self.set(move[2] + 1, move[3], 0)

		elif piece == -1:
			if move[2] == 7:
				# If black pawn reaches the last row, promote it
				self.set(move[2], move[3], -5)

			# If the end square is the en passant square, do an en passant
			elif (move[2], move[3]) == self.en_passant:
				self.set(move[2] - 1, move[3], 0)

		# Castling
		elif abs(piece) == 6 and abs(move[1] - move[3]) == 2:
			# King side castling
			if move[3] == 2:
				self.swap((move[0], 3), (move[0], 0))
				if piece == 6:
					self.whiteCastled = True
				else:
					self.blackCastled = True

			# Queen side castling
			if move[3] == 6:
				self.swap((move[0], 5), (move[0], 7))
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
