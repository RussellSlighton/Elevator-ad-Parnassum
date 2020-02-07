from math import floor

from pysine import sine

TONIC = 440  # A4
TWELFTH_ROOT_TWO = 1.059463094359
DIST_A4_C4 = 9

def synth(note, tonicIndex):
    return TONIC * TWELFTH_ROOT_TWO ** (semitonesAway(note, tonicIndex) - DIST_A4_C4)

def playNotes(notes, tonicIndex):
    freqs = [synth(n, tonicIndex) for n in notes]
    for f in freqs:
        sine(f, .2)

# TODO: This should be dep injected
# major
def __scalePositionToSemitones(pos):
    if pos == 0:
        return 0
    elif pos == 1:
        return 2
    elif pos == 2:
        return 4
    elif pos == 3:
        return 5
    elif pos == 4:
        return 7
    elif pos == 5:
        return 9
    elif pos == 6:
        return 11
    elif pos == 7:
        return 12
    else:
        raise ("Mistake in synth")

# Minor
# def __scalePositionToSemitones(pos):
#     if pos == 0:
#         return 0
#     elif pos == 1:
#         return 2
#     elif pos == 2:
#         return 3
#     elif pos == 3:
#         return 5
#     elif pos == 4:
#         return 7
#     elif pos == 5:
#         return 8
#     elif pos == 6:
#         return 11
#     elif pos == 7:
#         return 12
#     else:
#         raise ("Mistake in synth")

def semitonesAway(note, tonicIndex):
    scaledNote = __scalePositionToSemitones((note - tonicIndex) % 7)
    octavesAway = floor((note - tonicIndex) / 7)
    semitones = scaledNote + octavesAway * 12
    return semitones
