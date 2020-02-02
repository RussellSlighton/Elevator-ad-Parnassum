from typing import *

from src.types.noteLength import NoteLength

TemporalisedLine = Tuple[List[Any], NoteLength]

def makeTemporalisedLine(line: List[Any], noteLength: NoteLength) -> TemporalisedLine:
    return (line, noteLength)

def getPitches(tl: TemporalisedLine) -> List[Any]:
    return tl[0]

def getNoteLength(tl: TemporalisedLine) -> NoteLength:
    return tl[1]

def asUniqueValues(lines: List[TemporalisedLine]):
    uuid = 0
    mapping = {}
    indexLines = []
    for line in lines:
        curLine = []
        for note in getPitches(line):
            curLine.append(uuid)
            mapping[uuid] = note
            uuid += 1
        indexLines.append(tuple([curLine, getNoteLength(line)]))
    # mapping is how you get out the original values
    return mapping, indexLines
