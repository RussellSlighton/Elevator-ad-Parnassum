import pytest

from src.types.voice import *

@pytest.fixture
def v():
    return makeVoice([1, 2, 3], NoteLength.WHOLE, 1)

def test_make_voice(v):
    assert v == ([1, 2, 3], NoteLength.WHOLE, 1)

def test_get_notes(v):
    assert getNotes(v) == [1, 2, 3]

def test_get_note_length(v):
    assert getNoteLength(v) == NoteLength.WHOLE

def test_get_tonic_index(v):
    assert getTonicIndex(v) == 1
