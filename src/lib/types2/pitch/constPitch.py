import math

from src.lib.types2.pitch.pitch import Pitch

maxLetter = 12

class ConstPitch(Pitch):
    def __init__(self, *args: int):
        if len(args) == 2:
            super().__init__(args[0], args[1])
        elif len(args) == 1:
            letter = args[0] % maxLetter
            octave = math.floor(args[0] / maxLetter)
            super().__init__(letter, octave)
        else:
            raise Exception("Pitch cannot be constructed from more than two values")