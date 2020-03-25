from typing import List

from src.constraints.beginning import *
from src.species.universal import *
from src.types import *

def defineSecondSpecies(cantusFirmus: List[int], name, gamutLength):
    tonicIndex = cantusFirmus[0]
    length = len(cantusFirmus) * 2

    # Really should be dep injected
    opt = Optimize()
    line = Line(length, "SecondSpecies" + name)
    sm = makeSimMap([makeTemporalisedLine(cantusFirmus, NoteLength.WHOLE)], makeTemporalisedLine(line, NoteLength.HALF))

    constraints = And(
        universalRequirements(length, tonicIndex, gamutLength, opt, line),
        firstNoteAccompaniesCantusTonic(tonicIndex, line),
        unisonOnlyBeginningAndEnd(sm),
        noDissonantIntervals(sm),
    )
    opt.add(constraints)
    return opt, line
