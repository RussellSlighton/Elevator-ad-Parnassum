from src.species.cantusFirmus import *

def test_make_cantusFirmus():
    opt, line = defineCantusFirmus(2, "me", 2)
    assert len(opt.assertions()) > len(Optimize().assertions()), "Means that the optimiser has some constraints"
    assert len(line) == 2
