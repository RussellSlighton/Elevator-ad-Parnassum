from z3 import *

from src.types2 import Pitch, ConstPitch, Line, Constraint, Interval, maxLetter, ConstraintType

# Note, only works upwards - C:G is a fifth, not a third.
def isNthInterval(n: Interval, n1: Pitch, n2: Pitch):
    return Interval.absBetween(n1, n2) == n

def isUnison(n1, n2):
    return isNthInterval(Interval.UNISON(), n1, n2)

def isSecond(n1, n2):
    return isNthInterval(Interval.SECOND(), n1, n2)

def isThird(n1, n2):
    return isNthInterval(Interval.THIRD(), n1, n2)

def isFourth(n1, n2):
    return isNthInterval(Interval.FOURTH(), n1, n2)

def isFifth(n1, n2):
    return isNthInterval(Interval.FIFTH(), n1, n2)

def isSixth(n1, n2):
    return isNthInterval(Interval.SIXTH(), n1, n2)

def isSeventh(n1, n2):
    return isNthInterval(Interval.SEVENTH(), n1, n2)

def isOctave(n1, n2):
    return isNthInterval(Interval.OCTAVE(), n1, n2)

def isDissonant(n1, n2):
    return Not(Or(isConsonant(n1, n2), isSixth(n1, n2)))

def isConsonant(n1, n2):
    return Or(isUnison(n1, n2), isThird(n1, n2), isFifth(n1, n2), isOctave(n1, n2))

# TODO: Must made this consonant mod octave!
def isTriadic(n1, n2, n3):
    tonicIndex = ConstPitch(0, 0)
    return And(isConsonant(tonicIndex, n1),
               isConsonant(tonicIndex, n2),
               isConsonant(tonicIndex, n3)
               )

# Calculation of interval between notes
# Degree:  1 2 3 4 5 6 7  1  2  3  4  5  6  7
# Base:    0 2 4 5 7 9 11 12 14 16 17 19 21 23
# Seconds:   2 2 1 2 2 2  1  2  2  1  2
# Thirds:      4 3 3 4 4  3  3  4  3  3
# Fourths:       5 5 5 6  5  5  5  5  5  5  6
# Fifths:          7 7 7  7  7  7  6  7  7  7

# This relationship happens to hold. Its certainly not intuitive though
def isStep(n1, n2):
    return Or(Interval.absBetween(n1, n2) == Interval(1), Interval.absBetween(n1, n2) == Interval(2))

# Technically not true (see above), but it is close enough
def isSkip(n1, n2):
    return And(Interval.absBetween(n1, n2) >= Interval(3), Interval.absBetween(n1, n2) <= Interval(6))

# Technically not true (see above), but it is close enough
def isLeap(n1, n2):
    return Interval.absBetween(n1, n2) >= Interval(7)

def isMotionUp(n1, n2):
    return n1 - n2 < 0

def isMotionDown(n1, n2):
    return n1 - n2 > 0

# Refers to interval, not distance.
# TODO: Z3 has a bug where int enum Interval is not automatically cast to int
#       We should be able to fix this..., but for now, just cast to int
def isIntervalOrLarger(n: Interval, n1, n2):
    return Interval.absBetween(n1, n2) >= n

def isIntervalOrSmaller(n: Interval, n1, n2):
    return Interval.absBetween(n1, n2) <= n

def pitchesLetterValueValid(line : Line) -> Constraint:
    return Constraint(And([And([IntVal(0) <= x.letter, x.letter < IntVal(maxLetter)]) for x in line]), ConstraintType.INVIOLABLE, "Should never be violated")