import random

from const import *
from chessGame import calculate_moves
from random import choice


class ChessEngine:
	def __init__(self, mode):
		self.mode = mode

	# Function that when called makes a move
	def move(self, color, game, board):
		# In this mode all moves made by the engine are random
		if self.mode == RANDOM:
			moves = []
			if color == WHITE:
				for r, row in enumerate(board):
					for c, col in enumerate(row):
						if board[r][c] > 0:
							new_moves = calculate_moves(game, board[r][c], r, c)
							if not len(new_moves) == 0:
								for move in new_moves:
									moves.append(move)

				random_move = random.choice(moves)
				game.make_move(board, random_move, board[random_move[0]][random_move[1]])

			else:
				for r, row in enumerate(board):
					for c, col in enumerate(row):
						if board[r][c] < 0:
							new_moves = calculate_moves(game, board[r][c], r, c)
							if not len(new_moves) == 0:
								for move in new_moves:
									moves.append(move)

				random_move = random.choice(moves)
				game.make_move(board, random_move, board[random_move[0]][random_move[1]])
