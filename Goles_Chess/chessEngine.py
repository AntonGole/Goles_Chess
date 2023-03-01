import random
import copy
from const import *
from chessGame import calculate_legal_moves, calculate_legal_moves_v2
import time
import tensorflow as tf


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

	def get_boards(self, chessBoard, color, depth):
		"""
		get_boards walks the move generation tree of strictly legal moves and returns all possible final positions at a
		certain depth It walks the move generation

		:param chessBoard: the starting chessboard to evaluate from
		:param color: which turn to start from
		:param depth: which depth that should be stopped at
		"""

		final_boards = []

		if depth == 0:
			return [chessBoard]

		if color == WHITE:
			new_moves = calculate_legal_moves_v2(chessBoard, color)
			if not len(new_moves) == 0:
				for move in new_moves:
					new_board = copy.deepcopy(chessBoard)
					new_board.move(move)
					final_boards = final_boards + (self.get_boards(new_board, BLACK, depth - 1))
			else:
				print(f"Check mate {color}, depth = {depth}")
				chessBoard.print_board()
				print("\n\n\n\n")
		else:
			new_moves = calculate_legal_moves_v2(chessBoard, color)
			if not len(new_moves) == 0:
				for move in new_moves:
					new_board = copy.deepcopy(chessBoard)
					new_board.move(move)
					final_boards = final_boards + (self.get_boards(new_board, WHITE, depth - 1))
			else:
				print(f"Check mate {color}, depth = {depth}")
				chessBoard.print_board()
				print("\n\n\n\n")

		return final_boards

	"""
	perft_v1 results:
	Depth = 1: 0.002758500 seconds 
	Depth = 2: 0.062936100 seconds 
	Depth = 3: 1.405115300 seconds 
	Depth = 4: 31.035829000 seconds 
	Depth = 5: 777.322510200 seconds 
	"""

	def perft_v1(self, chessBoard, color, depth):
		"""
		perft_v1 (performance test, move path enumeration) is used for debugging purposes. It walks the move generation
		tree of strictly legal moves to count all the leaf nodes of a certain depth.
		Version 1 makes use of the deepcopy() function to generate moves, and uses the class ChessBoard for representing
		the game

		:param chessBoard: the starting chessboard to evaluate from
		:param color: which turn to start from
		:param depth: which depth that should be stopped at
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
					total_moves += self.perft_v1(new_board, BLACK, depth - 1)
		else:
			new_moves = calculate_legal_moves(chessBoard, color)
			if not len(new_moves) == 0:
				for move in new_moves:
					new_board = copy.deepcopy(chessBoard)
					new_board.move(move)
					total_moves += self.perft_v1(new_board, WHITE, depth - 1)

		return total_moves

	"""
	perft_v2 results:
	Depth = 1: 0.001154700 seconds 
	Depth = 2: 0.022314300 seconds 
	Depth = 3: 0.517744100 seconds 
	Depth = 4: 11.208699800 seconds 
	Depth = 5: 292.794247400 seconds 
	"""
	def perft_v2(self, chessBoard, color, depth):
		"""
		perft_v2 (performance test, move path enumeration) is used for debugging purposes. It walks the move generation
		tree of strictly legal moves to count all the leaf nodes of a certain depth
		Version 2 makes use of move() and undo_move() to generate moves, and uses the class ChessBoard for representing
		the game

		:param chessBoard: the starting chessboard to evaluate from
		:param color: which turn to start from
		:param depth: which depth that should be stopped at
		"""

		if depth == 0:
			return 1

		total_moves = 0

		if color == WHITE:
			new_moves = calculate_legal_moves_v2(chessBoard, color)
			if not len(new_moves) == 0:
				for move in new_moves:
					move_infos.append(chessBoard.move(move))
					total_moves += self.perft_v2(chessBoard, BLACK, depth - 1)
					chessBoard.undo_move(move_infos.pop())
			else:
				print(f"Check mate {color}, depth = {depth}")
				chessBoard.print_board()
				print("\n\n\n\n")
		else:
			new_moves = calculate_legal_moves_v2(chessBoard, color)
			if not len(new_moves) == 0:
				for move in new_moves:
					move_infos.append(chessBoard.move(move))
					total_moves += self.perft_v2(chessBoard, WHITE, depth - 1)
					chessBoard.undo_move(move_infos.pop())
			else:
				print(f"Check mate {color}, depth = {depth}")
				chessBoard.print_board()
				print("\n\n\n\n")

		return total_moves


def time_function(function, *args):
	"""
	time_function times the given function and returns time taken for function to execute both in seconds and
	milliseconds

	:param function: the function to time
	:param args: the arguments for the function
	"""

	# Timestamp before function execution
	tic = time.perf_counter()
	function(*args)
	# Timestamp after function execution
	toc = time.perf_counter()

	seconds = toc - tic
	ms = seconds * 1000

	# Return execution time in seconds and milliseconds
	print(f"Function took {seconds:0.9f} seconds to execute ({ms:0.9f}ms)")

