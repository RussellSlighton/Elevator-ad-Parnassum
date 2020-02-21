from z3 import *

from src.species import *
from src.types import *

def extractVoice(opt: Optimize, line: Line):
    if opt.check() != sat:
        raise Exception("Species or CF not satisfiable")
    return [opt.model()[p].as_long() for p in line]

def createCantusFirmus(length, tonic, gamutLength):
    if gamutLength - tonic < 3:
        raise Exception("Invalid gamut length - gamut must allow for a third to generate a cantus firmus")
    opt, line = defineCantusFirmus(length, "", tonic, gamutLength)
    return extractVoice(opt, line)

def createFirstSpecies(length, tonic, gamutLength):
    cf = createCantusFirmus(length, tonic, gamutLength)
    opt, line = defineFirstSpecies(cf, "", gamutLength)
    return [cf, extractVoice(opt, line)]

def createSecondSpecies(length, tonic, gamutLength):
    cf = createCantusFirmus(length, tonic, gamutLength)
    opt, line = defineSecondSpecies(cf, "", gamutLength)
    return [cf, extractVoice(opt, line)]

def createThirdSpecies(length, tonic, gamutLength):
    cf = createCantusFirmus(length, tonic, gamutLength)
    opt, line = defineThirdSpecies(cf, "", gamutLength)
    return [cf, extractVoice(opt, line)]

def createThroughThird(length, tonic, gamutLength):
    cf = createCantusFirmus(length, tonic, gamutLength)

    opt, s1 = defineFirstSpecies(cf, "", gamutLength)
    s1 = extractVoice(opt, s1)

    opt, s1 = defineFirstSpecies(cf, "", gamutLength)
    s1 = extractVoice(opt, s1)