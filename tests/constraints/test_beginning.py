import pytest

from src.constraints.beginning import *

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
    tonic = 1
    s.add(firstNote == tonic)
    s.add(firstNoteIsTonic(tonic, l))
    assert s.check() == sat

def test_firstNoteMustBeTonic_must_be_Tonic(s, l, firstNote):
    tonic = 0
    s.add(firstNote.asInt() == 1)
    s.add(firstNoteIsTonic(tonic, l))
    assert s.check() == unsat

def test_firstNoteMustBeTonic_does_not_constrain_later_notes(s, l, firstNote):
    tonic = 1000
    s.add(firstNote == tonic)
    s.add(firstNoteIsTonic(tonic, l))
    assert s.check() == sat

def test_firstNoteAccompaniesCantusTonic_unison_is_legal(s, l, firstNote):
    tonic = 1
    s.add(firstNote == tonic)
    s.add(firstNoteAccompaniesCantusTonic(1, l))
    assert s.check() == sat

def test_firstNoteAccompaniesCantusTonic_higher_unsat_on_illegal(s, l, firstNote):
    tonic = 1
    s.add(firstNote == tonic + 10)
    s.add(firstNoteAccompaniesCantusTonic(1, l))
    assert s.check() == unsat
