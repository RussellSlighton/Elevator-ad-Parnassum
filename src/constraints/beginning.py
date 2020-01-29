from src.constraints.pitch import *
from src.types import *

def firstNoteIsTonic(tonicIndex: TonicIndex, line: Line):
    return isUnison(tonicIndex, line[0])
