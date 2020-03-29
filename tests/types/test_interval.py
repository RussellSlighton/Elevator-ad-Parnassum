from pytest import fixture
from z3 import If

from src.types.interval import *
from src.types.pitch.constPitch import ConstPitch

@fixture
def constantPitch():
    return Pitch(1, 2)

def test_interval_constructor():
    assert Interval(4).semitoneDistance == 4

def test_interval_equality():
    assert Interval(4) == Interval(4)
    assert not Interval(4) == Interval(3)

def test_interval_defaults():
    assert Interval.UNISON() == Interval(0)
    assert Interval.SECOND() == Interval(2)
    assert Interval.THIRD() == Interval(4)
    assert Interval.FOURTH() == Interval(5)
    assert Interval.FIFTH() == Interval(7)
    assert Interval.SIXTH() == Interval(9)
    assert Interval.SEVENTH() == Interval(11)
    assert Interval.OCTAVE() == Interval(12)

def test_repr():
    assert str(Interval.UNISON()) == "Unison"
    assert str(Interval(-1)) == "I(-1)"

def test_le():
    assert Interval.SECOND() <= Interval.SECOND()
    assert Interval.SECOND() <= Interval.THIRD()
    assert not Interval.SECOND() <= Interval.UNISON()

def test_between(constantPitch):
    assert Interval.between(constantPitch, constantPitch) == Interval.UNISON()
    assert Interval.between(constantPitch, ConstPitch(constantPitch.letter + Interval.SECOND().semitoneDistance,
                                                      constantPitch.octave)) == Interval.SECOND()
    assert Interval.between(constantPitch,
                            ConstPitch(constantPitch.letter, constantPitch.octave + 1)) == Interval.OCTAVE()

def test_abs_between(constantPitch):
    assert Interval.absBetween(constantPitch, ConstPitch(constantPitch.letter + Interval.SECOND().semitoneDistance,
                                                         constantPitch.octave)) == Interval(logicalAbs(2))
    assert Interval.absBetween(
        ConstPitch(constantPitch.letter + Interval.SECOND().semitoneDistance, constantPitch.octave),
        constantPitch) == Interval(If(False, -2, 2))
