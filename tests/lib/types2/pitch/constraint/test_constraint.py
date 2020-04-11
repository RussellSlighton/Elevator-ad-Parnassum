from pytest import fixture
from z3 import *

from src.lib.types2 import ConstraintType
from src.lib.types2.constraint import Constraint

@fixture
def var():
    return Int('x')

@fixture
def logic(var):
    return var == 1

@fixture
def descr():
    return 'must be 1'

@fixture
def c(logic, descr):
    return Constraint(logic, ConstraintType.MISC, descr)

@fixture
def opt():
    return Optimize()

def test_constructor(c, logic, descr):
    assert c.description == descr
    assert c.formula == logic

def test_inv_constructs(c, logic, descr):
    assert c.inv().description == "inverse of " + descr
    assert c.inv().formula == Not(logic)

def test_inv_isSatisfiable(c):
    opt = Optimize()
    opt.add(c.inv().formula)
    assert opt.check() == sat

def test_inv_isInverse(c):
    opt = Optimize()
    opt.add(c.inv().formula)
    opt.add(c.formula)
    assert opt.check() == unsat
