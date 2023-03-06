from bitBoard.moves import *
from ctypes import c_ulonglong as U64


# Calculate king attacks in all eight directions
def kingAttacks(kings):
	attacks = eastOne(kings) | westOne(kings)
	kings |= attacks
	attacks |= nortOne(kings) | soutOne(kings)
	return attacks


# Array for initializing all possible king moves given a specific square, used for lookup
def kingAttackList():
	arrKingAttacks = []
	kingPos = U64(1).value
	for sq in range(64):
		arrKingAttacks.append(kingAttacks(kingPos))
		kingPos <<= 1

	return arrKingAttacks


def wKingMoves(wkings, wpieces):
	return kingAttacks(wkings) & ~wpieces


def bKingMoves(bkings, bpieces):
	return kingAttacks(bkings) & ~bpieces