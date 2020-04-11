from src.lib.constraints.pitch import *
from src.lib.types2 import *

def firstNoteIsTonic(line: Line) -> Constraint:
    return Constraint(isUnison(ConstPitch(0), line[0]), ConstraintType.BEGINNING, "First note should be the tonic")

def firstNoteAccompaniesCantusTonic(line: Line) -> Constraint:
    tonicIndex = ConstPitch(0)
    return Constraint(
        And(
            Implies(line[0] < tonicIndex, isOctave(line[0], tonicIndex)),
            Implies(line[0] > tonicIndex, Or(isOctave(tonicIndex, line[0]), isFifth(tonicIndex, line[0])))
        ),
        ConstraintType.BEGINNING,
        "First note should either be an octave above or below cantus tonic or a fifth above"
    )
    # Third case is that line[0] == tonicIndex
#
