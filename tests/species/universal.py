from src.species.universal import *
from src.types import *

def test_getUniversalRequirements():
    opt = Optimize()
    uni = getUniversalRequirements(2, 1, 2, opt, makeLine(2, "l"))
    assert len(uni.children()) > 0, "Means that the universal constraints aren't empty."
    assert len(str(opt)) > len(str(Optimize())), "Means some optimisation is going on in the background"
