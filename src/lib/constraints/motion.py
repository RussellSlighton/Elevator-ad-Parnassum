from src.lib.constraints.pitch import isStep, isLeap, isSkip
from src.lib.types2 import Line

def steps(line: Line):
    return [isStep(line[i], line[i + 1]) for i in range(0, len(line) - 1)]

def leaps(line: Line):
    return [isLeap(line[i], line[i + 1]) for i in range(0, len(line) - 1)]

def skips(line: Line):
    return [isSkip(line[i], line[i + 1]) for i in range(0, len(line) - 1)]
