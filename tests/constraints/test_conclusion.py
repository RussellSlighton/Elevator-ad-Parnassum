import pytest

from src.constraints.conclusion import *

@pytest.fixture
def s():
    return Solver()

@pytest.fixture
def l():
    return makeLine(2, "L")

def test_conclusion_is_tonic(s, l):
    tonic = 1
    n0 = Int("L_0")
    n1 = Int("L_1")
    s.add(n1 == tonic + 1)
    s.add(conclusionIsTonic(tonic, l))
    assert s.check() == unsat

def test_conclusion_is_tonic_leaves_other_notes_alone(s, l):
    tonic = 1
    n0 = Int("L_0")
    n1 = Int("L_1")
    s.add(n0 == tonic + 1)
    s.add(conclusionIsTonic(tonic, l))
    assert s.check() == sat

def test_conclusion_is_tonic_or_octave_leaves_other_notes_alone(s, l):
    tonic = 1
    n0 = Int("L_0")
    n1 = Int("L_1")
    s.add(n0 == tonic + 1)
    s.add(conclusionIsTonicOrOctave(tonic, l))
    assert s.check() == sat

def test_conclusion_is_tonic_or_octave(s, l):
    tonic = 1
    n0 = Int("L_0")
    n1 = Int("L_1")
    s.add(n1 != tonic)
    s.add(n1 != tonic + Interval.OCTAVE)
    s.add(conclusionIsTonicOrOctave(tonic, l))
    assert s.check() == unsat

def test_conclusion_is_tonic_or_octave_tonic_disallowed(s, l):
    tonic = 1
    n0 = Int("L_0")
    n1 = Int("L_1")
    s.add(n1 != tonic)
    s.add(conclusionIsTonicOrOctave(tonic, l))
    assert s.check() == sat

def test_conclusion_is_tonic_or_octave_octave_disallowed(s, l):
    tonic = 1
    n0 = Int("L_0")
    n1 = Int("L_1")
    s.add(n1 != tonic + Interval.OCTAVE)
    s.add(conclusionIsTonicOrOctave(tonic, l))
    assert s.check() == sat

def test_conclusion_steps_unison_not_allowed(s, l):
    n0 = Int("L_0")
    n1 = Int("L_1")
    s.add(n1 == n0)
    s.add(conclusionSteps(l))
    assert s.check() == unsat

def test_conclusion_steps_leap_not_allowed(s, l):
    n0 = Int("L_0")
    n1 = Int("L_1")
    s.add(n1 == n0 + 3)
    s.add(conclusionSteps(l))
    assert s.check() == unsat

def test_conclusion_steps_down_allowed(s, l):
    n0 = Int("L_0")
    n1 = Int("L_1")
    s.add(n1 == n0 - 1)
    s.add(conclusionSteps(l))
    assert s.check() == sat

def test_conclusion_steps_up_allowed(s, l):
    n0 = Int("L_0")
    n1 = Int("L_1")
    s.add(n1 == n0 + 1)
    s.add(conclusionSteps(l))
    assert s.check() == sat
