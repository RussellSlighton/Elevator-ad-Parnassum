# from src.lib.player.player import *
#
# # Manual test
# def test_player():
#     v1 = makeTemporalisedLine(
#         [Interval.THIRD().semitoneDistance, Interval.FOURTH().semitoneDistance, Interval.FIFTH().semitoneDistance,
#          Interval.SIXTH().semitoneDistance, Interval.SEVENTH().semitoneDistance],
#         NoteLength.WHOLE)
#     v2 = makeTemporalisedLine(
#         [Interval.UNISON().semitoneDistance, Interval.FIFTH().semitoneDistance, Interval.SECOND().semitoneDistance,
#          Interval.SIXTH().semitoneDistance, Interval.THIRD().semitoneDistance, Interval.SEVENTH().semitoneDistance,
#          Interval.FOURTH().semitoneDistance, Interval.OCTAVE().semitoneDistance, Interval.FIFTH().semitoneDistance,
#          Interval.SECOND().semitoneDistance + Interval.OCTAVE().semitoneDistance], NoteLength.HALF)
#     vs = [v1, v2]
#     print(v1, v2)
#     # playVoice(getPitches(v1))
#     # playVoice(getPitches(v2))
#     playPiece(vs)
