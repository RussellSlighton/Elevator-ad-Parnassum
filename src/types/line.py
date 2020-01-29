from typing import List

from src.types.pitch import Pitch, makePitch

Line = List[Pitch]
TonicIndex = int

def makeLine(lineLength, name) -> Line:
    pitches = [makePitch(name + "_" + str(i)) for i in range(0, lineLength)]
    return pitches

def getName(line: Line):
    return str(line[0]).split("_")[0]
