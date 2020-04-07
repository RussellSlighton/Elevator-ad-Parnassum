from z3 import *

from src.types.constraint import Constraint
from pytest import fixture

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
    return Constraint(logic, descr)

@fixture
def opt():
    return Optimize()

def test_constructor(c, logic, descr):
    assert c.purpose == descr
    assert c.formula == logic

def test_apply_isSatisfiable(opt, c):
    c.apply(opt)
    assert opt.check() == sat

def test_apply_constrains(opt, c):
    c.apply(opt)
    opt.add(Not(c.formula))
    assert opt.check() == unsat

def test_apply_doesNotTrack(opt,c):
    c.apply(opt)
    opt.add(Not(c.formula))
    opt.check()
    x = opt.unsat_core()
    assert len(x) == 0

def test_applyWithTracking_isSatisfiable(opt, c):
    c.applyWithTracking(opt)
    assert opt.check() == sat

def test_applyWithTracking_constrains(opt, c):
    c.applyWithTracking(opt)
    opt.add(Not(c.formula))
    assert opt.check() == unsat

def test_applyWithTracking_doesTrack(opt,c):
    c.applyWithTracking(opt)
    opt.add(Not(c.formula))
    opt.check()
    x = opt.unsat_core()
    print(x)
    assert len(x) == 1
    assert str(x[0]) == c.purpose