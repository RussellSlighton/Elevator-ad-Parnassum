from z3 import Int

from src.types2.pitch import VarPitch

def test_pitch():
    ID = "a"
    pitch = VarPitch(ID)
    assert pitch.letter == Int(ID + "_Letter")
    assert pitch.octave == Int(ID + "_Octave")
