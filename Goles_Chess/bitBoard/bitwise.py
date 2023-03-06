from ctypes import c_ulonglong as U64

# Series of useful bitwise operations while working with bitboards


# Returns the least significant 1-bit.
def get_LS1B(x):
	return x & -x


# Sets the least significant 1-bit to 0.
def reset_LS1B(x):
	return x & (x - 1)
