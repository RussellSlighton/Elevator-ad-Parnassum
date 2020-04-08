from pytest import fixture
from z3 import Optimize, sat, unsat

from src.constraints import distinctFromExample
from src.types import Line, ConstPitch

@fixture
def example():
    return [ConstPitch(1),ConstPitch(2),ConstPitch(3)]

@fixture
def line():
    return Line(3,"")

@fixture
def opt():
    return Optimize()


def test_distinctnessIsSatisfiable(example, line, opt):
    opt.add(distinctFromExample(line, example).formula)
    assert opt.check() == sat

def test_distinctnessAllowsSomeSimilarily(example, line, opt):
    opt.add(distinctFromExample(line, example).formula)
    opt.add(line[0] == example[0])
    opt.add(line[1] == example[1])
    assert opt.check() == sat

def test_distinctnessDisallowsIdentity(example, line, opt):
    opt.add(distinctFromExample(line, example).formula)
    opt.add(line[0] == example[0])
    opt.add(line[1] == example[1])
    opt.add(line[2] == example[2])
    assert opt.check() == unsat
