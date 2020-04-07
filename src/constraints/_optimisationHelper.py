from z3 import *

def maximise(opt: Optimize, indicators) -> None:
    count = sum([If(ind, 1, 0) for ind in indicators])
    opt.maximize(count)

def minimise(opt: Optimize, indicators) -> None:
    count = sum([If(ind, 1, 0) for ind in indicators])
    opt.minimize(count)
