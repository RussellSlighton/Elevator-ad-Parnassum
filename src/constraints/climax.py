from src.constraints.pitch import *
from src.types import *

def hasClimaxPitch(line: Line):
    climaxPitch = VarPitch(line.name + "_CP")
    return And(
        __climaxPitchIsHighestPitch(climaxPitch, line),
        isConsonant(ConstPitch(0), climaxPitch),
        __onlyOneNoteIsClimax(climaxPitch, line)
    )

def climaxMax(line: Line, maxPitch: Pitch):
    climaxPitch = VarPitch(line.name + "_CP")
    return Interval.between(climaxPitch, maxPitch) >= Interval.UNISON()

# TODO: Check if this actually how you say "only one of"
def __onlyOneNoteIsClimax(climaxPitch: Pitch, line: Line):
    isClimax = [p == climaxPitch for p in line]
    climaxPitchCount = sum([If(ind, 1, 0) for ind in isClimax])
    return climaxPitchCount == 1

def __climaxPitchIsHighestPitch(climaxPitch: Pitch, pitches: Line):
    return And([(p <= climaxPitch) for p in pitches])
