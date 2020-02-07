from src.constraints.pitch import *
from src.types import *

def hasClimaxPitch(tonicIndex: TonicIndex, line: Line):
    climaxPitch = Pitch(getName(line) + "_CP")
    return And(
        __climaxPitchIsHighestPitch(climaxPitch, line),
        isInTriad(tonicIndex, climaxPitch),
        __onlyOneNoteIsClimax(climaxPitch, line)
    )

# TODO: Check if this actually how you say "only one of"
def __onlyOneNoteIsClimax(climaxPitch: Pitch, line: Line):
    isClimax = [p == climaxPitch for p in line]
    climaxPitchCount = sum([If(ind, 1, 0) for ind in isClimax])
    return climaxPitchCount == 1

def __climaxPitchIsHighestPitch(climaxPitch: Pitch, pitches: Line):
    return And([(p <= climaxPitch) for p in pitches])
