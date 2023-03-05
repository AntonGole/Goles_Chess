from ctypes import c_ulonglong as U64

# Bitmasks for bitboard representation

rank1 = U64(0).value = 0xff
rank2 = U64(0).value = 0xff00
rank3 = U64(0).value = 0xff0000
rank4 = U64(0).value = 0xff000000
rank5 = U64(0).value = 0xff00000000
rank6 = U64(0).value = 0xff0000000000
rank7 = U64(0).value = 0xff000000000000
rank8 = U64(0).value = 0xff00000000000000


fileA = U64(0).value = 0x101010101010101
fileB = U64(0).value = 0x202020202020202
fileC = U64(0).value = 0x404040404040404
fileD = U64(0).value = 0x808080808080808
fileE = U64(0).value = 0x1010101010101010
fileF = U64(0).value = 0x2020202020202020
fileG = U64(0).value = 0x4040404040404040
fileH = U64(0).value = 0x8080808080808080


notRank1 = U64(0).value = ~0xff
notRank2 = U64(0).value = ~0xff00
notRank3 = U64(0).value = ~0xff0000
notRank4 = U64(0).value = ~0xff000000
notRank5 = U64(0).value = ~0xff00000000
notRank6 = U64(0).value = ~0xff0000000000
notRank7 = U64(0).value = ~0xff000000000000
notRank8 = U64(0).value = ~0xff00000000000000


notFileA = U64(0).value = ~0x101010101010101
notFileB = U64(0).value = ~0x202020202020202
notFileC = U64(0).value = ~0x404040404040404
notFileD = U64(0).value = ~0x808080808080808
notFileE = U64(0).value = ~0x1010101010101010
notFileF = U64(0).value = ~0x2020202020202020
notFileG = U64(0).value = ~0x4040404040404040
notFileH = U64(0).value = ~0x8080808080808080

notFileAB = U64(0).value = (notFileA | notFileB)
notFileAF = U64(0).value = (notFileA | notFileF)
notFileGH = U64(0).value = (notFileG | notFileH)
