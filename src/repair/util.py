from typing import List

from z3 import *

from src.species.cantusFirmus import defineCantusFirmus
from src.species.firstSpecies import defineFirstSpecies

def cfSpec(cf: List[int]) -> (Optimize, List[Int]):
    gamutLength = (max(cf) - min(cf)) + 2
    opt, line = defineCantusFirmus(len(cf), "cf", cf[0], gamutLength)  # +2 to count the max and min
    return opt, line

def s1Spec(cf: List[int], s1: List[int]) -> (Optimize, List[Int]):
    gamutLength = (max(cf + s1) - min(cf + s1)) + 2
    opt, line = defineFirstSpecies(cf, "s1", gamutLength)  # +2 to count the max and min
    return opt, line
