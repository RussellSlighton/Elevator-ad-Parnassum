from src.species.threeSimLines import *

def test_make_three_sim_lines():
    opt, line = defineThreeSimLines([VarPitch("")], [VarPitch("")], "name", 8)
    assert len(opt.assertions()) > len(Optimize().assertions()), "Means that the optimiser has some formulae"
    assert len(line) == 2
