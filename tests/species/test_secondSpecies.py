from src.species.secondSpecies import *

def test_make_second_species():
    cf = [ConstPitch(x) for x in [1, 2, 3, 4, 5]]
    opt, line = defineSecondSpecies(cf, "name", 8)
    assert len(opt.assertions()) > len(Optimize().assertions()), "Means that the optimiser has some constraints"
    assert len(line) == 10
