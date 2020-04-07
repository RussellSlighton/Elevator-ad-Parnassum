from src.constraints.beginning import *
from src.species.universal import *
from src.types import *

def defineFourSimLines(cantusFirmus, firstSpecies, secondSpecies, name, gamutLength):
    length = len(cantusFirmus) * 4

    # Really should be dep injected
    opt = Optimize()
    line = Line(length, "throughThird" + name)
    sm = makeSimMap(
        [makeTemporalisedLine(cantusFirmus, NoteLength.WHOLE), makeTemporalisedLine(firstSpecies, NoteLength.WHOLE),
         makeTemporalisedLine(secondSpecies, NoteLength.HALF)], makeTemporalisedLine(line, NoteLength.QUARTER))

    constraints = And(
        universalRequirements(gamutLength, opt, line),
        firstNoteAccompaniesCantusTonic(line).formula,
        unisonOnlyBeginningAndEnd(sm),
        noDissonantIntervals(sm),
        avoidsDissonance(opt, sm)
    )
    opt.add(constraints)
    return opt, line
