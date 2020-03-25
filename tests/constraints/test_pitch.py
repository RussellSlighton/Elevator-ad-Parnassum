import pytest

from src.constraints.pitch import *

def run2(function, arg1, arg2):
    s = Solver()
    s.add(Int("1") == arg1)
    s.add(Int("2") == arg2)
    s.add(function(arg1, arg2))
    return s

def run3(function, arg0, arg1, arg2):
    s = Solver()
    s.add(Int("1") == arg1)
    s.add(Int("2") == arg2)
    s.add(function(arg0, arg1, arg2))
    return s

def test_isNApart_negative():
    assert run3(isNthInterval, 1, -2, -1).check() == sat, "isNApart works on negatives"

def test_isNApart_positive():
    assert run3(isNthInterval, 1, 1, 2).check() == sat, "isNApart works on positives"

def test_is_unison():
    assert run2(isUnison, 0, 0).check() == sat
    assert run2(isUnison, 1, 1).check() == sat
    assert run2(isUnison, -1, -1).check() == sat
    assert run2(isUnison, 1, 2).check() == unsat

def test_is_second():
    assert run2(isSecond, 1, 2).check() == sat
    assert run2(isSecond, -2, -1).check() == sat
    assert run2(isSecond, 1, 1).check() == unsat

def test_is_third():
    assert run2(isThird, 1, 3).check() == sat
    assert run2(isThird, -3, -1).check() == sat
    assert run2(isThird, 1, 1).check() == unsat

def test_is_fourth():
    assert run2(isFourth, 1, 4).check() == sat
    assert run2(isFourth, -4, -1).check() == sat
    assert run2(isFourth, 1, 1).check() == unsat

def test_is_fifth():
    assert run2(isFifth, 1, 5).check() == sat
    assert run2(isFifth, -5, -1).check() == sat
    assert run2(isFifth, 1, 1).check() == unsat

def test_is_sixth():
    assert run2(isSixth, 1, 6).check() == sat
    assert run2(isSixth, -6, -1).check() == sat
    assert run2(isSixth, 1, 1).check() == unsat

def test_is_seventh():
    assert run2(isSeventh, 1, 7).check() == sat
    assert run2(isSeventh, -7, -1).check() == sat
    assert run2(isSeventh, 1, 1).check() == unsat

def test_is_octave():
    assert run2(isOctave, 1, 8).check() == sat
    assert run2(isOctave, -8, -1).check() == sat
    assert run2(isOctave, 1, 1).check() == unsat

# TODO: This really should be mocked
@pytest.fixture
def s():
    return Solver()

def consHelper(n1, n2, s):
    s.push()
    s.add(isInTriad(n1, n2))
    res = s.check()
    s.pop()
    return res

def test_is_consonant(s):
    assert consHelper(1, 1, s) == sat, "Unison is consonant"
    assert consHelper(1, 3, s) == sat, "Third is consonant"
    assert consHelper(1, 5, s) == sat, "Fifth is consonant"
    assert consHelper(1, 8, s) == sat, "Octave is consonant"
    assert consHelper(1, 6, s) == unsat, "Sixth is not consonant"

def triadicHelper(tonic, n1, n2, n3, s):
    s.push()
    s.add(isTriadic(tonic, n1, n2, n3))
    res = s.check()
    s.pop()
    return res

def test_is_triadic(s):
    assert triadicHelper(1, 1, 3, 5, s) == sat
    assert triadicHelper(1, 1, 3, 8, s) == sat
    assert triadicHelper(1, 1, 4, 8, s) == unsat

def stepHelper(n1, n2, s):
    s.push()
    s.add(isStep(n1, n2))
    res = s.check()
    s.pop()
    return res

def test_is_step(s):
    assert stepHelper(1, 2, s) == sat, "step works going up"
    assert stepHelper(2, 1, s) == sat, "step works going down"
    assert stepHelper(2, 8, s) == unsat, "leaps don't count as steps"

def leapHelper(n1, n2, s):
    s.push()
    s.add(isLeap(n1, n2))
    res = s.check()
    s.pop()
    return res

def test_is_leap(s):
    assert leapHelper(1, 5, s) == sat, "leap works going up"
    assert leapHelper(5, 1, s) == sat, "leap works going down"
    assert leapHelper(1, 4, s) == unsat, "skips don't count as leaps"

def skipHelper(n1, n2, s):
    s.push()
    s.add(isSkip(n1, n2))
    res = s.check()
    s.pop()
    return res

def test_is_skip(s):
    assert skipHelper(1, 3, s) == sat, "3 skip works going up"
    assert skipHelper(3, 1, s) == sat, "3 skip works going down"
    assert skipHelper(1, 4, s) == sat, "4 skip works going up"
    assert skipHelper(1, 4, s) == sat, "4 skip works going up"
    assert skipHelper(1, 5, s) == unsat, "leaps don't count as skips"
    assert skipHelper(1, 2, s) == unsat, "steps don't count as skips"

def test_isMotionUp():
    assert isMotionUp(1, 2)
    assert not isMotionUp(1, 1), "Unison is not motion"
    assert not isMotionUp(1, 0)

def test_isMotionDown():
    assert isMotionDown(2, 1)
    assert not isMotionDown(1, 1), "Unison is not motion"
    assert not isMotionDown(1, 2)

def largerHelper(n, n1, n2, s):
    s.push()
    s.add(isIntervalOrLarger(n, n1, n2))
    res = s.check()
    s.pop()
    return res

def test_is_interval_or_larger(s):
    assert largerHelper(Interval.THIRD, 1, 2, s) == unsat, "func should judge by interval, not distance"
    assert largerHelper(Interval.SECOND, 1, 2, s) == sat, "func should judge by interval"
    assert largerHelper(Interval.UNISON, 1, 2, s) == sat, "Smaller intervals count too"

def smallerHelper(n, n1, n2, s):
    s.push()
    s.add(isIntervalOrSmaller(n, n1, n2))
    res = s.check()
    s.pop()
    return res

def test_is_interval_or_smaller(s):
    assert smallerHelper(Interval.UNISON, 1, 2, s) == unsat, "func should judge by interval, not distance"
    assert smallerHelper(Interval.SECOND, 1, 2, s) == sat, "func should judge by interval"
    assert smallerHelper(Interval.THIRD, 1, 2, s) == sat, "Larger intervals count too"

def isDissonantHelper(n1, n2, s):
    s.push()
    s.add(isDissonant(n1, n2))
    res = s.check()
    s.pop()
    return res

def test_is_dissonant(s):
    assert isDissonantHelper(1, 7, s) == sat
    assert isDissonantHelper(1, 2, s) == sat
    assert isDissonantHelper(1, 4, s) == sat
    assert isDissonantHelper(1, 5, s) == unsat
    assert isDissonantHelper(7, 1, s) == sat
    assert isDissonantHelper(2, 1, s) == sat
    assert isDissonantHelper(4, 1, s) == sat
    assert isDissonantHelper(5, 1, s) == unsat
