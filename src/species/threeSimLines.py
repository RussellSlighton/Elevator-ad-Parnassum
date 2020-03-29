from src.constraints.beginning import *
from src.species.universal import *
from src.types import *

def defineThreeSimLines(cantusFirmus, firstSpecies, name, gamutLength):
    length = len(cantusFirmus) * 2

    # Really should be dep injected
    opt = Optimize()
    line = Line(length, "throughSecond" + name)
    sm = makeSimMap(
        [makeTemporalisedLine([ConstPitch(x) for x in cantusFirmus], NoteLength.WHOLE),
         makeTemporalisedLine([ConstPitch(x) for x in firstSpecies], NoteLength.WHOLE)],
        makeTemporalisedLine(line, NoteLength.HALF))

    constraints = And(
        universalRequirements(gamutLength, opt, line),
        firstNoteAccompaniesCantusTonic(line),
        unisonOnlyBeginningAndEnd(sm),
        noDissonantIntervals(sm),
    )
    opt.add(constraints)
    return opt, line
