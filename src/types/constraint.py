#TODO: Write and test this
from z3 import ExprRef, Optimize

class Constraint:
    def __init__(self, formula : ExprRef, purpose: str):
        self.formula = formula
        self.purpose = purpose

    def apply(self, opt : Optimize):
        opt.add(self.formula)

    def applyWithTracking(self, opt : Optimize):
        opt.assert_and_track(self.formula, self.purpose)

    def __repr__(self):
        return str("|" +self.purpose + "|")
