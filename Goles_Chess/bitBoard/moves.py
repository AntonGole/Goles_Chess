from bitBoard.bitmasks import *
from ctypes import c_ulonglong as U64


def soutOne(b):
	return b >> 8 & notRank8


def nortOne(b):
	return b << 8 & notRank1


def eastOne(b):
	return (b << 1) & notFileA


def noEaOne(b):
	return (b << 9) & notFileA & notRank1


def soEaOne(b):
	return (b >> 7) & notFileA & notRank8


def westOne(b):
	return (b >> 1) & notFileH


def soWeOne(b):
	return (b >> 9) & notFileH & notRank8


def noWeOne(b):
	return (b << 7) & notFileH & notRank1


def calculate_ray_attacks():
	ray_attacks = []

	for sq in range(64):


