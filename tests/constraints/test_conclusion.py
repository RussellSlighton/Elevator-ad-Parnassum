import pytest

from src.constraints.conclusion import *

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
def lastNote(l):
    return l[1]


def test_conclusion_is_tonic(s, l, lastNote):
    tonic = 1
    s.add(lastNote == tonic + 1)
    s.add(conclusionIsTonic(tonic, l))
    assert s.check() == unsat

def test_conclusion_is_tonic_leaves_other_notes_alone(s, l, firstNote):
    tonic = 1
    s.add(firstNote == tonic + 1)
    s.add(conclusionIsTonic(tonic, l))
    assert s.check() == sat

def test_conclusion_is_tonic_or_octave_leaves_other_notes_alone(s, l, firstNote):
    tonic = 1
    s.add(firstNote == tonic + 1)
    s.add(conclusionIsTonicOrOctave(tonic, l))
    assert s.check() == sat

def test_conclusion_is_tonic_or_octave(s, l, lastNote):
    tonic = 1

    s.add(lastNote != tonic)
    s.add(lastNote != tonic + Interval.OCTAVE)
    s.add(lastNote != tonic - Interval.OCTAVE)

    s.add(conclusionIsTonicOrOctave(tonic, l))

    assert s.check() == unsat

def test_conclusion_is_tonic_or_octave_tonic_disallowed(s, l, lastNote ):
    tonic = 1
    s.add(lastNote != tonic)
    s.add(conclusionIsTonicOrOctave(tonic, l))
    assert s.check() == sat

def test_conclusion_is_tonic_or_octave_octave_disallowed(s, l, lastNote):
    tonic = 1
    s.add(lastNote != tonic + Interval.OCTAVE)
    s.add(conclusionIsTonicOrOctave(tonic, l))
    assert s.check() == sat

def test_conclusion_steps_unison_not_allowed(s, l, firstNote, lastNote):
    s.add(lastNote == firstNote)
    s.add(conclusionSteps(l))
    assert s.check() == unsat

def test_conclusion_steps_leap_not_allowed(s, l, firstNote, lastNote):
    s.add(lastNote == firstNote + 3)
    s.add(conclusionSteps(l))
    assert s.check() == unsat

def test_conclusion_steps_down_allowed(s, l, firstNote, lastNote):
    s.add(lastNote == firstNote - 1)
    s.add(conclusionSteps(l))
    assert s.check() == sat

def test_conclusion_steps_up_allowed(s, l, firstNote, lastNote):
    s.add(lastNote == firstNote + 1)
    s.add(conclusionSteps(l))
    assert s.check() == sat

def test_conclusionIsInTriad_works_onTriadics(s, l):
    s.add(conclusionIsInTriad(1, l))
    s.push()
    s.add(l[-1] == 1)
    assert s.check() == sat
    s.pop()
    s.push()
    s.add(l[-1] == 3)
    assert s.check() == sat
    s.pop()
    s.push()
    s.add(l[-1] == 5)
    assert s.check() == sat
    s.pop()
    s.push()
    s.add(l[-1] == 8)
    assert s.check() == sat
    s.pop()
    s.push()

def test_conclusionIsInTriad_fails_onNon_Triadics(s, l):
    s.add(conclusionIsInTriad(1, l))
    s.add()
    s.push()
    s.add(l[-1] == 2)
    assert s.check() == unsat
    s.pop()
    s.push()
    s.add(l[-1] == 0)
    assert s.check() == unsat
    s.pop()
    s.push()
    s.add(l[-1] == 6)
    assert s.check() == unsat
    s.pop()
    s.push()
    s.add(l[-1] == 7)
    assert s.check() == unsat
    s.pop()
    s.push()
