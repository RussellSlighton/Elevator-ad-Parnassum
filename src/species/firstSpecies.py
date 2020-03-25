from typing import List

from src.constraints.beginning import *
from src.species.universal import *
from src.types import *

def defineFirstSpecies(cantusFirmus: List[int], name, gamutLength):
    tonicIndex = cantusFirmus[0]
    length = len(cantusFirmus)

    # Really should be dep injected
    opt = Optimize()
    line = Line(length, "FirstSpecies_" + name)
    sm = makeSimMap([makeTemporalisedLine(cantusFirmus, NoteLength.WHOLE)],
                    makeTemporalisedLine(line, NoteLength.WHOLE))

    constraints = And(
        universalRequirements(length, tonicIndex, gamutLength, opt, line),
        firstNoteAccompaniesCantusTonic(tonicIndex, line),
        unisonOnlyBeginningAndEnd(sm),
        noDissonantIntervals(sm),
        # avoidFourths(opt, sm)
    )
    opt.add(constraints)
    return opt, line
