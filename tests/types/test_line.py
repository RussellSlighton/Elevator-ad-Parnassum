import pytest
from z3 import Int

from src.types.line import *

@pytest.fixture
def line():
    return [Int("L_0")]

def test_constructor(line):
    assert makeLine(1, "L") == line

def test_getName(line):
    assert getName(line) == "L"
