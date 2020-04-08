from pytest import fixture

from src.generator import Generator
from src.specs import cantusSpec

@fixture
def length():
    return 5
@fixture
def cfGen1(length):
    return Generator(cantusSpec(length,10, ''))

@fixture
def impossible():
    return Generator(cantusSpec(5,1,''))

def test_createNewCreates(cfGen1, length):
    assert len(cfGen1.createNew()) == length

def test_createNewCreatesDifferent(cfGen1):
    old = cfGen1.createNew()
    new = cfGen1.createNew()
    assert old != new

def test_createImpossibleReturnsEmpty(impossible):
    assert len(impossible.createNew()) == 0