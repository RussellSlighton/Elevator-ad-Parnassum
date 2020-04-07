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
        firstNoteIsTonic(line).formula,
        conclusionIsTonic(line),
        hasClimaxPitch(line).formula,
        climaxMax(line, ConstPitch(int(gamutLength))).formula
    )
    opt.add(constraints)
    return opt, line
