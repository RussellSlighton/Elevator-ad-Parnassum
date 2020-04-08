from src.constraints import *
from src.types import *

def __universalConstraints(gamutLength, line):
     return [
        pitchesWithinGamut(0, gamutLength, line),
        pitchesOnScale(line),
        conclusionSteps(line),
        hasClimaxPitch(line),
        conclusionIsInTriad(line),
    ]
def __universalMaximisations(gamutLength, line):
    return [uniquePitchCounts(0, gamutLength, line), steps(line)]

def __universalMinimisations(line):
    return [leaps(line)]

def __baseLineSpec(gamutLength, line):
    return Spec(line,
                __universalConstraints(gamutLength,line),
                __universalMaximisations(gamutLength, line),
                __universalMinimisations(line))

def cantusSpec(length, gamutLength, name):
    line = Line(length, "CF_" + name)
    spec = __baseLineSpec(gamutLength,line)
    spec.constraints +=[
        firstNoteIsTonic(line),
        conclusionIsTonic(line),
    ]

    return spec

def firstSpeciesSpec(cantusFirmus: Line, gamutLength, name):
    length = len(cantusFirmus)
    line = Line(length, "FirstSpecies_" + name)
    sm = makeSimMap([makeTemporalisedLine(cantusFirmus, NoteLength.WHOLE)],
                    makeTemporalisedLine(line, NoteLength.WHOLE))

    spec = __baseLineSpec(gamutLength, line)
    spec.constraints += [
        firstNoteAccompaniesCantusTonic(line),
        unisonOnlyBeginningAndEnd(sm),
        noDissonantIntervals(sm),
    ]

    return spec

def secondSpeciesSpec(cantusFirmus : Line, gamutLength, name):
    length = len(cantusFirmus) * 2
    line = Line(length, "SecondSpecies_" + name)
    sm = makeSimMap([makeTemporalisedLine(cantusFirmus, NoteLength.WHOLE)],
                    makeTemporalisedLine(line, NoteLength.HALF))

    spec = __baseLineSpec(gamutLength, line)
    spec.constraints += [
        firstNoteAccompaniesCantusTonic(line),
        unisonOnlyBeginningAndEnd(sm),
        noDissonantIntervals(sm)
    ]

    return spec

def thirdSpeciesSpec(cantusFirmus: Line, gamutLength, name):
    length = len(cantusFirmus) * 4
    line = Line(length, "ThirdSpecies_" + name)
    sm = makeSimMap([makeTemporalisedLine(cantusFirmus, NoteLength.WHOLE)],
                    makeTemporalisedLine(line, NoteLength.QUARTER))

    spec = __baseLineSpec(gamutLength, line)
    spec.constraints += [
        firstNoteAccompaniesCantusTonic(line),
        unisonOnlyBeginningAndEnd(sm),
        noDissonantIntervals(sm)
    ]

    return spec




