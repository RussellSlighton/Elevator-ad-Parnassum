from pytest import fixture

from src.generator.gui import GUI

@fixture
def goodLength():
    return 4

@fixture
def goodGamut():
    return 13

@fixture
def badGamut():
    return 1

@fixture
def gui():
    return GUI()

@fixture
def cf(goodLength):
    return [0] * goodLength

def test_createNewCreates(gui, goodLength, goodGamut, cf):
    assert len(gui.createNew('cf',goodLength, goodGamut, cf)) == goodLength

def test_createNewOnSameCreatesDifferent(gui, goodGamut, goodLength, cf):
    old = gui.createNew('cf',goodLength, goodGamut, cf)
    new = gui.createNew('cf',goodLength, goodGamut, cf)
    assert old != new

def test_createImpossibleReturnsEmpty(gui, goodLength, badGamut, cf):
    assert len(gui.createNew('cf', goodLength, badGamut, cf)) == 0

def test_createHigherSpecies(gui, goodLength, goodGamut, badGamut, cf):
    old = gui.createNew('s1',goodLength, goodGamut, cf)
    new = gui.createNew('s1',goodLength, goodGamut, cf)
    assert len(old) == goodLength
    assert old != new
    assert len(gui.createNew('cf', goodLength, badGamut, cf)) == 0

