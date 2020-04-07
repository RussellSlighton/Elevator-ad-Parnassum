import pytest

from src.constraints.simultaneity import *

@pytest.fixture
def s():
    return Optimize()

@pytest.fixture
def l():
    return Line(5, "L")

@pytest.fixture
def cf():
    return [ConstPitch(x) for x in [0, 1, 2, 1, 0]]

@pytest.fixture
def sm(cf, l):
    return makeSimMap([makeTemporalisedLine(cf, NoteLength.WHOLE)], makeTemporalisedLine(l, NoteLength.WHOLE))

def test_onlyUnisonBeginningAndEnd_allows_unison_beginning_and_end(s, sm, l):
    s.add(unisonOnlyBeginningAndEnd(sm).formula)
    s.add(l[0] == ConstPitch(0))
    s.add(l[-1] == ConstPitch(0))
    assert s.check() == sat

def test_onlyUnisonBeginningAndEnd_disallows_unison_in_middle(s, sm, l):
    s.add(unisonOnlyBeginningAndEnd(sm).formula)
    s.add(l[1] == ConstPitch(1))
    assert s.check() == unsat

def test_noDissonantIntervals_legal_intervals_sat(s, sm, l):
    s.add(noDissonantIntervals(sm).formula)
    s.add(l[0] == ConstPitch(Interval.THIRD().semitoneDistance))
    assert s.check() == sat

def test_noDissonantIntervals_illegal_intervals_unsat(s, sm, l):
    s.add(noDissonantIntervals(sm).formula)
    s.add(Or(l[0] == ConstPitch(Interval.SECOND().semitoneDistance),
             l[0] == ConstPitch(Interval.SEVENTH().semitoneDistance)))
    assert s.check() == unsat

def test_minimiseFourths_fourths_minimised(s, sm, l, cf):
    count = sum([If(ind, 1, 0) for ind in fourths(sm)])
    s.minimize(count)
    s.check()
    for i in range(0, len(l)):
        pitch = s.model()[l[i].letter].as_long() + 12 * s.model()[l[i].octave].as_long()
        assert not (pitch - cf[i].letter == Interval.FOURTH().semitoneDistance or cf[
            i].letter - pitch == Interval.FOURTH().semitoneDistance)

def test_unaccentedPassingNotesDissonant_passingAllowsDissonant(s, sm, l, cf):
    s.add(l[1] == ConstPitch(cf[1].letter + 2))
    s.add(unaccentedPassingNotesMayBeDissonant(sm).formula)
    assert s.check() == sat

def test_unaccentedPassingNotesDissonant_passingAllowsConsonant(s, sm, l, cf):
    s.add(l[1] == ConstPitch(cf[1].letter + 4))
    s.add(unaccentedPassingNotesMayBeDissonant(sm).formula)
    assert s.check() == sat

def test_unaccentedPassingNotesDissonant_accentAllowsConsonant(s, sm, l, cf):
    s.add(l[2] == ConstPitch(cf[2].letter + 4))
    s.add(unaccentedPassingNotesMayBeDissonant(sm).formula)
    assert s.check() == sat

def test_minimiseDissonances_dissonances_minimised(s, sm, l, cf):
    count = sum([If(ind, 1, 0) for ind in dissonances(sm)])
    s.maximize(count)
    s.check()
    s2 = Solver()
    for i in range(0, len(l)):
        pitch = s.model()[l[i].letter].as_long() + 12 * s.model()[l[i].octave].as_long()
        s2.push()
        n1 = VarPitch("a")
        n2 = VarPitch("b")
        s2.add(n1 == ConstPitch(pitch))
        s2.add(n2 == ConstPitch(pitch))
        s2.add(isDissonant(n1, n2))
        assert s2.check() == unsat
        s2.pop()
