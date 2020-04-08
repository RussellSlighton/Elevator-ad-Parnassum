from src.types2.line import *

def test_line():
    l = Line(1, "L")
    assert l.lineLength == 1
    assert l.pitches == [VarPitch("L_0")]

def test_subscriptLine():
    l = Line(1, "L")
    assert l[0] == VarPitch("L_0")
