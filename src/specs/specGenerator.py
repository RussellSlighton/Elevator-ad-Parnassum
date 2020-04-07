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
    return [uniquePitchCounts(0, gamutLength, line)]

def __universalMinimisations(line):
    return [leaps(line)]

def __baseLineSpec(gamutLength, line):
    return Spec(__universalConstraints(gamutLength,line),
                __universalMaximisations(gamutLength, line),
                __universalMinimisations(line))

def cantusSpec(length, name, gamutLength):
    line = Line(length, "CF_" + name)
    spec = __baseLineSpec(gamutLength,line)
    spec.constraints +=[
        firstNoteIsTonic(line),
        conclusionIsTonic(line),
        climaxMax(line, ConstPitch(int(gamutLength)))
    ]

    return spec

def firstSpeciesSpec(cantusFirmus: Line, name, gamutLength):
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

def secondSpeciesSpec(cantusFirmus : Line, name, gamutLength):
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

def thirdSpeciesSpec(cantusFirmus: Line, name, gamutLength):
    length = len(cantusFirmus) * 4
    line = Line(length, "ThirdSpecies_" + name)
    sm = makeSimMap([makeTemporalisedLine(cantusFirmus, NoteLength.WHOLE)],
                    makeTemporalisedLine(line, NoteLength.Quarter))

    spec = __baseLineSpec(gamutLength, line)
    spec.constraints += [
        firstNoteAccompaniesCantusTonic(line),
        unisonOnlyBeginningAndEnd(sm),
        noDissonantIntervals(sm)
    ]

    return spec




