from typing import List

from z3 import *

from src.types.spec import Spec
from src.types.constraint import *
from src.types.pitch import ConstPitch, Pitch

class SpeciesForge:

    def __init__(self, opt : Optimize):
        self.opt = opt

    def applySpec(self, spec : Spec):
        for c in spec.constraints:
            self.apply(c)
        for mi in spec.minimisations:
            self.minimise(mi)
        for ma in spec.maximisations:
            self.maximise(ma)

    def applyAndTrackSpec(self, spec : Spec):
        for c in spec.constraints:
            self.applyAndTrack(c)
        for mi in spec.minimisations:
            self.minimise(mi)
        for ma in spec.maximisations:
            self.maximise(ma)

    def apply(self, constraint : Constraint):
        self.opt.add(constraint.formula)
        return self

    def applyAndTrack(self, constraint : Constraint):
        self.opt.assert_and_track(constraint.formula, str(constraint.constraintType) + ": " + constraint.description)
        return self

    def maximise(self, indicators) -> None:
        count = sum([If(ind, 1, 0) for ind in indicators])
        self.opt.maximize(count)

    def minimise(self, indicators) -> None:
        count = sum([If(ind, 1, 0) for ind in indicators])
        self.opt.minimize(count)

    def check(self):
        return self.opt.check()

    def getReasonsForUnsat(self) -> List[str]:
        self.check()
        return [str(x) for x in self.opt.unsat_core()]

    def getModel(self):
        self.check()
        return self.opt.model()

    def extractPitch(self, pitch : Pitch):
        self.check()

        letter = self.getModel()[pitch.letter].as_long()
        octave = self.getModel()[pitch.octave].as_long()
        return ConstPitch(letter, octave).flattened()
