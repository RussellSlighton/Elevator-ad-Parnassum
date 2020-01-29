import pytest

from src.constraints.motion import *

@pytest.fixture
def l():
    return makeLine(4, 'l')

@pytest.fixture
def s():
    return Optimize()

def test_maximiseSteps_leaps_still_possible(s, l):
    s.add(maximiseSteps(s, l))
    s.add(l[0] == 0, l[1] == 10)
    assert s.check() == sat

def test_maximiseSteps_stepsByDefault(s, l):
    s.add(maximiseSteps(s, l))
    assert s.check() == sat
    ps = [s.model()[p].as_long() for p in l]
    for i in range(0, len(l) - 1):
        assert abs(ps[i] - ps[i + 1]) <= 1

def test_minimiseLeaps_steps_still_possible(s, l):
    s.add(minimiseLeaps(s, l))
    s.add(l[0] == 0, l[1] == 1)
    assert s.check() == sat

def test_minimiseLeaps_skips_still_possible(s, l):
    s.add(minimiseLeaps(s, l))
    s.add(l[0] == 0, l[1] == 3)
    assert s.check() == sat
