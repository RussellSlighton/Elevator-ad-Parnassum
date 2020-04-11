from pytest import fixture
from z3 import *

from src.lib.types2 import Foundry, Constraint, ConstPitch, VarPitch, ConstraintType, Spec, Line

@fixture
def opt():
    return Optimize()

@fixture
def foundry(opt):
    return Foundry(opt)

@fixture
def descr():
    return "x must be 1"

@fixture
def logic():
    return Int('x') == 1

@fixture
def constraint(logic, descr):
    return Constraint(logic, ConstraintType.MISC, descr)

@fixture
def spec(constraint):
    return Spec(Line(1, ""), [constraint], [], [])

def testFoundryConstructor(foundry, opt):
    assert foundry.opt == opt

def testFoundryWithUntrackedConstraintsIsSat(foundry, constraint, opt):
    foundry.apply(constraint)
    assert foundry.check() == sat

def testFoundryWithUntrackedConstraintsConstrains(foundry, constraint):
    foundry.apply(constraint)
    foundry.apply(constraint.inv())
    assert foundry.check() == unsat

def testFoundryWithUntrackedConstaintsDoesNotTrack(foundry, constraint):
    foundry.apply(constraint)
    foundry.apply(constraint.inv())
    assert len(foundry.getReasonsForUnsat()) == 0

def testFoundryWithTrackedConstraintsIsSat(foundry, constraint, opt):
    foundry.applyAndTrack(constraint)
    assert foundry.check() == sat

def testFoundryWithTrackedConstraintsConstrains(foundry, constraint):
    foundry.applyAndTrack(constraint)
    foundry.applyAndTrack(constraint.inv())
    assert foundry.check() == unsat

def testFoundryWithTrackedConstaintsDoesNotTrack(foundry, constraint):
    foundry.applyAndTrack(constraint)
    foundry.applyAndTrack(constraint.inv())
    assert len(foundry.getReasonsForUnsat()) == 2
    assert str(constraint.constraintType) + ": " + constraint.description in foundry.getReasonsForUnsat()
    assert str(constraint.constraintType) + ": " + constraint.inv().description in foundry.getReasonsForUnsat()

def testFoundryWithMixedTracking(foundry, constraint):
    foundry.apply(constraint)
    foundry.applyAndTrack(constraint.inv())
    assert len(foundry.getReasonsForUnsat()) == 1
    assert foundry.getReasonsForUnsat()[0] == str(constraint.constraintType) + ": " + constraint.inv().description

def testExtractPitch(foundry):
    p0 = VarPitch('x')
    p1 = ConstPitch(4)
    foundry.apply(Constraint(p0 == p1, ConstraintType.MISC, "bla"))
    foundry.check()
    assert foundry.extractPitch(p0) == p1.flattened()

def testExtractPitches(foundry):
    l = Line(1, '')
    p0 = l[0]
    p1 = ConstPitch(4)
    foundry.apply(Constraint(p0 == p1, ConstraintType.MISC, "bla"))
    assert foundry.extractPitches(l) == [p1.flattened()]

def testApplySpecWithoutTrackingIsSat(foundry, spec):
    foundry.applySpec(spec)
    assert foundry.check() == sat

def testApplySpecWithoutTrackingConstrains(foundry, spec, ):
    foundry.applySpec(spec)
    foundry.apply(spec.constraints[0].inv())
    assert foundry.check() == unsat

def testApplySpecWithoutTrackingDoesNotTrack(foundry, spec, ):
    foundry.applySpec(spec)
    foundry.apply(spec.constraints[0].inv())
    assert foundry.getReasonsForUnsat() == []

def testApplySpecWithTrackingIsSat(foundry, spec):
    foundry.applyAndTrackSpec(spec)
    assert foundry.check() == sat

def testApplySpecWithTrackingConstrains(foundry, spec, ):
    foundry.applyAndTrackSpec(spec)
    foundry.apply(spec.constraints[0].inv())
    assert foundry.check() == unsat

def testApplySpecWithTrackingDoesNotTrack(foundry, spec, ):
    foundry.applyAndTrackSpec(spec)
    foundry.apply(spec.constraints[0].inv())
    assert len(foundry.getReasonsForUnsat()) == 1

def testApplyAllWithoutTrackingIsSat(foundry, constraint):
    foundry.applyAll([constraint, constraint])
    assert foundry.check() == sat

def testApplyAllWithoutTrackingConstrains(foundry, constraint, ):
    foundry.applyAll([constraint, constraint])
    foundry.apply(constraint.inv())
    assert foundry.check() == unsat

def testApplyAllWithoutTrackingDoesNotTrack(foundry, constraint, ):
    foundry.applyAll([constraint, constraint])
    foundry.apply(constraint.inv())
    assert foundry.getReasonsForUnsat() == []

def testApplyAllWithTrackingIsSat(foundry, constraint):
    foundry.applyAndTrackAll([constraint, constraint])
    assert foundry.check() == sat

def testApplyAllWithTrackingConstrains(foundry, constraint, ):
    foundry.applyAndTrackAll([constraint, constraint])
    foundry.apply(constraint.inv())
    assert foundry.check() == unsat

def testApplyAllWithTrackingDoesNotTrack(foundry, constraint, ):
    foundry.applyAndTrackAll([constraint, constraint.inv()])
    assert len(foundry.getReasonsForUnsat()) == 2

def test_maximise(foundry):
    a = Bool('a')
    b = Bool('b')
    foundry.maximise([a, b])
    assert foundry.check() == sat
    ps = [foundry.getModel()[p] for p in [a, b]]
    assert ps == [True, True]

def test_minimise(foundry):
    a = Bool('a')
    b = Bool('b')
    foundry.minimise([a, b])
    assert foundry.check() == sat
    ps = [foundry.getModel()[p] for p in [a, b]]
    assert ps == [False, False]
