from src.formulae.pitch import *
from src.types import *

def firstNoteIsTonic(line: Line):
    return isUnison(ConstPitch(0), line[0])

def firstNoteAccompaniesCantusTonic(line: Line):
    tonicIndex = ConstPitch(0)
    return And(
        Implies(line[0] < tonicIndex, isOctave(line[0], tonicIndex)),
        Implies(line[0] > tonicIndex, Or(isOctave(tonicIndex, line[0]), isFifth(tonicIndex, line[0])))
    )
    # Third case is that line[0] == tonicIndex
#
