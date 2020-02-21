from typing import List

from src.constraints.beginning import *
from src.species.universal import *
from src.types import *

def defineThirdSpecies(cantusFirmus: List[int], name, gamutLength):
    tonicIndex = cantusFirmus[0]
    length = len(cantusFirmus) * 4

    # Really should be dep injected
    opt = Optimize()
    line = makeLine(length, "ThirdSpecies" + name)
    sm = makeSimMap([makeTemporalisedLine(cantusFirmus, NoteLength.WHOLE)], makeTemporalisedLine(line, NoteLength.QUARTER))

    constraints = And(
        universalRequirements(length, tonicIndex, gamutLength, opt, line),
        firstNoteAccompaniesCantusTonic(tonicIndex, line),
        unisonOnlyBeginningAndEnd(sm),
        unaccentedPassingNotesMayBeDissonant(sm),
        avoidsDissonance(opt, sm)
    )
    opt.add(constraints)
    return opt, line
