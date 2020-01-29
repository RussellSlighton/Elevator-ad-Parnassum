from typing import List

from src.player.equalTemperamentSinSynth import *
from src.types import *

# Entrypoint for external users
def playPiece(voices: List[Voice]):
    if len(voices) != 1:
        raise Exception("Only 1 line supported rn")
    playNotes(getNotes(voices[0]), getTonicIndex(voices[0]))

def playVoice(notes, tonicIndex):
    playNotes(notes, tonicIndex)
