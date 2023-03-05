from ctypes import c_ulonglong as U64

# Series of useful bitwise operations while working with bitboards


# Isolates the least significant 1-bit. Used mostly for move generation
def LS1B(x):
	return x & -x
