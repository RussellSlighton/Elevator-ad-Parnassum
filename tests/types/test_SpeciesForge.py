from pytest import fixture
from z3 import *

from src.types import SpeciesForge, Constraint, ConstPitch, VarPitch, ConstraintType, Spec

@fixture
def opt():
    return Optimize()

@fixture
def forge(opt):
    return SpeciesForge(opt)

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
    return Spec([constraint], [],[])

def testForgeConstructor(forge, opt):
    assert forge.opt == opt

def testForgeWithUntrackedConstraintsIsSat(forge, constraint, opt):
    forge.apply(constraint)
    assert forge.check() == sat

def testForgeWithUntrackedConstraintsConstrains(forge, constraint):
    forge.apply(constraint)
    forge.apply(constraint.inv())
    assert forge.check() == unsat

def testForgeWithUntrackedConstaintsDoesNotTrack(forge, constraint):
    forge.apply(constraint)
    forge.apply(constraint.inv())
    assert len(forge.getReasonsForUnsat()) == 0

def testForgeWithTrackedConstraintsIsSat(forge, constraint, opt):
    forge.applyAndTrack(constraint)
    assert forge.check() == sat

def testForgeWithTrackedConstraintsConstrains(forge, constraint):
    forge.applyAndTrack(constraint)
    forge.applyAndTrack(constraint.inv())
    assert forge.check() == unsat

def testForgeWithTrackedConstaintsDoesNotTrack(forge, constraint):
    forge.applyAndTrack(constraint)
    forge.applyAndTrack(constraint.inv())
    assert len(forge.getReasonsForUnsat()) == 2
    assert str(constraint.constraintType) + ": " + constraint.description in forge.getReasonsForUnsat()
    assert str(constraint.constraintType) + ": " + constraint.inv().description in forge.getReasonsForUnsat()

def testForgeWithMixedTracking(forge, constraint):
    forge.apply(constraint)
    forge.applyAndTrack(constraint.inv())
    assert len(forge.getReasonsForUnsat()) == 1
    assert forge.getReasonsForUnsat()[0] == str(constraint.constraintType) + ": " + constraint.inv().description

def testExtractPitches(forge):
    p0 = VarPitch('x')
    p1 = ConstPitch(4)
    forge.apply(Constraint(p0 == p1, ConstraintType.MISC, "bla"))
    assert forge.extractPitch(p0) == p1.flattened()

def testApplySpecWithoutTrackingIsSat(forge, spec):
    forge.applySpec(spec)
    assert forge.check() == sat

def testApplySpecWithoutTrackingConstrains(forge, spec, ):
    forge.applySpec(spec)
    forge.apply(spec.constraints[0].inv())
    assert forge.check() == unsat

def testApplySpecWithoutTrackingDoesNotTrack(forge, spec, ):
    forge.applySpec(spec)
    forge.apply(spec.constraints[0].inv())
    assert forge.getReasonsForUnsat() == []

def testApplySpecWithTrackingIsSat(forge, spec):
    forge.applyAndTrackSpec(spec)
    assert forge.check() == sat

def testApplySpecWithoutTrackingConstrains(forge, spec, ):
    forge.applyAndTrackSpec(spec)
    forge.apply(spec.constraints[0].inv())
    assert forge.check() == unsat

def testApplySpecWithoutTrackingDoesNotTrack(forge, spec, ):
    forge.applyAndTrackSpec(spec)
    forge.apply(spec.constraints[0].inv())
    assert len(forge.getReasonsForUnsat()) == 1

def test_maximise(forge):
    a = Bool('a')
    b = Bool('b')
    forge.maximise([a, b])
    assert forge.check() == sat
    ps = [forge.getModel()[p] for p in [a, b]]
    assert ps == [True, True]

def test_minimise(forge):
    a = Bool('a')
    b = Bool('b')
    forge.minimise([a, b])
    assert forge.check() == sat
    ps = [forge.getModel()[p] for p in [a, b]]
    assert ps == [False, False]
