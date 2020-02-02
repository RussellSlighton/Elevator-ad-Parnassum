# Simultaneity register - tells when two notes occur at the same time

from src.types.temporalisedLine import *

SimMap = Dict[Any, Set[Any]]

# Notice the use of sets - this stores only sim pitches, not sim notes!
def makeSimMap(oldLines: List[TemporalisedLine], newLine: TemporalisedLine) -> SimMap:
    simPitches = {}
    for oldLine in oldLines:
        assert getNoteLength(oldLine) <= getNoteLength(newLine)
        newNotesPerOldNote = int(getNoteLength(newLine) / getNoteLength(oldLine))
        assert len(getPitches(newLine)) == len(getPitches(oldLine)) * newNotesPerOldNote

        for i in range(0, len(getPitches(oldLine))):
            start = i * newNotesPerOldNote
            end = start + newNotesPerOldNote
            for j in range(start, end):
                if getPitches(newLine)[j] in simPitches:
                    simPitches[getPitches(newLine)[j]].add(getPitches(oldLine)[i])
                else:
                    simPitches[getPitches(newLine)[j]] = {getPitches(oldLine)[i]}
    return simPitches