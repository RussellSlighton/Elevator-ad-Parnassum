from itertools import chain, combinations
from typing import List

from z3 import Optimize, sat

from src.checker import checkCF, CheckerResult
from src.checker.checker import checkS1
from src.lib import Spec, Foundry, cantusSpec, ConstPitch, Constraint, ConstraintType, Pitch, firstSpeciesSpec, \
    secondSpeciesSpec, thirdSpeciesSpec, maxLetter, SimMap, Interval, makeTemporalisedLine, NoteLength, makeSimMap

#TODO: Make this use minimise differences!
def bruteForceRepairLine(broken : List[Pitch], spec : Spec) -> List[int]:
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

def smartRepairLine(broken : List[Pitch], spec : Spec, reasons : CheckerResult, gamutMax, sm : SimMap) -> List[int]:
    reasonsStrings = [x.split(":")[0].split('.')[1] for x in reasons.reasons]
    reasonsEnums = [ConstraintType[x] for x in reasonsStrings]
    print(reasonsEnums)

    fixedIndicies = list(range(0, len(broken)))

    if ConstraintType.BEGINNING in reasonsEnums:
        if 0 in fixedIndicies:
            fixedIndicies.remove(0)

    if ConstraintType.CONCLUSION in reasonsEnums:

        if len(broken) - 1 in fixedIndicies:
            fixedIndicies.remove(len(broken) - 1)
        # for when second last note does not step
        if len(broken) - 2 in fixedIndicies:
            fixedIndicies.remove(len(broken) - 2)

    if ConstraintType.CLIMAX in reasonsEnums:
        climax = max([x.flattened() for x in broken])
        for i in range(0, len(broken)):
            if broken[i].flattened() == climax:
                if i in fixedIndicies:
                    fixedIndicies.remove(i)

    if ConstraintType.PITCH in reasonsEnums or ConstraintType.GAMUT in reasonsEnums:
        for i in range(0, len(broken)):
            if maxLetter <= broken[i].letter < 0 or broken[i].flattened() >= gamutMax or \
                    Interval(broken[i].letter) not in \
                    [Interval.UNISON(), Interval.SECOND(),
                     Interval.THIRD(), Interval.FOURTH(),
                     Interval.FIFTH(), Interval.SIXTH(),
                     Interval.SEVENTH(), Interval.OCTAVE()]:
                if i in fixedIndicies:
                    fixedIndicies.remove(i)

    if ConstraintType.SIMULTANEITY in reasonsEnums:
        for i in range(0, len(broken)):
            simPitches = sm[broken[i]]
            upperPitch = broken[i].flattened()
            for p in simPitches:
                lowerPitch = p.flattened()
                if(Interval(abs(upperPitch - lowerPitch))) not in \
                        [Interval.THIRD(),
                         Interval.FIFTH(), Interval.OCTAVE()]:
                    # Recall that unison is illegal, hence we leave it out
                    if i in fixedIndicies:
                        fixedIndicies.remove(i)

    # We skip motion constraints. These tend to be optimizations and hence do not ever appear

    foundry = Foundry(Optimize())
    foundry.applySpec(spec)
    for i in fixedIndicies:
        foundry.apply(Constraint(spec.line[i] == broken[i], ConstraintType.REPAIRER, "Ignore"))
    if foundry.check() == sat:
        return foundry.extractPitches(spec.line)
    else:
        return None

def repairLine(broken : List[Pitch], spec : Spec, reasons : CheckerResult, gamutMax, sm) -> List[int]:
    smart = smartRepairLine(broken, spec, reasons, gamutMax, sm)
    print("trying smart")
    if smart is not None:
        print("smart worked!")
        return smart
    else:
        print("smart failed")
        print("trying brute force")
        return bruteForceRepairLine(broken,spec)


def repairCF(cf: List[int], gamutMax):
    reasons = checkCF(cf)
    length = len(cf)
    cf = [ConstPitch(x) for x in cf]
    tCF = makeTemporalisedLine(cf, NoteLength.WHOLE)
    sm = makeSimMap([tCF],tCF)
    return repairLine(cf, cantusSpec(length, gamutMax, ''), reasons, gamutMax, sm)

def repairS1(cf: List[int], s1: List[int], gamutMax):
    reasons = checkS1(cf, s1)
    cf = [ConstPitch(x) for x in cf]
    s1 = [ConstPitch(x) for x in s1]
    tCF = makeTemporalisedLine(cf, NoteLength.WHOLE)
    tS1 = makeTemporalisedLine(s1, NoteLength.WHOLE)
    sm = makeSimMap([tCF],tS1)
    return repairLine(s1, firstSpeciesSpec(cf, gamutMax, ''), reasons, gamutMax,sm)

def repairS2(cf: List[int], s2: List[int], gamutMax):
    reasons = checkS1(cf, s2)
    cf = [ConstPitch(x) for x in cf]
    s2 = [ConstPitch(x) for x in s2]
    tCF = makeTemporalisedLine(cf, NoteLength.WHOLE)
    tS2 = makeTemporalisedLine(s2, NoteLength.HALF)
    sm = makeSimMap([tCF],tS2)
    return repairLine(s2, secondSpeciesSpec(cf, gamutMax, ''), reasons, gamutMax, sm)

def repairS3(cf: List[int], s3: List[int], gamutMax):
    reasons = checkS1(cf, s3)
    cf = [ConstPitch(x) for x in cf]
    s3 = [ConstPitch(x) for x in s3]
    tCF = makeTemporalisedLine(cf, NoteLength.WHOLE)
    tS3 = makeTemporalisedLine(s3, NoteLength.QUARTER)
    sm = makeSimMap([tCF],tS3)
    return repairLine(s3, thirdSpeciesSpec(cf, gamutMax, ''), reasons, gamutMax, sm)

# reverse of more-itertools powerset
def revpowset(iterable):
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s),-1,-1))