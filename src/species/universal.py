from z3 import *

from src.constraints import *

def getUniversalRequirements(length, tonicIndex, gamutLength, opt, line):
    return And(pitchesWithinGamut(gamutLength, line),
               maximisesUniquePitchCount(gamutLength, opt, line),
               minimiseLeaps(opt, line),
               maximiseSteps(opt, line)
               )
