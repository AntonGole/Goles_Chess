import random
import copy
from const import *
from chessGame import calculate_legal_moves
from random import choice


class ChessEngine:
	def __init__(self, mode):
		self.mode = mode

	# Function that when called makes a move
	def move(self, chessBoard, color):
		# In this mode all moves made by the engine are random
		if self.mode == RANDOM:
			moves = calculate_legal_moves(chessBoard, color)

			random_move = random.choice(moves)
			chessBoard.move(random_move)

	def count_possible_moves(self, chessBoard, color, depth):
		"""
		Recursive function that returns the amount of possible games at a certain depth
		"""

		if depth == 0:
			return 1

		total_moves = 0

		if color == WHITE:
			new_moves = calculate_legal_moves(chessBoard, color)
			if not len(new_moves) == 0:
				for move in new_moves:
					new_board = copy.deepcopy(chessBoard)
					new_board.move(move)
					total_moves += self.count_possible_moves(new_board, BLACK, depth - 1)
		else:
			new_moves = calculate_legal_moves(chessBoard, color)
			if not len(new_moves) == 0:
				for move in new_moves:
					new_board = copy.deepcopy(chessBoard)
					new_board.move(move)
					total_moves += self.count_possible_moves(new_board, WHITE, depth - 1)

		return total_moves
