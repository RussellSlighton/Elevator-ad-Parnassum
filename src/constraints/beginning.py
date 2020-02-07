from src.constraints.pitch import *
from src.types import *

def firstNoteIsTonic(tonicIndex: TonicIndex, line: Line):
    return isUnison(tonicIndex, line[0])

def firstNoteAccompaniesCantusTonic(tonicIndex: TonicIndex, line: Line):
    return And(
        Implies(line[0] < tonicIndex, isOctave(line[0], tonicIndex)),
        Implies(line[0] > tonicIndex, Or(isOctave(tonicIndex, line[0]), isFifth(tonicIndex, line[0])))
    )
    # Third case is that line[0] == tonicIndex
