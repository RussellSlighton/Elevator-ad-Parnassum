from z3 import Or

from src.types2 import Line, Constraint, ConstraintType

def distinctFromExample(line: Line, prevExample) -> Constraint:
    assert len(prevExample) == len(line)
    formula = Or([prevExample[i] != line[i] for i in range(0, len(prevExample))])
    return Constraint(formula, ConstraintType.MISC, "Line must not be exemplar")