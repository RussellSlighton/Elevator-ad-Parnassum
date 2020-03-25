from z3 import *

from src.species import *
from src.types import *

# TODO: This helper function is used in repair/repair - this func needs to be moved!
def extractVoice(opt: Optimize, line: Line):
    if opt.check() != sat:
        raise Exception("Species or CF not satisfiable")
    return [opt.model()[p.degree].as_long() + 7 * opt.model()[p.octave].as_long() for p in line]

def createCantusFirmus(length, tonic, gamutLength):
    if gamutLength - tonic < 3:
        raise Exception("Invalid gamut length - gamut must allow for a third to generate a cantus firmus")
    opt, line = defineCantusFirmus(length, "", tonic, gamutLength)
    return extractVoice(opt, line)

def createFirstSpecies(length, tonic, gamutLength):
    cf = createCantusFirmus(length, tonic, gamutLength)
    return cf
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

def createThroughSecond(length, tonic, gamutLength):
    primitiveLines = createFirstSpecies(length, tonic, gamutLength)
    cf = primitiveLines[0]
    s1 = primitiveLines[1]
    opt, line = defineThreeSimLines(cf, s1, "", gamutLength)

    s2 = extractVoice(opt, line)
    return [cf, s1, s2]

def createThroughThird(length, tonic, gamutLength):
    primitiveLines = createThroughSecond(length, tonic, gamutLength)
    cf = primitiveLines[0]
    s1 = primitiveLines[1]
    s2 = primitiveLines[2]
    opt, line = defineFourSimLines(cf, s1, s2, "", gamutLength)

    s3 = extractVoice(opt, line)
    return [cf, s1, s2, s3]
