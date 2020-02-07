import pytest

from src.constraints.simultaneity import *

@pytest.fixture
def s():
    return Optimize()

@pytest.fixture
def l():
    return makeLine(5, "L")

@pytest.fixture
def cf():
    return [1, 2, 3, 2, 1]

@pytest.fixture
def sm(cf, l):
    return makeSimMap([makeTemporalisedLine(cf, NoteLength.WHOLE)], makeTemporalisedLine(l, NoteLength.WHOLE))

def test_onlyUnisonBeginningAndEnd_allows_unison_beginning_and_end(s, sm, l):
    s.add(unisonOnlyBeginningAndEnd(sm))
    s.add(l[0] == 1)
    s.add(l[-1] == 1)
    assert s.check() == sat

def test_onlyUnisonBeginningAndEnd_disallows_unison_in_middle(s, sm, l):
    s.add(unisonOnlyBeginningAndEnd(sm))
    s.add(l[1] == 2)
    assert s.check() == unsat

def test_noDissonantIntervals_legal_intervals_sat(s, sm, l):
    s.add(noDissonantIntervals(sm))
    s.add(l[0] == 3)
    assert s.check() == sat

def test_noDissonantIntervals_illegal_intervals_unsat(s, sm, l):
    s.add(noDissonantIntervals(sm))
    s.add(Or(l[0] == 2, l[0] == 7))
    assert s.check() == unsat

def test_minimiseFourths_fourths_minimised(s, sm, l, cf):
    s.add(avoidFourths(s, sm))
    s.check()
    for i in range(0, len(l)):
        pitch = s.model()[l[i]].as_long()
        assert not (pitch - cf[i] == Interval.FOURTH or cf[i] - pitch == Interval.FOURTH)
