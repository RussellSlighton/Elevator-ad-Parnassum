from z3 import *

from src.constraints import *

def universalRequirements(gamutLength, opt, line):
    return And(pitchesWithinGamut(0, gamutLength, line),
               pitchesOnScale(line),
               minimiseLeaps(opt, line),
               # maximiseSteps(opt, line),
               maximisesUniquePitchCount(0, gamutLength, opt, line),
               conclusionSteps(line),
               hasClimaxPitch(line),
               conclusionIsInTriad(line)
               )
