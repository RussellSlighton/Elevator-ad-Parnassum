from z3 import ExprRef, Not

from src.types2.constraint.constraintType import ConstraintType

class Constraint:
    def __init__(self, formula: ExprRef, constraintType : ConstraintType, description: str):
        self.formula = formula
        self.constraintType = constraintType
        self.description = description

    def __repr__(self):
        return str("|" + self.description + "|")

    def inv(self):
        return Constraint(Not(self.formula), self.constraintType, "inverse of " + self.description)