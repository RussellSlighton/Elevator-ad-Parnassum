import pytest

from src.formulae.gamut import *

@pytest.fixture
def l():
    return Line(4, 'l')

@pytest.fixture
def s():
    return Optimize()

def test_gamut_bound_pitch_is_satisfiable(l, s):
    s.add(pitchesWithinGamut(-15, 15, l))
    assert s.check() == sat

def test_gamut_bounds_pitch_limits_pitches(l, s):
    s.add(pitchesWithinGamut(0, 0, l))
    assert s.check() == unsat

def test_pitchesOnScaleAllowsOnScalePitches(l, s):
    s.add(pitchesOnScale(l))
    s.add((l[0] == ConstPitch(0)))
    assert s.check() == sat

def test_pitchesOnScaleNotAllowsOffScalePitches(l, s):
    s.add(pitchesOnScale(l))
    s.add((l[0] == ConstPitch(1)))
    assert s.check() == unsat

def test_maximisesUniquePitchCount_uses_as_much_of_gamut_as_possible(s, l):
    s.add(maximisesUniquePitchCount(-1, 3, s, l))
    assert s.check() == sat, "Optimiser should still be sat if whole gamut cannot be filled"

    foundPitches = [s.model()[p.letter].as_long() + 12 * s.model()[p.octave].as_long() for p in l]
    # Now we check if all notes are distinct
    s2 = Solver()
    s2.add(Distinct([Int(str(i)) for i in foundPitches]))
    assert s2.check() == sat, "All pitches should be unique because the gamut is longer than the line"
