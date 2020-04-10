import pytest

from src.types2.temporalisedLine import *

@pytest.fixture
def tl():
    return makeTemporalisedLine([1, 2, 3], NoteLength.EIGHTH)

def test_make_temporalised_line(tl):
    assert tl == ([1, 2, 3], NoteLength.EIGHTH)

def test_get_pitches(tl):
    assert getNoteLength(tl) == 8

def test_get_note_length(tl):
    assert getPitches(tl) == [1, 2, 3]

def test_as_unique_values():
    m, i = asUniqueValues([makeTemporalisedLine([1, 2, 3], NoteLength.WHOLE),
                           makeTemporalisedLine([4, 5, 6, 7, 8, 9], NoteLength.HALF)])
    assert m == {0: 1, 1: 2, 2: 3, 3: 4, 4: 5, 5: 6, 6: 7, 7: 8, 8: 9}
    assert i == [([0, 1, 2], 1), ([3, 4, 5, 6, 7, 8], 2)]
    assert m[8] == 9
