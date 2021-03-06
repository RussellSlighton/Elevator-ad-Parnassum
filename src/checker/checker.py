from typing import List

from z3 import *

from src.checker.checkerResults import CheckerResult
from src.lib.specs import *
from src.lib.types2 import Foundry, ConstPitch, Constraint, ConstraintType

def checkCF(cf: List[int]):
    cfPitches = [ConstPitch(x) for x in cf]
    spec = cantusSpec(len(cf), getGamutLength(cf), '')
    spec.minimisations = []
    spec.maximisations = []
    foundry = Foundry(Optimize())\
        .applyAndTrackSpec(spec)\
        .applyAll([Constraint(spec.line[i] == cfPitches[i], ConstraintType.CHECKER, "Ignore") for i in range(0, len(spec.line))])
    return CheckerResult(foundry.getReasonsForUnsat())

def checkS1(cf: List[int], s1 : List[int]):
    cfPitches = [ConstPitch(x) for x in cf]
    s1Pitches = [ConstPitch(x) for x in s1]
    spec = firstSpeciesSpec(cfPitches, getGamutLength(s1),'')
    spec.minimisations = []
    spec.maximisations = []
    foundry = Foundry(Optimize())\
        .applyAndTrackSpec(spec)\
        .applyAll([Constraint(spec.line[i] == s1Pitches[i], ConstraintType.CHECKER, "Ignore") for i in range(0, len(spec.line))])
    return CheckerResult(foundry.getReasonsForUnsat())

def checkS2(cf: List[int], s2 : List[int]):
    cfPitches = [ConstPitch(x) for x in cf]
    s2Pitches = [ConstPitch(x) for x in s2]
    spec = secondSpeciesSpec(cfPitches, getGamutLength(s2),'')
    spec.minimisations = []
    spec.maximisations = []
    foundry = Foundry(Optimize())\
        .applyAndTrackSpec(spec)\
        .applyAll([Constraint(spec.line[i] == s2Pitches[i], ConstraintType.CHECKER, "Ignore") for i in range(0, len(spec.line))])
    return CheckerResult(foundry.getReasonsForUnsat())

def checkS3(cf: List[int], s3 : List[int]):
    cfPitches = [ConstPitch(x) for x in cf]
    s3Pitches = [ConstPitch(x) for x in s3]
    spec = thirdSpeciesSpec(cfPitches, getGamutLength(s3),'')
    spec.minimisations = []
    spec.maximisations = []
    foundry = Foundry(Optimize())\
        .applyAndTrackSpec(spec)\
        .applyAll([Constraint(spec.line[i] == s3Pitches[i], ConstraintType.CHECKER, "Ignore") for i in range(0, len(spec.line))])
    return CheckerResult(foundry.getReasonsForUnsat())

def getGamutLength(line : List[int]):
    # +1 for max, recall that the gamutLength arg is non-inclusive
    return max(line) + 1