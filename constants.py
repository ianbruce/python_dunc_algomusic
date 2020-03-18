notes = [
    10465.0, # C
    11087.3, # C#
    11746.6, # D
    12445.1, # D#
    13185.1, # E
    13969.1, # F
    14799.8, # F#
    15679.8, # G
    16612.2, # G#
    17600.0, # A
    18646.0, # A#
    19755.0 # B
]

ROOT = 0
PER_2ND = 2
MIN_3RD = 3
MAJ_3RD = 4
PER_4TH = 5
DIM_5TH = 6
PER_5TH = 7
PER_6TH = 9
MIN_7TH = 10
MAJ_7th = 11
PER_12TH = 12

DEFAULT_PATH = "music/"


chord = [
    [MIN_3RD, PER_5TH, PER_12TH], # MINOR
    [MAJ_3RD, PER_5TH, PER_12TH], # MAJOR
    [MIN_3RD, DIM_5TH, PER_12TH], # DIMINISHED
    [PER_4TH, PER_5TH, PER_12TH], # SUSPENDED
    [MAJ_3RD, PER_5TH, MIN_7TH] # MINOR_7TH
]

