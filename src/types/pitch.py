from z3 import *

class Pitch:
    def __init__(self, name):
        self.name = name
        self.degree = Int(name + "_Degree")
        self.octave = Int(name + "_Octave")

    def asInt(self) -> Int:
        return self.degree + 7 * self.octave

    def __eq__(self, other):
        if isinstance(other, Pitch):
            return self.asInt() == other.asInt()
        return self.asInt() == other

    def __ne__(self, other):
        if isinstance(other, Pitch):
            return self.asInt() != other.asInt()
        return self.asInt() != other

    def __lt__(self, other):
        if isinstance(other, Pitch):
            return self.asInt() < other.asInt()
        return self.asInt() < other

    def __le__(self, other):
        if isinstance(other, Pitch):
            return self.asInt() <= other.asInt()
        return self.asInt() <= other

    def __gt__(self, other):
        if isinstance(other, Pitch):
            return self.asInt() > other.asInt()
        return self.asInt() > other

    def __ge__(self, other):
        if isinstance(other, Pitch):
            return self.asInt() >= other.asInt()
        return self.asInt() >= other

    def __add__(self, other):
        if isinstance(other, Pitch):
            return self.asInt() + other.asInt()
        return self.asInt() + other

    def __sub__(self, other):
        if isinstance(other, Pitch):
            return self.asInt() - other.asInt()
        return self.asInt() - other

    def __mul__(self, other):
        if isinstance(other, Pitch):
            return self.asInt() * other.asInt()
        return self.asInt() * other

    def __radd__(self, other):
        if isinstance(other, Pitch):
            return self.asInt() + other.asInt()
        return self.asInt() + other

    def __rsub__(self, other):
        if isinstance(other, Pitch):
            return self.asInt() - other.asInt()
        return self.asInt() - other

    def __rmul__(self, other):
        if isinstance(other, Pitch):
            return self.asInt() * other.asInt()
        return self.asInt() * other

    def __hash__(self):
        return hash((self.degree, self.octave))

    def __repr__(self):
        return self.name