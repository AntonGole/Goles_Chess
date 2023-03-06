from bitBoard.moves import *


# Pushes


# Single push white
def wSinglePushTargets(wpawns, empty):
	return nortOne(wpawns) & empty


# Double push white
def wDblPushTargets(wpawns, empty):
	singlePushes = wSinglePushTargets(wpawns, empty)
	return nortOne(wpawns) & empty


# Single push black
def bSinglePushTargets(bpawns, empty):
	return soutOne(bpawns) & empty


# Double push black
def bDblPushTargets(bpawns, empty):
	singlePushes = bSinglePushTargets(bpawns, empty)
	return nortOne(bpawns) & empty


# All pushes white
def wPawnPushes(wpawns, empty):
	return wSinglePushTargets(wpawns, empty) | wDblPushTargets(wpawns, empty)


# All pushes black
def bPawnPushes(bpawns, empty):
	return bSinglePushTargets(bpawns, empty) | bDblPushTargets(bpawns, empty)


# Attacks


# White pseudolegal attacks
def wPawnEastAttacks(wpawns):
	return noEaOne(wpawns)


def wPawnWestAttacks(wpawns):
	return noWeOne(wpawns)


def wPawnAnyAttacks(wpawns):
	return wPawnEastAttacks(wpawns) | wPawnWestAttacks(wpawns)


# Black pseudolegal moves
def bPawnEastAttacks(bpawns):
	return soEaOne(bpawns)


def bPawnWestAttacks(bpawns):
	return soWeOne(bpawns)


def bPawnAnyAttacks(bpawns):
	return bPawnEastAttacks(bpawns) | bPawnWestAttacks(bpawns)


# White legal attacks
def wPawnAttacks(wpawns, bpieces):
	return wPawnAnyAttacks(wpawns) & bpieces


# Black legal attacks
def bPawnAttacks(bpawns, wpieces):
	return bPawnAnyAttacks(bpawns) & wpieces


# White legal moves
def wPawnMoves(wpawns, bpieces, empty):
	return wPawnPushes(wpawns, empty) | wPawnAnyAttacks(wpawns) & bpieces


# Black legal moves
def bPawnMoves(bpawns, wpieces, empty):
	return bPawnPushes(bpawns, empty) | bPawnAnyAttacks(bpawns) & wpieces
