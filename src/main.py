from z3 import *

from src.species import *
from src.types import *

def extractVoice(opt: Optimize, line: Line):
    opt.check()
    return [opt.model()[p].as_long() for p in line]

def createCantusFirmus(length, tonic, gamutLength):
    opt, line = defineCantusFirmus(length, "", tonic, gamutLength)
    return extractVoice(opt, line)
