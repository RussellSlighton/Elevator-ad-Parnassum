from z3 import *

from src.lib.types2.z3Utils import *

def test_abs():
    x = 1
    assert logicalAbs(x) == If(x >= 0, x, -x), "abs should produce an if statement on the arg value"

def test_find_different():
    x = Int('x')
    xs = [x]
    s = Solver()
    s.add(Or(x == 1, x == 2))
    assert s.check() == sat, "formula should be sat at first"
    findDifferent(xs, s)
    assert s.check() == sat, "formula should be sat after one solve"
    findDifferent(xs, s)
    assert s.check() == unsat, "formula should be unsat after two solves"
