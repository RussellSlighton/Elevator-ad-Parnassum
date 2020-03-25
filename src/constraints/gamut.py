from z3 import *

from src.constraints._optimisationHelper import maximise
from src.types import *

def pitchesWithinGamut(gamutLength: int, line: Line):
    return And([And(0 <= p, p < gamutLength) for p in line])

def maximisesUniquePitchCount(gamutLength: int, opt: Optimize, line: Line):
    uniquePitchInds = [Or([p == IntVal(i) for p in line]) for i in
                       range(0, gamutLength)]
    maximise(opt, uniquePitchInds)
    return True
