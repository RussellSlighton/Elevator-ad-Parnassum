from itertools import chain, combinations
from typing import List

from z3 import Optimize, sat

from src.lib import Spec, Foundry, cantusSpec, ConstPitch, Constraint, ConstraintType, Pitch, firstSpeciesSpec,\
    secondSpeciesSpec, thirdSpeciesSpec

#TODO: Make this use minimise differences!
def __bruteForceRepairLine(broken : List[Pitch], spec : Spec) -> List[int]:
    foundry = Foundry(Optimize())
    foundry.applySpec(spec)
    for fixedNoteIndexes in revpowset(range(0, len(broken))):
        foundry.opt.push()
        for i in fixedNoteIndexes:
            foundry.apply(Constraint(spec.line[i] == broken[i], ConstraintType.REPAIRER, "Ignore"))
        if foundry.check() == sat:
            return foundry.extractPitches(spec.line)
        foundry.opt.pop()
    raise Exception("No valid line could be found")

def repairCF(cf: List[int], gamutMax):
    length = len(cf)
    cf = [ConstPitch(x) for x in cf]
    return __bruteForceRepairLine(cf, cantusSpec(length, gamutMax, ''))

def repairS1(cf: List[int], s1: List[int], gamutMax):
    cf = [ConstPitch(x) for x in cf]
    s1 = [ConstPitch(x) for x in s1]
    return __bruteForceRepairLine(s1, firstSpeciesSpec(cf, gamutMax, ''))

def repairS2(cf: List[int], s2: List[int], gamutMax):
    cf = [ConstPitch(x) for x in cf]
    s2 = [ConstPitch(x) for x in s2]
    return __bruteForceRepairLine(s2, secondSpeciesSpec(cf, gamutMax, ''))

def repairS3(cf: List[int], s3: List[int], gamutMax):
    cf = [ConstPitch(x) for x in cf]
    s3 = [ConstPitch(x) for x in s3]
    return __bruteForceRepairLine(s3, thirdSpeciesSpec(cf, gamutMax, ''))

# reverse of more-itertools powerset
def revpowset(iterable):
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s),-1,-1))