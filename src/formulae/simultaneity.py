from src.formulae._optimisationHelper import *
from src.formulae.pitch import *
from src.types import *

def unisonOnlyBeginningAndEnd(sm: SimMap):
    # Recall that dict perserves insertion order
    return And([Not(val == key) for key in sm for val in sm[key]][1:-1])

def noDissonantIntervals(sm: SimMap):
    return And([Not(isDissonant(key, val)) for key in sm for val in sm[key]])

def unaccentedPassingNotesMayBeDissonant(sm: SimMap, ):
    return And([Not(isDissonant(key, val)) for key in list(sm.keys())[::2] for val in sm[key]])

def avoidsFourths(opt, sm: SimMap):
    isFourthInds = [isFourth(val, key) for key in sm for val in sm[key]]
    minimise(opt, isFourthInds)
    return True

def avoidsDissonance(opt, sm: SimMap):
    isDis = [isDissonant(key, val) for key in sm for val in sm[key]]
    minimise(opt, isDis)
    return True
