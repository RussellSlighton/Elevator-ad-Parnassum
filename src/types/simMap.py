# Simultaneity register - tells when two notes occur at the same time

from typing import List, Dict, Any, Tuple, Set

from src.types.noteLength import NoteLength
from src.types.pitch import Pitch

TemporalisedLine = Tuple[List[Any], NoteLength]

def makeTemporalisedLine(line: List[Any], noteLength: NoteLength) -> TemporalisedLine:
    return (line, noteLength)

def __getPitches(tl: TemporalisedLine) -> List[Any]:
    return tl[0]

def __getNoteLength(tl: TemporalisedLine) -> NoteLength:
    return tl[1]

SimMap = Dict[Pitch, Set[Any]]

# Notice the use of sets - this stores only sim pitches, not sim notes!
def makeSimMap(oldLines: List[TemporalisedLine], newLine: TemporalisedLine) -> SimMap:
    simPitches = {}
    for oldLine in oldLines:
        assert __getNoteLength(oldLine) <= __getNoteLength(newLine)
        newNotesPerOldNote = int(__getNoteLength(newLine) / __getNoteLength(oldLine))
        assert len(__getPitches(newLine)) == len(__getPitches(oldLine)) * newNotesPerOldNote

        for i in range(0, len(__getPitches(oldLine))):
            start = i * newNotesPerOldNote
            end = start + newNotesPerOldNote
            for j in range(start, end):
                if __getPitches(newLine)[j] in simPitches:
                    simPitches[__getPitches(newLine)[j]].add(__getPitches(oldLine)[i])
                else:
                    simPitches[__getPitches(newLine)[j]] = {__getPitches(oldLine)[i]}
    return simPitches
