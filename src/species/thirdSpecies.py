from src.constraints.beginning import *
from src.species.universal import *
from src.types import *

def defineThirdSpecies(cantusFirmus: Line, name, gamutLength):
    length = len(cantusFirmus) * 4

    # Really should be dep injected
    opt = Optimize()
    line = Line(length, "ThirdSpecies" + name)
    sm = makeSimMap([makeTemporalisedLine(cantusFirmus, NoteLength.WHOLE)],
                    makeTemporalisedLine(line, NoteLength.QUARTER))

    constraints = And(
        universalRequirements(gamutLength, opt, line),
        firstNoteAccompaniesCantusTonic(line),
        unisonOnlyBeginningAndEnd(sm),
        noDissonantIntervals(sm),
        # unaccentedPassingNotesMayBeDissonant(sm),
        avoidsDissonance(opt, sm)
    )
    opt.add(constraints)
    return opt, line
