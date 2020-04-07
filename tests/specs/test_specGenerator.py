from pytest import fixture
from z3 import Optimize, sat

from src.specs import *
from src.types import Spec, Line

@fixture
def length():
    return 8

@fixture()
def name():
    return ""

@fixture
def gamutLength():
    return 20

@fixture
def cf(length, name, gamutLength):
    return cantusSpec(length, name, gamutLength)

@fixture
def fixedCF(length, name):
    return Line(length, name+"cf")

@fixture
def s1(fixedCF, name, gamutLength):
    return firstSpeciesSpec(fixedCF, name, gamutLength)

@fixture
def s2(fixedCF, name, gamutLength):
    return firstSpeciesSpec(fixedCF, name, gamutLength)

@fixture
def s3(fixedCF, name, gamutLength):
    return firstSpeciesSpec(fixedCF, name, gamutLength)

@fixture
def opt():
    return Optimize()

def test_cf(cf : Spec, opt):
    for c in cf.constraints:
        opt.add(c.formula)
    assert opt.check() == sat

def test_s1(s1 : Spec, opt):
    for c in s1.constraints:
        opt.add(c.formula)
    assert opt.check() == sat

def test_s2(s2: Spec, opt):
    for c in s2.constraints:
        opt.add(c.formula)
    assert opt.check() == sat

def test_s3(s3: Spec, opt):
    for c in s3.constraints:
        opt.add(c.formula)
    assert opt.check() == sat

