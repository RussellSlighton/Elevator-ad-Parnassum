from src.constraints.pitch import *
from src.types2 import *

def hasClimaxPitch(line: Line) -> Constraint:
    climaxPitch = VarPitch(line.name + "_CP")
    formula =  And(
        __climaxPitchIsHighestPitch(climaxPitch, line),
        isConsonant(ConstPitch(0), climaxPitch),
        __onlyOneNoteIsClimax(climaxPitch, line)
    )
    return Constraint(formula, ConstraintType.CLIMAX, "Climax should be unique and consonant with the tonic")

def climaxMax(line: Line, maxPitch: Pitch) -> Constraint:
    climaxPitch = VarPitch(line.name + "_CP")
    formula =  Interval.between(climaxPitch, maxPitch) >= Interval.UNISON()
    return Constraint(formula, ConstraintType.CLIMAX, "Climax should be no greater than " + str(maxPitch.flattened()))


# TODO: Check if this actually how you say "only one of"
def __onlyOneNoteIsClimax(climaxPitch: Pitch, line: Line):
    isClimax = [p == climaxPitch for p in line]
    climaxPitchCount = sum([If(ind, 1, 0) for ind in isClimax])
    return climaxPitchCount == 1

def __climaxPitchIsHighestPitch(climaxPitch: Pitch, pitches: Line):
    return And([(p <= climaxPitch) for p in pitches])
