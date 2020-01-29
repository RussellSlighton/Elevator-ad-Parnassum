from enum import IntEnum

# Note, numbers correspond to distances between notes
class Interval(IntEnum):
    UNISON = 0
    SECOND = 1
    THIRD = 2
    FOURTH = 3
    FIFTH = 4
    SIXTH = 5
    SEVENTH = 6
    OCTAVE = 7
