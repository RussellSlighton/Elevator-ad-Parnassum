import pytest

from src.types.pitch import *

@pytest.fixture
def pitches():
    pitches = []
    for i in range(0, 20):
        pitches.append(Int(str(i)))
    return pitches

def test_pitch():
    ID = "a"
    pitch = Pitch(ID)
    assert pitch.degree == Int(ID + "_Degree")
    assert pitch.octave == Int(ID + "_Octave")

def test_asInt():
    pitch = Pitch("")
    assert pitch.asInt() == pitch.asInt()