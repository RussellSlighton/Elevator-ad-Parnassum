import pytest
from z3 import Int

from src.types.line import *

def test_line():
    l = Line(1, "L")
    assert l.lineLength == 1
    assert l.pitches == [Pitch("L_0")]

def test_subscriptLine():
    l = Line(1, "L")
    assert l[0] == Pitch("L_0")