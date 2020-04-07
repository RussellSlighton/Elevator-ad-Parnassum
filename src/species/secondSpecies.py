from typing import List

from src.constraints.beginning import *
from src.species.universal import *
from src.types import *

def defineSecondSpecies(cantusFirmus: List[int], name, gamutLength):
    length = len(cantusFirmus) * 2

    # Really should be dep injected
    opt = Optimize()
    line = Line(length, "SecondSpecies" + name)
    sm = makeSimMap([makeTemporalisedLine(cantusFirmus, NoteLength.WHOLE)], makeTemporalisedLine(line, NoteLength.HALF))

    constraints = And(
        universalRequirements(gamutLength, opt, line),
        firstNoteAccompaniesCantusTonic(line).formula,
        unisonOnlyBeginningAndEnd(sm).formula,
        noDissonantIntervals(sm).formula,
    )
    opt.add(constraints)
    return opt, line
