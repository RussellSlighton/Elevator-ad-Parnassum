from pytest import fixture
from z3 import Int

from src.specs import *
from src.types import *

@fixture
def cons():
    return [Constraint(Int('x') == 1, ConstraintType.MISC, 'bla')]

@fixture
def mini():
    return [1,2]

@fixture
def maxi():
    return [3]

@fixture
def spec(cons, mini, maxi):
    return Spec(cons, maxi, mini)

def test_specConstruction(spec, cons, mini, maxi):
    assert spec.constraints == cons
    assert spec.maximisations == maxi
    assert spec.minimisations == mini