import pytest

from src.formulae.beginning import *

@pytest.fixture
def s():
    return Solver()

@pytest.fixture
def l():
    return Line(2, "L")

@pytest.fixture
def firstNote(l):
    return l[0]

@pytest.fixture
def secondNote(l):
    return l[1]

def test_firstNoteMustBeTonic_allows_tonic(s, l, firstNote):
    tonic = ConstPitch(0, 0)
    s.add(firstNote == tonic)
    s.add(firstNoteIsTonic(l))
    assert s.check() == sat

def test_firstNoteMustBeTonic_must_be_Tonic(s, l, firstNote):
    tonic = ConstPitch(0, 0)
    s.add(firstNote == ConstPitch(1, 0))
    s.add(firstNoteIsTonic(l))
    assert s.check() == unsat

def test_firstNoteMustBeTonic_does_not_constrain_later_notes(s, l, secondNote):
    tonic = ConstPitch(1000)
    s.add(secondNote == tonic)
    s.add(firstNoteIsTonic(l))
    assert s.check() == sat

def test_firstNoteAccompaniesCantusTonic_unison_is_legal(s, l, firstNote):
    tonic = ConstPitch(0)
    s.add(firstNote == tonic)
    s.add(firstNoteAccompaniesCantusTonic(l))
    assert s.check() == sat

def test_firstNoteAccompaniesCantusTonic_higher_unsat_on_illegal(s, l, firstNote):
    s.add(firstNote == ConstPitch(11))
    s.add(firstNoteAccompaniesCantusTonic(l))
    assert s.check() == unsat
