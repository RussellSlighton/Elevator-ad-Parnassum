from pysine import sine

TONIC = 440  # A4
TWELTH_ROOT_TWO = 1.059463094359
DIST_A4_C4 = 9

def synth(note, tonicIndex):
    return TONIC * TWELTH_ROOT_TWO ** (semitonesAway(note, tonicIndex) - DIST_A4_C4)

def playNotes(notes, tonicIndex):
    freqs = [synth(n, tonicIndex) for n in notes]
    for f in freqs:
        sine(f, .2)

def semitonesAway(note, tonicIndex):
    scaledNote = (note - tonicIndex) + 1
    if scaledNote == 0:
        return -1
    elif scaledNote == 1:
        return 0
    elif scaledNote == 2:
        return 2
    elif scaledNote == 3:
        return 4
    elif scaledNote == 4:
        return 5
    elif scaledNote == 5:
        return 7
    elif scaledNote == 6:
        return 9
    elif scaledNote == 7:
        return 11
    elif scaledNote == 8:
        return 12
    else:
        raise ("Gamut size not supported by player")
