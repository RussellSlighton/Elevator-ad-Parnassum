# Simultaneity register - tells when two notes occur at the same time

from src.types.temporalisedLine import *

#TODO: Replace this structure with more sane varient - just return a set...
# Also, refactor out the slotting functionality to a slotmap.

SimMap = Dict[Any, Set[Any]]

# Notice the use of sets - this stores only sim pitches, not sim notes!
def makeSimMap(oldLines: List[TemporalisedLine], newLine: TemporalisedLine) -> SimMap:
    simPitches = {}
    for oldLine in oldLines:
        assert getNoteLength(oldLine) <= getNoteLength(newLine)
        newNotesPerOldNote = int(getNoteLength(newLine) / getNoteLength(oldLine))
        if not (len(getPitches(newLine)) == len(getPitches(oldLine)) * newNotesPerOldNote):
            print("new line len: " + str(len(getPitches(newLine))) + " old line len: " + str(
                len(getPitches(oldLine))) + " new notes per old note: " + str(newNotesPerOldNote))
            assert False

        for i in range(0, len(getPitches(oldLine))):
            start = i * newNotesPerOldNote
            end = start + newNotesPerOldNote
            for j in range(start, end):
                if getPitches(newLine)[j] in simPitches:
                    simPitches[getPitches(newLine)[j]].add(getPitches(oldLine)[i])
                else:
                    simPitches[getPitches(newLine)[j]] = {getPitches(oldLine)[i]}
    return simPitches
