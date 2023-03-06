from bitmasks import *


def soutOne(b):
	return b >> 8


def nortOne(b):
	return b << 8


def eastOne(b):
	return (b << 1) & notFileA


def noEaOne(b):
	return (b << 9) & notFileA


def soEaOne(b):
	return (b >> 7) & notFileA


def westOne(b):
	return (b >> 1) & notFileH


def soWeOne(b):
	return (b >> 9) & notFileH


def noWeOne(b):
	return (b << 7) & notFileH
