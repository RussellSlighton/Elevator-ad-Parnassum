from src.formulae.pitch import *
from src.types import *

# Conclusion must be re-do or ti-do
def conclusionIsTonic(line: Line):
    return isUnison(ConstPitch(0), line[-1])

def conclusionIsTonicOrOctave(line: Line):
    return \
        Or(
            isUnison(ConstPitch(0), line[-1]),
            isOctave(ConstPitch(0), line[-1])
        )

def conclusionSteps(line):
    return isStep(line[-1], line[-2])

def conclusionIsInTriad(line):
    return isConsonant(ConstPitch(0), line[-1])
