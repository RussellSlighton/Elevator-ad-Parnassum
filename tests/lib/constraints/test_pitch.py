import pytest

from src.lib.constraints.pitch import *
from src.lib.types2 import ConstPitch

def run2(function, arg1, arg2):
    s = Solver()
    s.add(function(ConstPitch(arg1), ConstPitch(arg2)))
    return s

def run3(function, arg0, arg1, arg2):
    s = Solver()
    s.add(function(arg0, ConstPitch(arg1), ConstPitch(arg2)))
    return s

def test_isNApart_negative():
    assert run3(isNthInterval, Interval.SECOND(), -3, -1).check() == sat, "isNApart works on negatives"
    assert run3(isNthInterval, Interval.SECOND(), -3, -2).check() == unsat, "isNApart works on negatives"
    assert run3(isNthInterval, Interval.SECOND(), -2, -3).check() == unsat, "isNApart works on negatives"

def test_isNApart_positive():
    assert run3(isNthInterval, Interval.SECOND(), 4, 6).check() == sat, "isNApart works on negatives"
    assert run3(isNthInterval, Interval.SECOND(), 2, 3).check() == unsat, "isNApart works on negatives"
    assert run3(isNthInterval, Interval.SECOND(), 2, 3).check() == unsat, "isNApart works on negatives"

def test_is_unison():
    assert run2(isUnison, 0, 0).check() == sat
    assert run2(isUnison, 1, 1).check() == sat
    assert run2(isUnison, -1, -1).check() == sat
    assert run2(isUnison, 1, 2).check() == unsat

def test_is_second():
    assert run2(isSecond, 1, 1 + Interval.SECOND().semitoneDistance).check() == sat
    assert run2(isSecond, -2, -2 + Interval.SECOND().semitoneDistance).check() == sat
    assert run2(isSecond, 1, 2 + Interval.SECOND().semitoneDistance).check() == unsat

def test_is_third():
    assert run2(isThird, 1, 1 + Interval.THIRD().semitoneDistance).check() == sat
    assert run2(isThird, -3, -3 + Interval.THIRD().semitoneDistance).check() == sat
    assert run2(isThird, 1, 1).check() == unsat

def test_is_fourth():
    assert run2(isFourth, 1, 1 + Interval.FOURTH().semitoneDistance).check() == sat
    assert run2(isFourth, -4, -4 + Interval.FOURTH().semitoneDistance).check() == sat
    assert run2(isFourth, 1, 1).check() == unsat

def test_is_fifth():
    assert run2(isFifth, 1, 1 + Interval.FIFTH().semitoneDistance).check() == sat
    assert run2(isFifth, -5, -5 + Interval.FIFTH().semitoneDistance).check() == sat
    assert run2(isFifth, 1, 1).check() == unsat

def test_is_sixth():
    assert run2(isSixth, 1, 1 + Interval.SIXTH().semitoneDistance).check() == sat
    assert run2(isSixth, -6, -6 + Interval.SIXTH().semitoneDistance).check() == sat
    assert run2(isSixth, 1, 1).check() == unsat

def test_is_seventh():
    assert run2(isSeventh, 1, 1 + Interval.SEVENTH().semitoneDistance).check() == sat
    assert run2(isSeventh, -7, -7 + Interval.SEVENTH().semitoneDistance).check() == sat
    assert run2(isSeventh, 1, 1).check() == unsat

def test_is_octave():
    assert run2(isOctave, 1, 1 + Interval.OCTAVE().semitoneDistance).check() == sat
    assert run2(isOctave, -8, -8 + Interval.OCTAVE().semitoneDistance).check() == sat
    assert run2(isOctave, 1, 1).check() == unsat

# TODO: This really should be mocked
@pytest.fixture
def s():
    return Solver()

def consHelper(n1, n2, s):
    s.push()
    s.add(isConsonant(ConstPitch(n1), ConstPitch(n2)))
    res = s.check()
    s.pop()
    return res

def test_is_consonant(s):
    assert consHelper(1, 1, s) == sat, "Unison is consonant"
    assert consHelper(1, 1 + Interval.THIRD().semitoneDistance, s) == sat, "Third is consonant"
    assert consHelper(1, 1 + Interval.FIFTH().semitoneDistance, s) == sat, "Fifth is consonant"
    assert consHelper(0, Interval.OCTAVE().semitoneDistance, s) == sat, "Octave is consonant"
    assert consHelper(0, Interval.SIXTH().semitoneDistance, s) == unsat, "Sixth is not consonant"

def triadicHelper(n1, n2, n3, s):
    s.push()
    s.add(isTriadic(ConstPitch(n1), ConstPitch(n2), ConstPitch(n3)))
    res = s.check()
    s.pop()
    return res

def test_is_triadic(s):
    assert triadicHelper(Interval.UNISON().semitoneDistance, Interval.THIRD().semitoneDistance,
                         Interval.FIFTH().semitoneDistance, s) == sat
    assert triadicHelper(Interval.UNISON().semitoneDistance, Interval.THIRD().semitoneDistance,
                         Interval.OCTAVE().semitoneDistance, s) == sat
    assert triadicHelper(Interval.UNISON().semitoneDistance, Interval.FOURTH().semitoneDistance,
                         Interval.OCTAVE().semitoneDistance, s) == unsat

def stepHelper(n1, n2, s):
    s.push()
    s.add(isStep(ConstPitch(n1), ConstPitch(n2)))
    res = s.check()
    s.pop()
    return res

def test_is_step(s):
    assert stepHelper(Interval.UNISON().semitoneDistance, Interval.SECOND().semitoneDistance,
                      s) == sat, "step works going up"
    assert stepHelper(Interval.SECOND().semitoneDistance, Interval.UNISON().semitoneDistance,
                      s) == sat, "step works going down"
    assert stepHelper(Interval.SECOND().semitoneDistance, Interval.OCTAVE().semitoneDistance,
                      s) == unsat, "leaps don't count as steps"

def leapHelper(n1, n2, s):
    s.push()
    s.add(isLeap(ConstPitch(n1.semitoneDistance), ConstPitch(n2.semitoneDistance)))
    res = s.check()
    s.pop()
    return res

def test_is_leap(s):
    assert leapHelper(Interval.UNISON(), Interval.FIFTH(), s) == sat, "leap works going up"
    assert leapHelper(Interval.FIFTH(), Interval.UNISON(), s) == sat, "leap works going down"
    assert leapHelper(Interval.UNISON(), Interval.FOURTH(), s) == unsat, "skips don't count as leaps"

def skipHelper(n1, n2, s):
    s.push()
    s.add(isSkip(ConstPitch(n1.semitoneDistance), ConstPitch(n2.semitoneDistance)))
    res = s.check()
    s.pop()
    return res

def test_is_skip(s):
    assert skipHelper(Interval.UNISON(), Interval.THIRD(), s) == sat, "3 skip works going up"
    assert skipHelper(Interval.THIRD(), Interval.UNISON(), s) == sat, "3 skip works going down"
    assert skipHelper(Interval.SECOND(), Interval.FOURTH(), s) == sat, "4 skip works going up"
    assert skipHelper(Interval.FOURTH(), Interval.UNISON(), s) == sat, "4 skip works going down"
    assert skipHelper(Interval.UNISON(), Interval.FIFTH(), s) == unsat, "leaps don't count as skips"
    assert skipHelper(Interval.UNISON(), Interval.SECOND(), s) == unsat, "steps don't count as skips"

def test_isMotionUp():
    assert isMotionUp(1, 2)
    assert not isMotionUp(1, 1), "Unison is not motion"
    assert not isMotionUp(1, 0), "Down is not up"

def test_isMotionDown():
    assert isMotionDown(2, 1)
    assert not isMotionDown(1, 1), "Unison is not motion"
    assert not isMotionDown(1, 2), "Up is not down"

def largerHelper(n, n1, n2, s):
    s.push()
    s.add(isIntervalOrLarger(n, ConstPitch(n1), ConstPitch(n2)))
    res = s.check()
    s.pop()
    return res

def test_is_interval_or_larger(s):
    assert largerHelper(Interval.THIRD(), Interval.UNISON().semitoneDistance, Interval.SECOND().semitoneDistance,
                        s) == unsat, "func should judge by interval, not distance"
    assert largerHelper(Interval.SECOND(), Interval.UNISON().semitoneDistance, Interval.SECOND().semitoneDistance,
                        s) == sat, "func should judge by interval"
    assert largerHelper(Interval.UNISON(), Interval.UNISON().semitoneDistance, Interval.SECOND().semitoneDistance,
                        s) == sat, "Smaller intervals count too"

def smallerHelper(n, n1, n2, s):
    s.push()
    s.add(isIntervalOrSmaller(n, ConstPitch(n1), ConstPitch(n2)))
    res = s.check()
    s.pop()
    return res

def test_is_interval_or_smaller(s):
    assert smallerHelper(Interval.UNISON(), Interval.UNISON().semitoneDistance, Interval.SECOND().semitoneDistance,
                         s) == unsat, "func should judge by interval, not distance"
    assert smallerHelper(Interval.SECOND(), Interval.UNISON().semitoneDistance, Interval.SECOND().semitoneDistance,
                         s) == sat, "func should judge by interval"
    assert smallerHelper(Interval.THIRD(), Interval.UNISON().semitoneDistance, Interval.SECOND().semitoneDistance,
                         s) == sat, "Larger intervals count too"

def isDissonantHelper(n1, n2, s):
    s.push()
    s.add(isDissonant(ConstPitch(n1), ConstPitch(n2)))
    res = s.check()
    s.pop()
    return res

def test_is_dissonant(s):
    assert isDissonantHelper(Interval.UNISON().semitoneDistance, Interval.SEVENTH().semitoneDistance, s) == sat
    assert isDissonantHelper(Interval.UNISON().semitoneDistance, Interval.SECOND().semitoneDistance, s) == sat
    assert isDissonantHelper(Interval.UNISON().semitoneDistance, Interval.FOURTH().semitoneDistance, s) == sat
    assert isDissonantHelper(Interval.UNISON().semitoneDistance, Interval.FIFTH().semitoneDistance, s) == unsat
    assert isDissonantHelper(Interval.UNISON().semitoneDistance, Interval.THIRD().semitoneDistance, s) == unsat
    assert isDissonantHelper(Interval.SECOND().semitoneDistance, Interval.UNISON().semitoneDistance, s) == sat
    assert isDissonantHelper(Interval.SEVENTH().semitoneDistance, Interval.UNISON().semitoneDistance, s) == sat
    assert isDissonantHelper(Interval.FOURTH().semitoneDistance, Interval.UNISON().semitoneDistance, s) == sat
    assert isDissonantHelper(Interval.FIFTH().semitoneDistance, Interval.UNISON().semitoneDistance, s) == unsat

def test_pitchIsValid(s):
    line = Line(1, '')
    p = line[0]
    s.push()
    s.add(p.letter == IntVal(-1))
    s.add(pitchesLetterValueValid(line).formula)
    assert s.check() == unsat

    s.pop()
    s.push()
    s.add(p.letter == IntVal(1))
    s.add(pitchesLetterValueValid(line).formula)
    assert s.check() == sat

    s.pop()
    s.push()
    s.add(p.letter == IntVal(12))
    s.add(pitchesLetterValueValid(line).formula)
    assert s.check() == unsat