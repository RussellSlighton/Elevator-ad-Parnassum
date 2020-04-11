from pytest import fixture

from src.checker.checker import *
from src.lib.specs import *
from src.lib.types2 import Foundry, ConstPitch

@fixture
def maxCount():
    return 6

@fixture
def cantus():
    return cantusSpec(4,5, '')

@fixture
def highSpeciesGamut():
    return 13

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

### cf ###

def test_cfValidWorksOnValid(foundry, cantus):
    assert checkCF(foundry.applySpec(cantus).extractPitches(cantus.line)).isValid()

#TODO: NEED TO VALIDATE REASONS!
def test_cfValidWorksOnInvalid(foundry, cantus, maxCount):
    badSpecs = getAllBadSpecs(cantus, maxCount)
    for badSpec in badSpecs:
        foundry = Foundry(Optimize()).applySpec(badSpec)
        cantus = foundry.extractPitches(badSpec.line)
        assert checkCF(cantus).isValid() == False

### util ###

@fixture
def goodCF():
    return  [0,4,2,0]

@fixture
def badCF():
    return [0,2,2,0]

def test_goodCFIsGood(goodCF):
    assert checkCF(goodCF).isValid()

def test_badCFIsBad(badCF):
    assert not checkCF(badCF).isValid()

### s1 ###

@fixture
def s1GoodCF(goodCF, highSpeciesGamut):
    return firstSpeciesSpec([ConstPitch(x) for x in goodCF], highSpeciesGamut, '')

@fixture
def s1BadCF(badCF, highSpeciesGamut):
    return firstSpeciesSpec([ConstPitch(x) for x in badCF], highSpeciesGamut, '')

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

### s2 ###

@fixture
def s2GoodCF(goodCF, highSpeciesGamut):
    return secondSpeciesSpec([ConstPitch(x) for x in goodCF], highSpeciesGamut, '')

@fixture
def s2BadCF(badCF, highSpeciesGamut):
    return secondSpeciesSpec([ConstPitch(x) for x in badCF], highSpeciesGamut, '')

def test_goodCFIsS2Sat(s2GoodCF):
    foundry = Foundry(Optimize())
    foundry.applySpec(s2GoodCF)
    assert foundry.check() == sat

def test_badCFIsS2Sat(s2BadCF):
    foundry = Foundry(Optimize())
    foundry.applySpec(s2BadCF)
    assert foundry.check() == sat

def test_s2ValidWorksOnValidS2ValidCF(foundry, s2GoodCF, goodCF):
    checkS2(goodCF, foundry.applySpec(s2GoodCF).extractPitches(s2GoodCF.line)).isValid()

def test_s2ValidWorksOnValidS2InvalidCF(foundry, s2BadCF, badCF):
    assert checkS2(badCF, foundry.applySpec(s2BadCF).extractPitches(s2BadCF.line)).isValid()

@fixture
def s2MaxCounts(maxCount):
    # The s3 tests are really slow
    return int(maxCount / 2)

def test_s2ValidWorksOnInvalidS2BadCF(foundry, badCF, s2BadCF, s2MaxCounts):
    badSpecs = getAllBadSpecs(s2BadCF, s2MaxCounts)
    for badSpec in badSpecs:
        foundry = Foundry(Optimize()).applySpec(badSpec)
        s2BadCF = foundry.extractPitches(badSpec.line)
        assert checkS2(badCF, s2BadCF).isValid() == False

def test_s2ValidWorksOnInvalidS2GoodCF(foundry, goodCF, s2GoodCF, s2MaxCounts):
    badSpecs = getAllBadSpecs(s2GoodCF, s2MaxCounts)
    for badSpec in badSpecs:
        foundry = Foundry(Optimize()).applySpec(badSpec)
        s2GoodCF = foundry.extractPitches(badSpec.line)
        assert checkS2(goodCF, s2GoodCF).isValid() == False

### s3 ###

@fixture
def s3GoodCF(goodCF, highSpeciesGamut):
    return thirdSpeciesSpec([ConstPitch(x) for x in goodCF], highSpeciesGamut, '')

@fixture
def s3BadCF(badCF, highSpeciesGamut):
    return thirdSpeciesSpec([ConstPitch(x) for x in badCF], highSpeciesGamut, '')

def test_goodCFIsS3Sat(s3GoodCF):
    foundry = Foundry(Optimize())
    foundry.applySpec(s3GoodCF)
    assert foundry.check() == sat

def test_badCFIsS3Sat(s3BadCF):
    foundry = Foundry(Optimize())
    foundry.applySpec(s3BadCF)
    assert foundry.check() == sat

def test_s3ValidWorksOnValidS2ValidCF(foundry, s3GoodCF, goodCF):
    checkS3(goodCF, foundry.applySpec(s3GoodCF).extractPitches(s3GoodCF.line)).isValid()

def test_s3ValidWorksOnValidS2InvalidCF(foundry, s3BadCF, badCF):
    assert checkS3(badCF, foundry.applySpec(s3BadCF).extractPitches(s3BadCF.line)).isValid()

@fixture
def s3MaxCounts(s2MaxCounts):
    # The s3 tests are really slow
    return int(s2MaxCounts / 2)

def test_s3ValidWorksOnInvalidS3BadCF(foundry, badCF, s3BadCF, s3MaxCounts):
    badSpecs = getAllBadSpecs(s3BadCF, s3MaxCounts)
    for badSpec in badSpecs:
        foundry = Foundry(Optimize()).applySpec(badSpec)
        s3BadCF = foundry.extractPitches(badSpec.line)
        assert checkS3(badCF, s3BadCF).isValid() == False

def test_s3ValidWorksOnInvalidS3GoodCF(foundry, goodCF, s3GoodCF, s3MaxCounts):
    badSpecs = getAllBadSpecs(s3GoodCF, s3MaxCounts)
    for badSpec in badSpecs:
        foundry = Foundry(Optimize()).applySpec(badSpec)
        s3GoodCF = foundry.extractPitches(badSpec.line)
        assert checkS3(goodCF, s3GoodCF).isValid() == False

