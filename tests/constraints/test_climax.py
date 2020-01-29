import pytest

from src.constraints.climax import *

@pytest.fixture
def s():
    return Solver()

@pytest.fixture
def l():
    return makeLine(10, "L")

def test_has_climax_pitch(s, l):
    s.add(hasClimaxPitch(1, l))
    assert s.check() == sat
    ps = [s.model()[p].as_long() for p in l]
    climax = max(ps)
    ps.remove(climax)
    for x in ps:
        assert x < climax, "This is only true if climax was unique and the largest"
