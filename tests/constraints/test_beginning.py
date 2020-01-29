import pytest

from src.constraints.beginning import *

@pytest.fixture
def s():
    return Solver()

@pytest.fixture
def l():
    return makeLine(2, "L")

def test_firstNoteMustBeTonic_allows_tonic(s, l):
    tonic = 1
    n1 = Int("L_0")
    s.add(n1 == tonic)
    s.add(firstNoteIsTonic(tonic, l))
    assert s.check() == sat

def test_firstNoteMustBeTonic_must_be_Tonic(s, l):
    tonic = 1
    n1 = Int("L_0")
    s.add(n1 != tonic)
    s.add(firstNoteIsTonic(tonic, l))
    assert s.check() == unsat

def test_firstNoteMustBeTonic_does_not_constrain_later_notes(s, l):
    tonic = 1000
    n1 = Int("L_1")
    s.add(n1 == tonic)
    s.add(firstNoteIsTonic(tonic, l))
    assert s.check() == sat
