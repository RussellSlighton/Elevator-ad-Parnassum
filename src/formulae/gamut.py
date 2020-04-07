from z3 import *

from src.formulae._optimisationHelper import maximise
from src.types import *

def pitchesWithinGamut(gamutMin: int, gamutMax: int, line: Line):
    return And([And(ConstPitch(gamutMin) <= p, p < ConstPitch(gamutMax)) for p in line])

def pitchesOnScale(line: Line):
    return And([Or(p.letter == Interval.UNISON().semitoneDistance,
                   p.letter == Interval.SECOND().semitoneDistance,
                   p.letter == Interval.THIRD().semitoneDistance,
                   p.letter == Interval.FOURTH().semitoneDistance,
                   p.letter == Interval.FIFTH().semitoneDistance,
                   p.letter == Interval.SIXTH().semitoneDistance,
                   p.letter == Interval.SEVENTH().semitoneDistance,
                   ) for p in line])

def maximisesUniquePitchCount(gamutMin: int, gamutMax: int, opt: Optimize, line: Line):
    uniquePitchInds = [Or([p == ConstPitch(i) for p in line]) for i in
                       range(gamutMin, gamutMax)]
    maximise(opt, uniquePitchInds)
    return True
