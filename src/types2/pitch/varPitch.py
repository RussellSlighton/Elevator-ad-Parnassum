from z3 import Int

from src.types2.pitch.pitch import Pitch

class VarPitch(Pitch):
    def __init__(self, name: str):
        super().__init__(Int(name + "_Letter"), Int(name + "_Octave"))
        self.name = name
