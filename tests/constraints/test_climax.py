import pytest

from src.constraints.climax import *

@pytest.fixture
def s():
    return Solver()

@pytest.fixture
def l():
    return Line(10, "L")

def test_has_climax_pitch(s, l):
    s.add(hasClimaxPitch(1, l))
    assert s.check() == sat
    print(l[0].octave)
    ps = [s.model()[p.degree].as_long() + 7 * s.model()[p.octave].as_long() for p in l]
    climax = max(ps)
    ps.remove(climax)
    for x in ps:
        assert x < climax, "This is only true if climax was unique and the largest"
