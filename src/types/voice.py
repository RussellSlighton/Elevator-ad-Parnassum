from typing import List, Tuple

from src.types import *

Voice = Tuple[
    List[int],  # int, not Int, this is for playing, not logiking
    NoteLength,
    TonicIndex
]

def makeVoice(notes: List[int], noteLength: NoteLength, tonicIndex: TonicIndex) -> Voice:
    return (notes, noteLength, tonicIndex)

def getNotes(voice: Voice):
    return voice[0]

def getNoteLength(voice: Voice):
    return voice[1]

def getTonicIndex(voice: Voice):
    return voice[2]
