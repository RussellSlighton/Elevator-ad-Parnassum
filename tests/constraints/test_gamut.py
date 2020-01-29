import pytest

from src.constraints.gamut import *

@pytest.fixture
def l():
    return makeLine(4, 'l')

@pytest.fixture
def s():
    return Optimize()

def test_gamut_bound_pitch_is_satisfiable(l, s):
    s.add(pitchesWithinGamut(15, l))
    assert s.check() == sat

def test_gamut_bounds_pitch_limits_pitches(l, s):
    s.add(pitchesWithinGamut(0, l))
    assert s.check() == unsat

def test_maximisesUniquePitchCount_uses_as_much_of_gamut_as_possible(s, l):
    s.add(maximisesUniquePitchCount(5, s, l))
    assert s.check() == sat, "Optimiser should still be sat if whole gamut cannot be filled"

    foundPitches = []
    for p in l:
        foundPitches.append(s.model()[p].as_long())
    # Now we check if all notes are distinct
    s2 = Solver()
    s2.add(Distinct([Int(str(i)) for i in foundPitches]))
    assert s2.check() == sat, "All pitches should be unique because the gamut is longer than the line"
