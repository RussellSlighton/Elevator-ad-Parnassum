from pytest import fixture

from src.generator import Generator
from src.specs import cantusSpec

@fixture
def length():
    return 4

@fixture
def cfGen1(length):
    return Generator(cantusSpec(length, 13, ''))

@fixture
def impossible(length):
    return Generator(cantusSpec(length, 1, ''))

def test_createNewCreates(cfGen1, length):
    assert len(cfGen1.createNew()) == length

def test_createNewCreatesDifferent(cfGen1):
    old = cfGen1.createNew()
    new = cfGen1.createNew()
    assert old != new

def test_createImpossibleReturnsEmpty(impossible):
    assert len(impossible.createNew()) == 0
