from typing import List

from z3 import *

from src.checker.checkerResults import CheckerResult
from src.specs import cantusSpec, firstSpeciesSpec
from src.types2 import Foundry, ConstPitch, Constraint, ConstraintType

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


def getGamutLength(line : List[int]):
    # +1 for max, recall that the gamutLength arg is non-inclusive
    return max(line) + 1