from pytest import fixture

from src.checker.checker import getGamutLength, Optimize, checkCF, sat, checkS1
from src.specs import cantusSpec, getAllBadSpecs, firstSpeciesSpec
from src.types2 import Foundry, ConstPitch

@fixture
def maxCount():
    return 20

@fixture
def cantus():
    return cantusSpec(4,5, '')

@fixture
def goodCF():
    return  [0,4,2,0]

@fixture
def badCF():
    return [0,2,2,0]

@fixture
def highSpeciesGamut():
    return 13

@fixture
def s1GoodCF(goodCF, highSpeciesGamut):
    return firstSpeciesSpec([ConstPitch(x) for x in goodCF], highSpeciesGamut, '')

@fixture
def s1BadCF(badCF, highSpeciesGamut):
    return firstSpeciesSpec([ConstPitch(x) for x in badCF], highSpeciesGamut, '')

@fixture
def finishedLineGamutSize():
    return 5

@fixture
def foundry():
    return Foundry(Optimize())

@fixture
def finishedLine(finishedLineGamutSize):
    return list(range(0, finishedLineGamutSize))

def test_getGamutLength(finishedLineGamutSize, finishedLine):
    assert getGamutLength(finishedLine) == finishedLineGamutSize

def test_cfValidWorksOnValid(foundry, cantus):
    assert checkCF(foundry.applySpec(cantus).extractPitches(cantus.line)).isValid()

#TODO: NEED TO VALIDATE REASONS!
def test_cfValidWorksOnInvalid(foundry, cantus, maxCount):
    badSpecs = getAllBadSpecs(cantus, maxCount)
    for badSpec in badSpecs:
        foundry = Foundry(Optimize()).applySpec(badSpec)
        cantus = foundry.extractPitches(badSpec.line)
        assert checkCF(cantus).isValid() == False

def test_goodCFIsGood(goodCF):
    assert checkCF(goodCF).isValid()

def test_badCFIsBad(badCF):
    assert not checkCF(badCF).isValid()

def test_goodCFIsS1Sat(s1GoodCF):
    foundry = Foundry(Optimize())
    foundry.applySpec(s1GoodCF)
    assert foundry.check() == sat

def test_badCFIsS1Sat(s1BadCF):
    foundry = Foundry(Optimize())
    foundry.applySpec(s1BadCF)
    assert foundry.check() == sat

def test_s1ValidWorksOnValidS1ValidCF(foundry, s1GoodCF, goodCF):
    checkS1(goodCF, foundry.applySpec(s1GoodCF).extractPitches(s1GoodCF.line)).isValid()

def test_s1ValidWorksOnValidS1InvalidCF(foundry, s1BadCF, badCF):
    print(s1BadCF.constraints)
    assert checkS1(badCF, foundry.applySpec(s1BadCF).extractPitches(s1BadCF.line)).isValid()

def test_s1ValidWorksOnInvalidS1BadCF(foundry, badCF, s1BadCF, maxCount):
    badSpecs = getAllBadSpecs(s1BadCF, maxCount)
    for badSpec in badSpecs:
        foundry = Foundry(Optimize()).applySpec(badSpec)
        s1BadCF = foundry.extractPitches(badSpec.line)
        assert checkS1(badCF, s1BadCF).isValid() == False

def test_s1ValidWorksOnInvalidS1GoodCF(foundry, goodCF, s1GoodCF, maxCount):
    badSpecs = getAllBadSpecs(s1GoodCF, maxCount)
    for badSpec in badSpecs:
        foundry = Foundry(Optimize()).applySpec(badSpec)
        s1GoodCF = foundry.extractPitches(badSpec.line)
        assert checkS1(goodCF, s1GoodCF).isValid() == False