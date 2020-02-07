from z3 import *

from src.types.interval import Interval
from src.types.z3Utils import logicalAbs

# Note, only works upwards - C:G is a fifth, not a third.
def isNthInterval(n, n1, n2):
    return logicalAbs(n2 - n1) == int(n)

def isUnison(n1, n2):
    return isNthInterval(int(Interval.UNISON), n1, n2)

def isSecond(n1, n2):
    return isNthInterval(int(Interval.SECOND), n1, n2)

def isThird(n1, n2):
    return isNthInterval(int(Interval.THIRD), n1, n2)

def isFourth(n1, n2):
    return isNthInterval(int(Interval.FOURTH), n1, n2)

def isFifth(n1, n2):
    return isNthInterval(int(Interval.FIFTH), n1, n2)

def isSixth(n1, n2):
    return isNthInterval(int(Interval.SIXTH), n1, n2)

def isSeventh(n1, n2):
    return isNthInterval(int(Interval.SEVENTH), n1, n2)

def isOctave(n1, n2):
    return isNthInterval(int(Interval.OCTAVE), n1, n2)

def isDissonant(n1, n2):
    return Or(isSecond(n1, n2), isSeventh(n1, n2))

# TODO: Must made this consonant mod octave!
def isInTriad(n1, n2):
    return Or(isUnison(n1, n2), isThird(n1, n2), isFifth(n1, n2), isOctave(n1, n2))

# TODO: Must made this consonant mod octave!
def isTriadic(tonicIndex, n1, n2, n3):
    return And(isInTriad(tonicIndex, n1),
               isInTriad(tonicIndex, n2),
               isInTriad(tonicIndex, n3)
               )

# TODO: Add perfect and imperfect consonances

def isStep(n1, n2):
    return logicalAbs(n1 - n2) == int(Interval.SECOND)

def isSkip(n1, n2):
    return Or(logicalAbs(n1 - n2) == int(Interval.THIRD),
              logicalAbs(n1 - n2) == int(Interval.FOURTH)
              )

def isLeap(n1, n2):
    return logicalAbs(n1 - n2) >= int(Interval.FIFTH)

def isMotionUp(n1, n2):
    return n1 - n2 < 0

def isMotionDown(n1, n2):
    return n1 - n2 > 0

# Refers to interval, not distance.
# TODO: Z3 has a bug where int enum Interval is not automatically cast to int
#       We should be able to fix this..., but for now, just cast to int
def isIntervalOrLarger(n: Interval, n1, n2):
    return logicalAbs(n1 - n2) >= int(n)

def isIntervalOrSmaller(n: Interval, n1, n2):
    return logicalAbs(n1 - n2) <= int(n)
