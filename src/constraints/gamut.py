from z3 import *
from src.types import *

def pitchesWithinGamut(gamutMin: int, gamutMax: int, line: Line) -> Constraint:
    formula = And([And(ConstPitch(gamutMin) <= p, p < ConstPitch(gamutMax)) for p in line])
    return Constraint(formula, ConstraintType.GAMUT, "Pitches must be between " + str(gamutMin) + " and " + str(gamutMin))

def pitchesOnScale(line: Line) -> Constraint:
    formula = And([Or(p.letter == Interval.UNISON().semitoneDistance,
                   p.letter == Interval.SECOND().semitoneDistance,
                   p.letter == Interval.THIRD().semitoneDistance,
                   p.letter == Interval.FOURTH().semitoneDistance,
                   p.letter == Interval.FIFTH().semitoneDistance,
                   p.letter == Interval.SIXTH().semitoneDistance,
                   p.letter == Interval.SEVENTH().semitoneDistance,
                   ) for p in line])
    return Constraint(formula, ConstraintType.GAMUT, "Pitches must be semitones on the scale")

def uniquePitchCounts(gamutMin: int, gamutMax: int, line: Line):
    return [Or([p == ConstPitch(i) for p in line]) for i in
                       range(gamutMin, gamutMax)]