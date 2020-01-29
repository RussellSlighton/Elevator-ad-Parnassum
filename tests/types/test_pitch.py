import pytest

from src.types.pitch import *

@pytest.fixture
def pitches():
    pitches = []
    for i in range(0, 20):
        pitches.append(Int(str(i)))
    return pitches

def test_make_pitch():
    ID = "a"
    assert makePitch(ID) == Int(ID), "Pitch should be a Z3 int"
