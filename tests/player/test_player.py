from src.player.player import *

# Manual test
if __name__ == "__main__":
    v1 = makeTemporalisedLine([3, 4, 5, 6, 7], NoteLength.WHOLE)
    v2 = makeTemporalisedLine([1, 5, 2, 6, 3, 7, 4, 8, 5, 9], NoteLength.HALF)
    v3 = makeTemporalisedLine([8, 5, 9, 6, 10, 7, 11, 8, 12, 9, 8, 5, 9, 6, 10, 7, 11, 8, 12, 9], NoteLength.QUARTER)
    vs = [v1, v2, v3]
    playPiece(vs, 1)
