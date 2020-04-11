from pytest import fixture
from z3 import Optimize, sat, unsat

from src.specs.badSpecsFactory import powset, getAllBadSpecs
from src.specs import cantusSpec
from src.types2 import Foundry

@fixture
def length():
    return 4

@fixture()
def name():
    return ""

@fixture
def gamutLength():
    return 5


@fixture
def spec(length, name, gamutLength):
    return cantusSpec(length, gamutLength, name)

def test_powset():
    assert powset([1,2,3]) == [[], [1], [2], [3], [1, 2], [1, 3], [2, 3], [1, 2, 3]]
    assert len(powset(range(0,10))) == 2**10

def test_getAllBadSpecsCorrectSpecCount(spec):
    assert len(getAllBadSpecs(spec)) > 0

def test_defaultsAreSatisfiable(spec):
    assert Foundry(Optimize()).applySpec(spec).check() == sat

def test_allBadSpecsSatisfiable(spec):
    badSpecs = getAllBadSpecs(spec, 15)
    for badSpec in badSpecs:
        foundry = Foundry(Optimize()).applySpec(badSpec)
        assert foundry.check() == sat

def test_allBadSpecsAreBad(spec):
    badSpecs = getAllBadSpecs(spec, 15)
    for badSpec in badSpecs:
        foundry = Foundry(Optimize()).applyAndTrackSpec(badSpec).applyAndTrackSpec(spec)
        assert foundry.check() == unsat
        assert len(foundry.getReasonsForUnsat()) != 0

