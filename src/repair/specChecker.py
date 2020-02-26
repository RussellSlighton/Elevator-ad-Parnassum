from typing import List
from z3 import *
from src.species.cantusFirmus import defineCantusFirmus
from src.species.firstSpecies import defineFirstSpecies
def cfValid(cf : List[int]):
    gamutLength = (max(cf) - min(cf))+2
    opt, line = defineCantusFirmus(len(cf), "cf", cf[0], gamutLength) # +2 to count the max and min
    for i in range(0, len(line)):
        opt.add(line[i] == cf[i])
    return opt.check() == sat

def s1Valid(cf : List[int], s1 : List[int]):
    gamutLength = (max(cf + s1) - min(cf + s1))+2
    opt, line = defineFirstSpecies(cf, "s1", gamutLength) # +2 to count the max and min
    for i in range(0, len(line)):
        opt.add(line[i] == s1[i])
    return opt.check() == sat