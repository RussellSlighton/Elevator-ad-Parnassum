from z3 import *

from src.constraints import *

def universalRequirements(gamutLength, opt, line):
    return And(pitchesWithinGamut(0, gamutLength, line).formula,
               pitchesOnScale(line).formula,
               #minimiseLeaps(opt, line),
               # maximiseSteps(opt, line),
               #uniquePitchCounts(0, gamutLength, line),
               conclusionSteps(line).formula,
               hasClimaxPitch(line).formula,
               conclusionIsInTriad(line).formula
               )
