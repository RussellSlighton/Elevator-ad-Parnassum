from src.constraints.beginning import *
from src.species.universal import *
from src.types import *

def defineFirstSpecies(cantusFirmus: Line, name, gamutLength):
    tonicIndex = cantusFirmus[0]
    length = len(cantusFirmus)

    # Really should be dep injected
    opt = Optimize()
    line = Line(length, "FirstSpecies_" + name)
    sm = makeSimMap([makeTemporalisedLine(cantusFirmus, NoteLength.WHOLE)],
                    makeTemporalisedLine(line, NoteLength.WHOLE))

    constraints = And(
        universalRequirements(gamutLength, opt, line),
        firstNoteAccompaniesCantusTonic(line).formula,
        unisonOnlyBeginningAndEnd(sm).formula,
        noDissonantIntervals(sm).formula,
    )
    opt.add(constraints)
    return opt, line
