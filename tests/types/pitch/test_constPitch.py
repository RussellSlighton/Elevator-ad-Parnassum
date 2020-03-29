from src.types import ConstPitch

def test_twoArgConstructorWorks():
    p = ConstPitch(1, 2)
    assert p.letter == 1
    assert p.octave == 2

def test_oneArgConstructorWorks_zerothOctave():
    p = ConstPitch(1)
    assert p.letter == 1
    assert p.octave == 0

def test_oneArgConstructorWorks_PositiveOctave():
    p = ConstPitch(27)
    assert p.letter == 3
    assert p.octave == 2

def test_oneArgConstructorWorks_NegativeOctave():
    p = ConstPitch(-3)
    assert p.letter == 9
    assert p.octave == -1
