from src.lib.constraints.pitch import *
from src.lib.types2 import *

# Conclusion must be re-do or ti-do

def conclusionIsTonic(line: Line) -> Constraint:
    return Constraint(
        isUnison(ConstPitch(0), line[-1]),
        ConstraintType.CONCLUSION,
        "Conclusion should be tonic"
    )

def conclusionIsTonicOrOctave(line: Line) -> Constraint:
    formula = \
        Or(
            isUnison(ConstPitch(0), line[-1]),
            isOctave(ConstPitch(0), line[-1])
        )
    return Constraint(formula, ConstraintType.CONCLUSION, "Conclusion should be either the tonic or the octave")

def conclusionSteps(line) -> Constraint:
    return Constraint(
        isStep(line[-1], line[-2]),
        ConstraintType.CONCLUSION,
        "Second last note should be a step away from the conclusion (last note)"
    )

def conclusionIsInTriad(line) -> Constraint:
    return Constraint(
        isConsonant(ConstPitch(0), line[-1]),
        ConstraintType.CONCLUSION,
        "Conclusion must be consonant with the tonic"
    )
