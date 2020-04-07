import pytest

from src.formulae.conclusion import *

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
    s.add(lastNote == ConstPitch(2))
    s.add(conclusionIsTonic(l))
    assert s.check() == unsat

def test_conclusion_is_tonic_leaves_other_notes_alone(s, l, firstNote):
    s.add(firstNote == ConstPitch(2))
    s.add(conclusionIsTonic(l))
    assert s.check() == sat

def test_conclusion_is_tonic_or_octave_leaves_other_notes_alone(s, l, firstNote):
    s.add(firstNote == ConstPitch(2))
    s.add(conclusionIsTonicOrOctave(l))
    assert s.check() == sat

def test_conclusion_is_tonic_or_octave(s, l, lastNote):
    s.add(lastNote != ConstPitch(0))
    s.add(lastNote != ConstPitch(12))
    s.add(lastNote != ConstPitch(-12))

    s.add(conclusionIsTonicOrOctave(l))

    assert s.check() == unsat

def test_conclusion_is_tonic_or_octave_tonic_disallowed(s, l, lastNote):
    tonic = ConstPitch(1)
    s.add(lastNote != tonic)
    s.add(conclusionIsTonicOrOctave(l))
    assert s.check() == sat

def test_conclusion_is_tonic_or_octave_octave_disallowed(s, l, lastNote):
    s.add(lastNote != ConstPitch(Interval.OCTAVE().semitoneDistance))
    s.add(conclusionIsTonicOrOctave(l))
    assert s.check() == sat

def test_conclusion_steps_unison_not_allowed(s, l, firstNote, lastNote):
    s.add(lastNote == firstNote)
    s.add(conclusionSteps(l))
    assert s.check() == unsat

def test_conclusion_steps_leap_not_allowed(s, l, firstNote, lastNote):
    s.add(lastNote == ConstPitch(0))
    s.add(firstNote == ConstPitch(100))
    s.add(conclusionSteps(l))
    assert s.check() == unsat

def test_conclusion_steps_down_allowed(s, l, firstNote, lastNote):
    s.add(lastNote.flattened() < firstNote.flattened())
    s.add(conclusionSteps(l))
    assert s.check() == sat

def test_conclusion_steps_up_allowed(s, l, firstNote, lastNote):
    s.add(lastNote.flattened() > firstNote.flattened())
    s.add(conclusionSteps(l))
    assert s.check() == sat

def test_conclusionIsInTriad_works_onTriadics(s, l):
    s.add(conclusionIsInTriad(l))
    s.push()
    s.add(l[-1] == ConstPitch(Interval.UNISON().semitoneDistance))
    assert s.check() == sat
    s.pop()
    s.push()
    s.add(l[-1] == ConstPitch(Interval.THIRD().semitoneDistance))
    assert s.check() == sat
    s.pop()
    s.push()
    s.add(l[-1] == ConstPitch(Interval.FIFTH().semitoneDistance))
    assert s.check() == sat
    s.pop()
    s.push()
    s.add(l[-1] == ConstPitch(Interval.OCTAVE().semitoneDistance))
    assert s.check() == sat
    s.pop()
    s.push()

def test_conclusionIsInTriad_fails_onNon_Triadics(s, l):
    s.add(conclusionIsInTriad(l))
    s.push()
    s.add(l[-1] == ConstPitch(Interval.SECOND().semitoneDistance))
    assert s.check() == unsat
    s.pop()
    s.push()
    s.add(l[-1] == ConstPitch(Interval.FOURTH().semitoneDistance))
    assert s.check() == unsat
    s.pop()
    s.push()
    s.add(l[-1] == ConstPitch(Interval.SIXTH().semitoneDistance))
    assert s.check() == unsat
    s.pop()
    s.push()
    s.add(l[-1] == ConstPitch(Interval.SEVENTH().semitoneDistance))
    assert s.check() == unsat
    s.pop()
    s.push()
