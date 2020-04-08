from src.constraints.pitch import *
from src.types2 import *

def unisonOnlyBeginningAndEnd(sm: SimMap) -> Constraint:
    # Recall that dict perserves insertion order
    return Constraint(
        And([Not(val == key) for key in sm for val in sm[key]][1:-1]),
        ConstraintType.SIMULTANEITY,
        "Only the first and last notes may be the same between lines"
    )

def noDissonantIntervals(sm: SimMap) -> Constraint:
    return Constraint(
        And([Not(isDissonant(key, val)) for key in sm for val in sm[key]]),
        ConstraintType.SIMULTANEITY,
        "Intervals should not be dissonant"
    )

def unaccentedPassingNotesMayBeDissonant(sm: SimMap) -> Constraint:
    return Constraint(
        And([Not(isDissonant(key, val)) for key in list(sm.keys())[::2] for val in sm[key]]),
        ConstraintType.SIMULTANEITY,
        "Only intervals between unaccented passing notes may be dissonant"
    )

def fourths(sm: SimMap):
    return [isFourth(val, key) for key in sm for val in sm[key]]

def dissonances(sm: SimMap):
    return [isDissonant(key, val) for key in sm for val in sm[key]]
