from typing import List

from z3 import *

from src.types import Constraint, ConstPitch, Pitch

class SpeciesForge():

    def __init__(self, opt : Optimize):
        self.opt = opt

    def addConstraint(self, constraint : Constraint):
        self.opt.add(constraint.formula)
        return self

    def addAndTrackConstraint(self, constraint : Constraint):
        self.opt.assert_and_track(constraint.formula, constraint.description)
        return self

    def check(self):
        return self.opt.check()

    def getReasonsForUnsat(self) -> List[str]:
        self.check()
        return [str(x) for x in self.opt.unsat_core()]

    def __getModel(self):
        self.check()
        return self.opt.model()

    def extractPitch(self, pitch : Pitch):
        self.check()

        letter = self.__getModel()[pitch.letter].as_long()
        octave = self.__getModel()[pitch.octave].as_long()
        return ConstPitch(letter, octave).flattened()

