import pytest

from src.main import *
from src.player.player import playVoice, playPiece

@pytest.fixture
def opt():
    return Optimize()

@pytest.fixture
def l():
    return Line(2, "l")

@pytest.fixture
def length():
    return 8

@pytest.fixture
def gamutSize():
    return 20

@pytest.fixture
def cf(length, gamutSize):
    return createCantusFirmus(length, gamutSize)

@pytest.fixture
def s1(length, gamutSize):
    return createFirstSpecies(length, gamutSize)

@pytest.fixture
def s2(length, gamutSize):
    return createSecondSpecies(length, gamutSize)

@pytest.fixture
def s3(length, gamutSize):
    return createThirdSpecies(length, gamutSize)

def test_extract_voices(opt, l):
    opt.add(l[0] == ConstPitch(10))
    opt.add(l[1] == ConstPitch(20))
    v = extractVoice(opt, l)
    assert v == [10, 20]

def test_createCantusFirmus(cf, length, gamutSize):
    assert len(cf) == length
    for p in cf:
        assert p in range(0, gamutSize)
    print(cf)
    playVoice(cf)

def test_createFirstSpecies(cf, s1, length, gamutSize):
    assert len(s1[0]) == length
    assert len(s1[1]) == length
    for p in s1[1]:
        assert p in range(0, gamutSize)
    print(s1)
    playPiece([makeTemporalisedLine(x, NoteLength.WHOLE) for x in s1])

def test_createSecondSpecies(cf, s2, length, gamutSize):
    assert len(s2[0]) == length
    assert len(s2[1]) == length * 2
    for p in s2[1]:
        assert p in range(0, gamutSize)
    print(s2)
    playPiece([makeTemporalisedLine(s2[0], NoteLength.WHOLE), makeTemporalisedLine(s2[1], NoteLength.HALF)])

def test_createThirdSpecies(cf, s3, length, gamutSize):
    assert len(s3[0]) == length
    assert len(s3[1]) == length * 4
    for p in s3[1]:
        assert p in range(0, gamutSize)
    print(s3)
    playPiece([makeTemporalisedLine(s3[0], NoteLength.WHOLE), makeTemporalisedLine(s3[1], NoteLength.QUARTER)])

# def test_createThroughSecondSpecies(cf, length, gamutSize):
#     ls = createThroughSecond(length, gamutSize)
#     print(ls)
#     ls = [[x + 12 * i for x in ls[i]] for i in range(0, len(ls))]
#     print(ls)
#     playPiece([makeTemporalisedLine(ls[0], NoteLength.WHOLE), makeTemporalisedLine(ls[1], NoteLength.WHOLE),
#                makeTemporalisedLine(ls[2], NoteLength.HALF)])
#
# # def test_createThroughThirdSpecies(cf, length, gamutSize, tonicIndex):
# #     ls = createThroughThird(length, tonicIndex, gamutSize)
# #     print(ls)
# #     ls = [[x + 7 * i for x in ls[i]] for i in range(0, len(ls))]
# #     print(ls)
# #     playPiece([makeTemporalisedLine(ls[0], NoteLength.WHOLE), makeTemporalisedLine(ls[1], NoteLength.WHOLE),
# #                makeTemporalisedLine(ls[2], NoteLength.HALF), makeTemporalisedLine(ls[3], NoteLength.QUARTER)],
# #               tonicIndex)
