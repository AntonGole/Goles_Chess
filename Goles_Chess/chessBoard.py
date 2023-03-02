from const import *
from copy import deepcopy


class ChessBoard:
	def __init__(self, board, turn, whiteCastled, blackCastled, whiteRook1_moved, whiteRook2_moved,
				 blackRook1_moved, blackRook2_moved, en_passant):

		self.board = board

		self.turn = turn

		self.whiteCastled = whiteCastled
		self.blackCastled = blackCastled

		self.whiteRook1_moved = whiteRook1_moved
		self.whiteRook2_moved = whiteRook2_moved
		self.blackRook1_moved = blackRook1_moved
		self.blackRook2_moved = blackRook2_moved

		self.en_passant = en_passant

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
		"""
		move makes a move using given 4-tuple

		:param move: a 4-tuple containing the following values: (start_row, start_col, end_row, end_col)
		"""
		piece = self.get(move[0], move[1])
		captured = self.get(move[2], move[3])
		self.set(move[0], move[1], 0)
		self.set(move[2], move[3], piece)

		move_info = [move, piece, captured, self.turn, self.whiteCastled, self.blackCastled, self.whiteRook1_moved,
					 self.whiteRook2_moved, self.blackRook1_moved, self.blackRook2_moved, self.en_passant]

		# Promotion of pawns and en passant
		if piece == WHITE_PAWN:
			if move[2] == 0:
				# If white pawn reaches the last row, promote it
				self.set(move[2], move[3], 5)

			# If the end square is the en passant square, do an en passant
			elif (move[2], move[3]) == self.en_passant:
				self.set(move[2] + 1, move[3], 0)

		elif piece == BLACK_PAWN:
			# If the end square is the en passant square, do an en passant
			if (move[2], move[3]) == self.en_passant:
				self.set(move[2] - 1, move[3], 0)

		# Castling
		elif abs(piece) == WHITE_KING and abs(move[1] - move[3]) == 2:
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
		elif piece == WHITE_KING:
			self.whiteCastled = True

		elif piece == BLACK_KING:
			self.blackCastled = True

		elif piece == WHITE_ROOK and not self.whiteCastled:
			if (move[0], move[1]) == (7, 0):
				self.whiteRook1_moved = True
			elif (move[0], move[1]) == (7, 7):
				self.whiteRook2_moved = True

		elif piece == BLACK_ROOK and not self.blackCastled:
			if (move[0], move[1]) == (0, 0):
				self.blackRook1_moved = True
			elif (move[0], move[1]) == (0, 7):
				self.blackRook2_moved = True

		# Set and reset en passant square
		if piece == WHITE_PAWN and move[2] - move[0] == -2:
			# If pawn moved 2 steps, set en passant square equal to the skipped square
			self.en_passant = (move[2] + 1, move[3])

		elif piece == BLACK_PAWN and move[2] - move[0] == 2:
			# If pawn moved 2 steps, set en passant square equal to the skipped square
			self.en_passant = (move[2] - 1, move[3])

		else:
			self.en_passant = None

		self.swap_turn()

		return move_info

	def print_board(self):
		"""
		print_board print the board in console with unicodes of pieces
		"""
		for row in range(ROWS):
			row_strings = []
			for col in range(COLS):
				if self.board[row][col] == 0:
					if (row + col) % 2 == 0:
						row_strings.append(unicodes.get(BLACK_EMPTY) + "\u2006 ")
					else:
						row_strings.append(unicodes.get(WHITE_EMPTY) + "\u2006 ")
				elif self.board[row][col] == WHITE_PAWN:
					row_strings.append(unicodes.get(WHITE_PAWN) + " ")
				elif self.board[row][col] == WHITE_KNIGHT:
					row_strings.append(unicodes.get(WHITE_KNIGHT) + " ")
				elif self.board[row][col] == WHITE_BISHOP:
					row_strings.append(unicodes.get(WHITE_BISHOP) + " ")
				elif self.board[row][col] == WHITE_ROOK:
					row_strings.append(unicodes.get(WHITE_ROOK) + " ")
				elif self.board[row][col] == WHITE_QUEEN:
					row_strings.append(unicodes.get(WHITE_QUEEN) + " ")
				elif self.board[row][col] == WHITE_KING:
					row_strings.append(unicodes.get(WHITE_KING) + " ")
				elif self.board[row][col] == BLACK_PAWN:
					row_strings.append(unicodes.get(BLACK_PAWN) + " ")
				elif self.board[row][col] == BLACK_KNIGHT:
					row_strings.append(unicodes.get(BLACK_KNIGHT) + " ")
				elif self.board[row][col] == BLACK_BISHOP:
					row_strings.append(unicodes.get(BLACK_BISHOP) + " ")
				elif self.board[row][col] == BLACK_ROOK:
					row_strings.append(unicodes.get(BLACK_ROOK) + " ")
				elif self.board[row][col] == BLACK_QUEEN:
					row_strings.append(unicodes.get(BLACK_QUEEN) + " ")
				elif self.board[row][col] == BLACK_KING:
					row_strings.append(unicodes.get(BLACK_KING) + " ")
			print("".join(row_strings))

	def undo_move(self, move_info):
		"""
		undo_move undoes the previous move

		:param move_info: an array containing information about the previous state variables before the move was made,
		as well as the move itself and the piece moved and piece captured (might be an emtpy square)
		"""
		self.set(move_info[0][0], move_info[0][1], move_info[1])
		self.set(move_info[0][2], move_info[0][3], move_info[2])

		# Promotion of pawns and en passant
		if move_info[1] == WHITE_PAWN:
			# If the end square is the en passant square, do an en passant
			if (move_info[0][2], move_info[0][3]) == move_info[10]:
				self.set(move_info[0][2] + 1, move_info[0][3], BLACK_PAWN)

		elif move_info[1] == BLACK_PAWN:
			# If the end square is the en passant square, do an en passant
			if (move_info[0][2], move_info[0][3]) == move_info[10]:
				self.set(move_info[0][2] - 1, move_info[0][3], WHITE_PAWN)

		# Castling
		elif abs(move_info[1]) == WHITE_KING and abs(move_info[0][1] - move_info[0][3]) == 2:
			# King side castling
			if move_info[0][3] == 2:
				self.swap((move_info[0][0], 3), (move_info[0][0], 0))
				if move_info[1] == 6:
					self.whiteCastled = True
				else:
					self.blackCastled = True

			# Queen side castling
			if move_info[0][3] == 6:
				self.swap((move_info[0][0], 5), (move_info[0][0], 7))
				if move_info[1] == 6:
					self.whiteCastled = True
				else:
					self.blackCastled = True

		self.turn = move_info[3]

		self.whiteCastled = move_info[4]
		self.blackCastled = move_info[5]

		self.whiteRook1_moved = move_info[6]
		self.whiteRook2_moved = move_info[7]
		self.blackRook1_moved = move_info[8]
		self.blackRook2_moved = move_info[9]

		self.en_passant = move_info[10]