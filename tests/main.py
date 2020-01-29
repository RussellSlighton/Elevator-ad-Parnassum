import pytest

from src.main import *

@pytest.fixture
def opt():
    return Optimize()

@pytest.fixture
def l():
    return makeLine(2, "l")

def test_extract_voices(opt, l):
    opt.add(l[0] == 10)
    opt.add(l[1] == 20)
    v = extractVoice(opt, l)
    assert v == [10, 20]

def test_createCantusFirmus():
    length = 4
    gamutSize = 4
    tonicIndex = 1
    cf = createCantusFirmus(length, tonicIndex, gamutSize)
    assert len(cf) == length
    for p in cf:
        assert p in range(0, gamutSize)
    assert cf[0] == tonicIndex, "This test assumes the first note of a CF must be the tonic"
