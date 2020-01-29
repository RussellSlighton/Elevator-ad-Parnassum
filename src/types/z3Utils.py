from z3 import If, Or

def logicalAbs(x):
    return If(x >= 0, x, -x)

def findDifferent(predicates, solver):
    vals = []
    for p in predicates:
        vals.append((p, solver.model()[p]))
    solver.add(Or([v[0] != v[1] for v in vals]))
