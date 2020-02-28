from typing import List
from z3 import *
from src.species.cantusFirmus import defineCantusFirmus
from src.species.firstSpecies import defineFirstSpecies
from src.repair.util import cfSpec, s1Spec

def cfValid(cf : List[int]):
    opt, line = cfSpec(cf)
    for i in range(0, len(line)):
        opt.add(line[i] == cf[i])
    return opt.check() == sat

def s1Valid(cf : List[int], s1 : List[int]):
    opt, line = s1Spec(cf, s1)
    for i in range(0, len(line)):
        opt.add(line[i] == s1[i])
    return opt.check() == sat