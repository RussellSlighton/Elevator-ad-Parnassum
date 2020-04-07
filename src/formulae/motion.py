from src.formulae._optimisationHelper import *
from src.formulae.pitch import *
from src.types import *

def maximiseSteps(opt: Optimize, line: Line):
    stepInds = [isStep(line[i], line[i + 1]) for i in range(0, len(line) - 1)]
    maximise(opt, stepInds)
    return True

def minimiseLeaps(opt: Optimize, line: Line):
    leapInds = [isLeap(line[i], line[i + 1]) for i in range(0, len(line) - 1)]
    minimise(opt, leapInds)
    return True
