from src.constraints.pitch import *
from src.types import *

# Conclusion must be re-do or ti-do
def conclusionIsTonic(tonicIndex: TonicIndex, line: Line):
    return isUnison(tonicIndex, line[-1])

def conclusionIsTonicOrOctave(tonicIndex, line: Line):
    return \
        Or(
            isUnison(tonicIndex, line[-1]),
            isOctave(tonicIndex, line[-1])
        )

def conclusionSteps(line):
    return isStep(line[-1], line[-2])
