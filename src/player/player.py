from typing import List

from synthesizer import Player, Synthesizer, Waveform

from src.player.equalTemperamentSynth import *
from src.types import *
from src.types.temporalisedLine import asUniqueValues

def playPiece(lines: List[TemporalisedLine], tonicIndex):
    mapping, indexLines = asUniqueValues(lines)

    lowerLines = indexLines[0:-1]
    upperLine = indexLines[-1]

    sm = makeSimMap(lowerLines, upperLine)

    player = Player()
    player.open_stream()
    synthesizer = Synthesizer(osc1_waveform=Waveform.sine, osc1_volume=1.0, use_osc2=False)

    for k in upperLine[0]:
        print(mapping[k])
        toPlay = [synth(mapping[n], tonicIndex) for n in sm[k].union([k])]
        print([mapping[n] for n in list(sm[k].union([k]))])
        print(toPlay)
        player.play_wave(synthesizer.generate_chord([n for n in toPlay], 1))

def playVoice(notes, tonicIndex):
    player = Player()
    player.open_stream()
    synthesizer = Synthesizer(osc1_waveform=Waveform.sine, osc1_volume=1.0, use_osc2=False)

    for note in notes:
        player.play_wave(synthesizer.generate_constant_wave(synth(note, tonicIndex), .3))
