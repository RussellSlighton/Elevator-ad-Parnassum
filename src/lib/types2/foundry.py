from typing import List

from z3 import *

from src.lib.types2.constraint import *
from src.lib.types2.line import Line
from src.lib.types2.pitch import ConstPitch, Pitch
from src.lib.types2.spec import Spec

class Foundry:

    def __init__(self, opt: Optimize):
        self.opt = opt

    def applySpec(self, spec: Spec):
        self.applyAll(spec.constraints)
        for mi in spec.minimisations:
            self.minimise(mi)
        for ma in spec.maximisations:
            self.maximise(ma)

        return self

    def applyAndTrackSpec(self, spec: Spec):
        self.applyAndTrackAll(spec.constraints)
        for mi in spec.minimisations:
            self.minimise(mi)
        for ma in spec.maximisations:
            self.maximise(ma)

        return self

    def apply(self, constraint: Constraint):
        self.opt.add(constraint.formula)
        return self

    def applyAll(self, constraints: List[Constraint]):
        for c in constraints:
            self.apply(c)
        return self

    def applyAndTrack(self, constraint: Constraint):
        self.opt.assert_and_track(
            constraint.formula,
            str(constraint.constraintType) + ": " + constraint.description
        )
        return self

    def applyAndTrackAll(self, constraints: List[Constraint]):
        for c in constraints:
            self.applyAndTrack(c)
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
        return self.opt.model()

    def extractPitch(self, pitch: Pitch):
        letter = self.getModel()[pitch.letter].as_long()
        octave = self.getModel()[pitch.octave].as_long()
        return ConstPitch(letter, octave).flattened()

    def extractPitches(self, line: Line):
        self.check()
        return [self.extractPitch(p) for p in line]
