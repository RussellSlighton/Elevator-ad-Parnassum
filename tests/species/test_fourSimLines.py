from src.species.fourSimLines import *

def test_make_four_sim_lines():
    opt, line = defineFourSimLines([Int("")], [Int("")], [Int(""), Int("")], "name", 8)
    assert len(opt.assertions()) > len(Optimize().assertions()), "Means that the optimiser has some constraints"
    assert len(line) == 4
