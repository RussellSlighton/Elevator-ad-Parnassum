import pytest

from src.types.simMap import *
from src.types.simMap import __getNoteLength, __getPitches

def test_privates():
    tl = makeTemporalisedLine([1, 2, 3], NoteLength.EIGHTH)
    assert __getNoteLength(tl) == 8
    assert __getPitches(tl) == [1, 2, 3]

@pytest.fixture
def cf():
    return [(makeTemporalisedLine([1, 9], NoteLength.WHOLE))]

@pytest.fixture
def s1(cf):
    species1 = (makeTemporalisedLine([1, 9], NoteLength.WHOLE))
    return cf + [species1]

@pytest.fixture
def s2(s1):
    species2 = (makeTemporalisedLine([1, 5, 9, 13], NoteLength.HALF))
    return s1 + [species2]

@pytest.fixture
def s3(s2):
    species3 = (makeTemporalisedLine([1, 3, 5, 7, 9, 11, 13, 15], NoteLength.QUARTER))
    return s2 + [species3]

@pytest.fixture
def s4(s3):
    species4 = (makeTemporalisedLine([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16],
                                     NoteLength.EIGHTH))
    return s3 + [species4]

def test_fixtures(s4):
    cfBeats = len(__getPitches(s4[0])) / __getNoteLength(s4[0])
    for s in range(1, 5):
        assert cfBeats == len(__getPitches(s4[s])) / __getNoteLength(s4[s])

def test_make_temporalised_line(cf):
    assert cf[0] == ([1, 9], 1)

def test_make_sim_map_to_s1(s1, cf):
    olds = cf
    new = s1[1]
    sm = makeSimMap(olds, new)
    for p in __getPitches(new):
        assert sm[p] == {p}

def test_make_sim_map_to_s4(s4, s3):
    olds = s3
    new = s4[4]
    sm = makeSimMap(olds, new)
    assert sm == {1: {1}, 2: {1}, 3: {1, 3}, 4: {1, 3}, 5: {1, 5}, 6: {1, 5}, 7: {1, 5, 7}, 8: {1, 5, 7}, 9: {9},
                  10: {9}, 11: {9, 11}, 12: {9, 11}, 13: {9, 13}, 14: {9, 13}, 15: {9, 13, 15}, 16: {9, 13, 15}}
