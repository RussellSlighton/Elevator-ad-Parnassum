from itertools import combinations, chain
from typing import List

from z3 import *

from src.main import extractVoice
from src.repair.util import cfSpec, s1Spec

# TODO: Make this use minimise differences!
def __repairLine(broken: List[int], spec: Optimize, repair: List[Int]) -> List[int]:
    for fixedNoteIndexes in revpowset(range(0, len(broken))):
        spec.push()
        for i in fixedNoteIndexes:
            spec.add(repair[i] == broken[i])
        if spec.check() == sat:
            return extractVoice(spec, repair)
        spec.pop()
    # Return none if no fix can be found

def repairCF(cf: List[int]) -> List[int]:
    opt, line = cfSpec(cf)
    return __repairLine(cf, opt, line)

# Note, does not guarantee the correctness of CF!
def repairS1(cf: List[int], s1: List[int]) -> (List[int], List[int]):
    opt, line = s1Spec(cf, s1)
    repaired = __repairLine(s1, opt, line)

    # CF is broken so s1 can't be fixed!
    if repaired is not None:
        return cf, repaired

    # fix CF
    opt, line = cfSpec(cf)
    newCF = __repairLine(cf, opt, line)

    # fix S1
    # note we do not call recursively because in the case of bugs the (not None) check might infinite loop.
    opt, line = s1Spec(newCF, s1)
    return newCF, __repairLine(s1, opt, line)

# reverse of more-itertools powerset
def revpowset(iterable):
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s), -1, -1))
