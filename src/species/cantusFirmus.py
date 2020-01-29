from z3 import *

from src.constraints import *
from src.species.universal import getUniversalRequirements
from src.types import *

def defineCantusFirmus(length, name, tonicIndex, gamutLength):
    # Really should be dep injected
    opt = Optimize()
    line = makeLine(length, "CF_" + name)

    constraints = And(
        getUniversalRequirements(length, tonicIndex, gamutLength, opt, line),
        firstNoteIsTonic(tonicIndex, line),
        conclusionIsTonic(tonicIndex, line),
        conclusionSteps(line),
        hasClimaxPitch(tonicIndex, line),
    )
    opt.add(constraints)
    return opt, line
