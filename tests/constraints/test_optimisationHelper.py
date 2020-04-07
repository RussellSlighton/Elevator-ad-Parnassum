from src.formulae._optimisationHelper import *

def test_maximise():
    opt = Optimize()
    a = Bool('a')
    b = Bool('b')
    maximise(opt, [a, b])
    assert opt.check() == sat
    ps = [opt.model()[p] for p in [a, b]]
    assert ps == [True, True]

def test_minimise():
    opt = Optimize()
    a = Bool('a')
    b = Bool('b')
    minimise(opt, [a, b])
    assert opt.check() == sat
    ps = [opt.model()[p] for p in [a, b]]
    assert ps == [False, False]
