from src.species.threeSimLines import *

def test_make_three_sim_lines():
    opt, line = defineThreeSimLines([Int("")], [Int("")], "name", 8)
    assert len(opt.assertions()) > len(Optimize().assertions()), "Means that the optimiser has some constraints"
    assert len(line) == 2
