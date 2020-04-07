import pytest

from src.constraints.motion import *

@pytest.fixture
def l():
    return Line(4, 'l')

@pytest.fixture
def s():
    return Optimize()

def test_maximiseSteps_leaps_still_possible(s, l):
    s.add(maximiseSteps(s, l))
    s.add(l[0] == ConstPitch(0), l[1] == ConstPitch(10))
    assert s.check() == sat

def test_maximiseSteps_stepsByDefault(s, l):
    s.add(maximiseSteps(s, l))
    assert s.check() == sat
    ps = [s.model()[p.letter].as_long() + 12 * s.model()[p.octave].as_long() for p in l]
    print(ps)
    for i in range(0, len(l) - 1):
        assert abs(ps[i] - ps[i + 1]) <= 2

def test_minimiseLeaps_steps_still_possible(s, l):
    s.add(minimiseLeaps(s, l))
    s.add(l[0] == ConstPitch(0), l[1] == ConstPitch(1))
    assert s.check() == sat

def test_minimiseLeaps_skips_still_possible(s, l):
    s.add(minimiseLeaps(s, l))
    s.add(l[0] == ConstPitch(0), l[1] == ConstPitch(4))
    assert s.check() == sat
