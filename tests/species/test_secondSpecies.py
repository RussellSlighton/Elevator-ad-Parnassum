from src.species.secondSpecies import *

def test_make_first_species():
    cf = [1, 2, 3, 4, 5]
    opt, line = defineSecondSpecies(cf, "name", 8)
    assert len(opt.assertions()) > len(Optimize().assertions()), "Means that the optimiser has some constraints"
    assert len(line) == 10
