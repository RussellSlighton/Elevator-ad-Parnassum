from src.constraints.beginning import *
from src.species.universal import *
from src.types import *

def defineThreeSimLines(cantusFirmus, firstSpecies, name, gamutLength):
    length = len(cantusFirmus) * 2
    # Really should be dep injected
    opt = Optimize()
    line = Line(length, "throughSecond" + name)
    sm = makeSimMap(
        [makeTemporalisedLine(cantusFirmus, NoteLength.WHOLE),
         makeTemporalisedLine(firstSpecies, NoteLength.WHOLE)],
        makeTemporalisedLine(line, NoteLength.HALF))

    constraints = And(
        universalRequirements(gamutLength, opt, line),
        firstNoteAccompaniesCantusTonic(line).formula,
        unisonOnlyBeginningAndEnd(sm),
        noDissonantIntervals(sm),
    )
    opt.add(constraints)
    return opt, line
