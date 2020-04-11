from itertools import chain, combinations
from typing import List
from sklearn.utils import shuffle

from z3 import Optimize, sat

from src.lib.constraints import pitchesLetterValueValid
from src.lib.types2 import Spec, Foundry

def getAllBadSpecs(spec : Spec, maxCount = None) -> List[Spec]:
    badSpecs = []
    constraintsToInclude = powset(spec.constraints)
    constraintsToInvert = constraintsToInclude[::-1]

    constraintsToInclude = constraintsToInclude[:-1]
    constraintsToInvert = constraintsToInvert[:-1]

    constraintsToInclude, constraintsToInvert = shuffle(constraintsToInclude, constraintsToInvert)

    if maxCount is None:
        maxCount = len(constraintsToInclude)
    else:
        maxCount = min(maxCount, len(constraintsToInclude))

    for i in range(maxCount):
        constraints = [pitchesLetterValueValid(spec.line)] # Needed ensure that the spec doesn't cheat on the gamut constraint
        constraints += constraintsToInclude[i]
        constraints += [x.inv() for x in constraintsToInvert[i]]
        badSpec = Spec(spec.line, constraints, spec.maximisations, spec.minimisations)
        foundry = Foundry(Optimize()).applySpec(badSpec)

        # We want to make sure inverting one doesn't render the bad spec invalid due to conflict with an overlapping constraint
        if foundry.check() == sat:
            badSpecs.append(badSpec)

    return badSpecs

def powset(s):
    return list([list(x) for x in chain.from_iterable(combinations(s, r) for r in range(0, len(s)+1))])