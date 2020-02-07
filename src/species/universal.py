from z3 import *

from src.constraints import *

def universalRequirements(length, tonicIndex, gamutLength, opt, line):
    return And(pitchesWithinGamut(gamutLength, line),
               maximisesUniquePitchCount(gamutLength, opt, line),
               minimiseLeaps(opt, line),
               maximiseSteps(opt, line),
               conclusionSteps(line),
               hasClimaxPitch(tonicIndex, line),
               conclusionIsInTriad(tonicIndex, line)
               )
