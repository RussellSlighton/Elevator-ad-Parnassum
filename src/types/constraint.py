# TODO: Write and test this
from z3 import ExprRef, Optimize, Not

class Constraint:
    def __init__(self, formula: ExprRef, description: str):
        self.formula = formula
        self.description = description

    def __repr__(self):
        return str("|" + self.description + "|")

    def inv(self):
        return Constraint(Not(self.formula), "inverse of " + self.description)