import pytest

from src.constraints.pitch import *

def test_isNApart_z3_primitives():
    assert not isNApart(1, Int(""), Int("")), "isNApart type checks on z3 Ints"

def test_isNApart_negative():
    assert isNApart(1, -2, -1), "isNApart works on negatives"

def test_isNApart_positive():
    assert isNApart(1, 1, 2), "isNApart works on positives"

def test_isNApart__not_abs():
    assert not isNApart(1, 2, 1), "isNApart does not use absolute value"

def test_is_unison():
    assert isUnison(0, 0)
    assert isUnison(1, 1)
    assert isUnison(-1, -1)
    assert not isUnison(1, 2)

def test_is_second():
    assert isSecond(1, 2)
    assert isSecond(-2, -1)
    assert not isSecond(1, 1)

def test_is_third():
    assert isThird(1, 3)
    assert isThird(-3, -1)
    assert not isThird(1, 1)

def test_is_fourth():
    assert isFourth(1, 4)
    assert isFourth(-4, -1)
    assert not isFourth(1, 1)

def test_is_fifth():
    assert isFifth(1, 5)
    assert isFifth(-5, -1)
    assert not isFifth(1, 1)

def test_is_sixth():
    assert isSixth(1, 6)
    assert isSixth(-6, -1)
    assert not isSixth(1, 1)

def test_is_seventh():
    assert isSeventh(1, 7)
    assert isSeventh(-7, -1)
    assert not isSeventh(1, 1)

def test_is_octave():
    assert isOctave(1, 8)
    assert isOctave(-8, -1)
    assert not isOctave(1, 1)

# TODO: This really should be mocked
@pytest.fixture
def s():
    return Solver()

def ppHelper(n1, n2, s):
    s.push()
    s.add(isPalestrinaPerfect(n1, n2))
    res = s.check()
    s.pop()
    return res

def test_is_palestrina_perfect(s):
    assert ppHelper(1, 8, s) == sat, "Octave is PP"
    assert ppHelper(1, 1, s) == sat, "Unison is PP"
    assert ppHelper(1, 5, s) == sat, "Octave is PP"
    assert ppHelper(1, 6, s) == unsat, "Sixth is not PP"
    assert ppHelper(8, 1, s) == unsat, "backwards eight is not PP"
    assert ppHelper(5, 1, s) == unsat, "backwards fifth is not PP"

def consHelper(n1, n2, s):
    s.push()
    s.add(isConsonant(n1, n2))
    res = s.check()
    s.pop()
    return res

def test_is_consonant(s):
    assert consHelper(1, 1, s) == sat, "Unison is consonant"
    assert consHelper(1, 3, s) == sat, "Third is consonant"
    assert consHelper(1, 5, s) == sat, "Fifth is consonant"
    assert consHelper(1, 8, s) == sat, "Octave is consonant"
    assert consHelper(1, 6, s) == unsat, "Sixth is not consonant"
    assert consHelper(3, 1, s) == unsat, "backwards Third is not consonant"
    assert consHelper(5, 1, s) == unsat, "backwards fifth is not consonant"
    assert consHelper(8, 1, s) == unsat, "backwards octave is not consonant"

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
