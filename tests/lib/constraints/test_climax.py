import pytest

from src.lib.constraints.climax import *

@pytest.fixture
def s():
    return Solver()

@pytest.fixture
def l():
    return Line(10, "L")

def test_has_climax_pitch(s, l):
    s.add(hasClimaxPitch(l).formula)
    assert s.check() == sat
    ps = [s.model()[p.letter].as_long() + 7 * s.model()[p.octave].as_long() for p in l]
    climax = max(ps)
    ps.remove(climax)
    for x in ps:
        assert x < climax, "This is only true if climax was unique and the largest"

def test_climaxMax(s, l):
    s.add(hasClimaxPitch(l).formula)
    s.add(climaxMax(l, ConstPitch(3)).formula)
    assert s.check() == sat
    s.add(l[0] == ConstPitch(3))
    assert s.check() == unsat
