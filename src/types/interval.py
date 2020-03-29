from __future__ import annotations

from src.types.pitch.pitch import Pitch
from src.types.z3Utils import logicalAbs

class Interval:
    def __init__(self, semitoneDistance: int):
        self.semitoneDistance = semitoneDistance

    def __eq__(self, other: Interval):
        return self.semitoneDistance == other.semitoneDistance

    def __le__(self, other):
        return self.semitoneDistance <= other.semitoneDistance

    def __repr__(self):
        if self == self.UNISON():
            return "Unison"
        elif self == self.SECOND():
            return "Second"
        elif self == self.THIRD():
            return "Third"
        elif self == self.FIFTH():
            return "Fourth"
        elif self == self.FIFTH():
            return "Fifth"
        elif self == self.SIXTH():
            return "Sixth"
        elif self == self.SEVENTH():
            return "Seventh"
        elif self == self.OCTAVE():
            return "Octave"
        else:
            return "I(" + str(self.semitoneDistance) + ")"

    @staticmethod
    def between(p1: Pitch, p2: Pitch):
        return Interval(p2.flattened() - p1.flattened())

    @staticmethod
    def absBetween(p1: Pitch, p2: Pitch):
        return Interval(logicalAbs(p2.flattened() - p1.flattened()))

    @staticmethod
    def UNISON():
        return Interval(0)

    @staticmethod
    def SECOND():
        return Interval(2)

    @staticmethod
    def THIRD():
        return Interval(4)

    @staticmethod
    def FOURTH():
        return Interval(5)

    @staticmethod
    def FIFTH():
        return Interval(7)

    @staticmethod
    def SIXTH():
        return Interval(9)

    @staticmethod
    def SEVENTH():
        return Interval(11)

    @staticmethod
    def OCTAVE():
        return Interval(12)

    # TODO: Add step, leap, etc
