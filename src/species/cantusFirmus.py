from z3 import *

from src.constraints import *
from src.species.universal import universalRequirements
from src.types import *

def defineCantusFirmus(length, name, gamutLength):
    # Really should be dep injected
    opt = Optimize()
    line = Line(length, "CF_" + name)

    constraints = And(
        universalRequirements(gamutLength, opt, line),
        firstNoteIsTonic(line),
        conclusionIsTonic(line),
        hasClimaxPitch(line),
        climaxMax(line, ConstPitch(int(gamutLength)))
    )
    opt.add(constraints)
    return opt, line
