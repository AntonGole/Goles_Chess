from bitBoard.bitmasks import *
from bitBoard.moves import *


# Pseudolegal attacks
def knightAttacks(knights):
	east = eastOne(knights)
	west = westOne(knights)
	attacks = (east | west) << 16
	attacks |= (east | west) >> 16
	east = eastOne(east)
	west = westOne(west)
	attacks |= (east | west) << 8
	attacks |= (east | west) >> 8
	return attacks


# White legal moves
def wKnightMoves(wknights, wpieces):
	return knightAttacks(wknights) & ~wpieces


# Black legal moves
def bKnightMoves(bknights, bpieces):
	return knightAttacks(bknights) & ~bpieces
