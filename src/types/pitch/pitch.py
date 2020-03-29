from __future__ import annotations

class Pitch:
    def __init__(self, letter, octave):
        self.letter = letter
        self.octave = octave

    def flattened(self):
        return self.letter + self.octave * 12

    def __eq__(self, other: Pitch):
        return self.flattened() == other.flattened()

    def __ne__(self, other):
        return self.flattened() != other.flattened()

    def __le__(self, other: Pitch):
        return self.flattened() <= other.flattened()

    def __lt__(self, other: Pitch):
        return self.flattened() < other.flattened()

    def __repr__(self):
        return 'P(' + str(self.letter) + ',' + str(self.octave) + ')'

    def __hash__(self):
        return hash((self.letter, self.octave))
