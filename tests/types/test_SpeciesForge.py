from pytest import fixture
from z3 import *

from src.types import SpeciesForge, Constraint, ConstPitch, VarPitch, ConstraintType

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

def testForgeConstructor(forge, opt):
    assert forge.opt == opt

def testForgeWithUntrackedConstraintsIsSat(forge, constraint, opt):
    forge.addConstraint(constraint)
    assert forge.check() == sat

def testForgeWithUntrackedConstraintsConstrains(forge, constraint):
    forge.addConstraint(constraint)
    forge.addConstraint(constraint.inv())
    assert forge.check() == unsat

def testForgeWithUntrackedConstaintsDoesNotTrack(forge, constraint):
    forge.addConstraint(constraint)
    forge.addConstraint(constraint.inv())
    assert len(forge.getReasonsForUnsat()) == 0

def testForgeWithTrackedConstraintsIsSat(forge, constraint, opt):
    forge.addAndTrackConstraint(constraint)
    assert forge.check() == sat

def testForgeWithTrackedConstraintsConstrains(forge, constraint):
    forge.addAndTrackConstraint(constraint)
    forge.addAndTrackConstraint(constraint.inv())
    assert forge.check() == unsat

def testForgeWithTrackedConstaintsDoesNotTrack(forge, constraint):
    forge.addAndTrackConstraint(constraint)
    forge.addAndTrackConstraint(constraint.inv())
    assert len(forge.getReasonsForUnsat()) == 2
    assert constraint.description in forge.getReasonsForUnsat()
    assert constraint.inv().description in forge.getReasonsForUnsat()

def testForgeWithMixedTracking(forge, constraint):
    forge.addConstraint(constraint)
    forge.addAndTrackConstraint(constraint.inv())
    assert len(forge.getReasonsForUnsat()) == 1
    assert forge.getReasonsForUnsat()[0] == constraint.inv().description

def testExtractPitches(forge):
    p0 = VarPitch('x')
    p1 = ConstPitch(4)
    forge.addConstraint(Constraint(p0 == p1, ConstraintType.MISC, "bla"))
    assert forge.extractPitch(p0) == p1.flattened()

