import pytest
from z3 import *

from src.constraints.motion import *
from src.types2 import *

@pytest.fixture
def l():
    return Line(4, 'l')

@pytest.fixture
def s():
    return Optimize()

def test_maximiseSteps_leaps_still_possible(s, l):
    count = sum([If(ind, 1, 0) for ind in steps(l)])
    s.maximize(count)
    s.add(l[0] == ConstPitch(0), l[1] == ConstPitch(10))
    assert s.check() == sat

def test_maximiseSteps_stepsByDefault(s, l):
    count = sum([If(ind, 1, 0) for ind in steps(l)])
    s.maximize(count)
    assert s.check() == sat
    ps = [s.model()[p.letter].as_long() + 12 * s.model()[p.octave].as_long() for p in l]
    print(ps)
    for i in range(0, len(l) - 1):
        assert abs(ps[i] - ps[i + 1]) <= 2

def test_minimiseLeaps_steps_still_possible(s, l):
    count = sum([If(ind, 1, 0) for ind in leaps(l)])
    s.minimize(count)
    s.add(l[0] == ConstPitch(0), l[1] == ConstPitch(1))
    assert s.check() == sat

def test_minimiseLeaps_skips_still_possible(s, l):
    count = sum([If(ind, 1, 0) for ind in leaps(l)])
    s.minimize(count)
    s.add(l[0] == ConstPitch(0), l[1] == ConstPitch(4))
    assert s.check() == sat

def test_minimiseSkips_steps_still_possible(s, l):
    count = sum([If(ind, 1, 0) for ind in steps(l)])
    s.minimize(count)
    s.add(l[0] == ConstPitch(0), l[1] == ConstPitch(1))
    assert s.check() == sat

def test_minimiseSkips_Leaps_still_possible(s, l):
    count = sum([If(ind, 1, 0) for ind in steps(l)])
    s.minimize(count)
    s.add(l[0] == ConstPitch(0), l[1] == ConstPitch(9))
    assert s.check() == sat
