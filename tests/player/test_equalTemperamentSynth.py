from src.player.equalTemperamentSynth import *

def test_semitones_away():
    away = [semitonesAway(note, 1) for note in range(-10, 11)]
    assert away == [-19, -17, -15, -13, -12, -10, -8, -7, -5, -3, -1, 0, 2, 4, 5, 7, 9, 11, 12, 14, 16]
    away = [semitonesAway(note, -1) for note in range(-10, 11)]
    assert away == [-15, -13, -12, -10, -8, -7, -5, -3, -1, 0, 2, 4, 5, 7, 9, 11, 12, 14, 16, 17, 19]
