from src.types.interval import *

def test_interval():
    assert Interval.UNISON == 0
    assert Interval.SECOND == 1
    assert Interval.THIRD == 2
    assert Interval.FOURTH == 3
    assert Interval.FIFTH == 4
    assert Interval.SIXTH == 5
    assert Interval.SEVENTH == 6
    assert Interval.OCTAVE == 7
