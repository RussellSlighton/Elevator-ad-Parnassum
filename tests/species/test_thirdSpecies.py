from src.species.thirdSpecies import *

def test_make_second_species():
    cf = [1, 2, 3, 4, 5]
    opt, line = defineThirdSpecies(cf, "name", 8)
    assert len(opt.assertions()) > len(Optimize().assertions()), "Means that the optimiser has some constraints"
    assert len(line) == 20
