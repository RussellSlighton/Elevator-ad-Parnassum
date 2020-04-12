from pytest import fixture

from src.checker.checker import checkCF, checkS3, checkS2, checkS1, Optimize, sat
from src.lib import makeSimMap, makeTemporalisedLine, NoteLength
from src.lib.specs import *
from src.lib.types2 import Foundry, ConstPitch
from src.repairer import repairCF, repairS2, repairS3, repairS1
from src.repairer.repairer import smartRepairLine

@fixture
def cantusGamut():
    return 5

@fixture
def cantus(cantusGamut):
    return cantusSpec(5,cantusGamut, '')


@fixture
def workingCF(cantus):
    f = Foundry(Optimize())
    f.applySpec(cantus)
    return f.extractPitches(cantus.line)

def test_beginningFailure(workingCF, cantus, cantusGamut):
    workingCF[0] = 2
    assert checkCF(workingCF).reasons[0].split(':')[0].split('.')[1] == "BEGINNING"
    symCF = [ConstPitch(x) for x in workingCF]
    sm = makeSimMap([makeTemporalisedLine(workingCF, NoteLength.WHOLE)],
                    makeTemporalisedLine(workingCF, NoteLength.WHOLE))
    x = smartRepairLine(symCF, cantus, checkCF(workingCF), cantusGamut, sm)
    assert x is not None
    assert checkCF(x).isValid()

def test_conclusionFailure(workingCF, cantus, cantusGamut):
    workingCF[-1] = 2
    assert checkCF(workingCF).reasons[0].split(':')[0].split('.')[1] == "CONCLUSION"
    symCF = [ConstPitch(x) for x in workingCF]
    sm = makeSimMap([makeTemporalisedLine(symCF, NoteLength.WHOLE)],
                    makeTemporalisedLine(symCF, NoteLength.WHOLE))
    x = smartRepairLine(symCF, cantus, checkCF(workingCF), cantusGamut, sm)
    assert x is not None
    assert checkCF(x).isValid()

def test_climaxFailure(workingCF, cantus, cantusGamut):
    workingCF[2] = max(workingCF)
    workingCF[1] = max(workingCF)
    assert checkCF(workingCF).reasons[0].split(':')[0].split('.')[1] == "CLIMAX"
    symCF = [ConstPitch(x) for x in workingCF]
    sm = makeSimMap([makeTemporalisedLine(symCF, NoteLength.WHOLE)],
                    makeTemporalisedLine(symCF, NoteLength.WHOLE))
    x = smartRepairLine(symCF, cantus, checkCF(workingCF), cantusGamut, sm)
    assert x is not None
    assert checkCF(x).isValid()

def test_gamutFailure(workingCF, cantus, cantusGamut):
    workingCF[2] = 1
    assert checkCF(workingCF).reasons[0].split(':')[0].split('.')[1] == "GAMUT"
    symCF = [ConstPitch(x) for x in workingCF]
    sm = makeSimMap([makeTemporalisedLine(symCF, NoteLength.WHOLE)],
                    makeTemporalisedLine(symCF, NoteLength.WHOLE))
    x = smartRepairLine(symCF, cantus, checkCF(workingCF), cantusGamut, sm)
    assert x is not None
    assert checkCF(x).isValid()


def test_SimFailure(workingCF):
    cf = workingCF
    s1 = workingCF.copy()
    s1[1] = s1[1] + 11 #seventh
    assert checkS1(cf, s1).reasons[0].split(':')[0].split('.')[1] == "SIMULTANEITY"
    symCF = [ConstPitch(x) for x in cf]
    symS1 = [ConstPitch(x) for x in s1]
    sm = makeSimMap([makeTemporalisedLine(symCF, NoteLength.WHOLE)],
                    makeTemporalisedLine(symS1, NoteLength.WHOLE))
    x = smartRepairLine(symS1, firstSpeciesSpec(symCF, 20, ''), checkS1(cf, s1), 13, sm)
    assert x is not None
    assert checkS1(cf,x).isValid()


@fixture
def maxCount():
    return 6

@fixture
def highSpeciesGamut():
    return 13

@fixture
def finishedLineGamutSize():
    return 5

@fixture
def foundry():
    return Foundry(Optimize())

### cf ###

def test_repairGoodCFDoesNothing(foundry, cantus, cantusGamut):
    res = foundry.applySpec(cantus).extractPitches(cantus.line)
    assert res == repairCF(res, cantusGamut)

def test_repairCFWorksOnBrokenCF(foundry, cantus, maxCount, cantusGamut):
    badSpecs = getAllBadSpecs(cantus, maxCount)
    for badSpec in badSpecs:
        foundry = Foundry(Optimize()).applySpec(badSpec)
        cantus = foundry.extractPitches(badSpec.line)
        assert checkCF(repairCF(cantus, cantusGamut)).isValid()

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

def test_repairS1WithGoodCFDoesNoting(foundry, s1GoodCF, goodCF):
    res = foundry.applySpec(s1GoodCF).extractPitches(s1GoodCF.line)
    assert res == repairS1(goodCF, res, max(res)+1)

def test_repairS1WithBadCFDoesNoting(foundry, s1BadCF, badCF):
    res = foundry.applySpec(s1BadCF).extractPitches(s1BadCF.line)
    assert res == repairS1(badCF, res, max(res)+1)

def test_repairS1WorksFromBadCF(foundry, badCF, s1BadCF, maxCount, highSpeciesGamut):
    badSpecs = getAllBadSpecs(s1BadCF, maxCount)
    for badSpec in badSpecs:
        foundry = Foundry(Optimize()).applySpec(badSpec)
        s1BadCF = foundry.extractPitches(badSpec.line)
        assert checkS1(badCF, repairS1(badCF, s1BadCF, highSpeciesGamut)).isValid() == True

def test_repairS1WorksFromGoodCF(foundry, goodCF, s1GoodCF, maxCount, highSpeciesGamut):
    badSpecs = getAllBadSpecs(s1GoodCF, maxCount)
    for badSpec in badSpecs:
        foundry = Foundry(Optimize()).applySpec(badSpec)
        s1GoodCF = foundry.extractPitches(badSpec.line)
        assert checkS1(goodCF, repairS1(goodCF, s1GoodCF, highSpeciesGamut)).isValid() == True

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

def test_repairS2WithGoodCFDoesNoting(foundry, s2GoodCF, goodCF):
    res = foundry.applySpec(s2GoodCF).extractPitches(s2GoodCF.line)
    assert res == repairS2(goodCF, res, max(res)+1)

def test_repairS2WithBadCFDoesNoting(foundry, s2BadCF, badCF):
    res = foundry.applySpec(s2BadCF).extractPitches(s2BadCF.line)
    assert res == repairS2(badCF, res, max(res)+1)

@fixture
def s2MaxCounts(maxCount):
    # The s3 tests are really slow
    return int(maxCount / 2)

def test_repairS2WorksFromBadCF(foundry, badCF, s2BadCF, s2MaxCounts, highSpeciesGamut):
    badSpecs = getAllBadSpecs(s2BadCF, s2MaxCounts)
    for badSpec in badSpecs:
        foundry = Foundry(Optimize()).applySpec(badSpec)
        s2BadCF = foundry.extractPitches(badSpec.line)
        assert checkS2(badCF, repairS2(badCF, s2BadCF, highSpeciesGamut)).isValid() == True

def test_repairS2WorksFromGoodCF(foundry, goodCF, s2GoodCF, s2MaxCounts, highSpeciesGamut):
    badSpecs = getAllBadSpecs(s2GoodCF, s2MaxCounts)
    for badSpec in badSpecs:
        foundry = Foundry(Optimize()).applySpec(badSpec)
        s2GoodCF = foundry.extractPitches(badSpec.line)
        assert checkS2(goodCF, repairS2(goodCF, s2GoodCF, highSpeciesGamut)).isValid() == True

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

def test_repairS3WithGoodCFDoesNoting(foundry, s3GoodCF, goodCF):
    res = foundry.applySpec(s3GoodCF).extractPitches(s3GoodCF.line)
    assert res == repairS3(goodCF, res, max(res)+1)

def test_repairS3WithBadCFDoesNoting(foundry, s3BadCF, badCF):
    res = foundry.applySpec(s3BadCF).extractPitches(s3BadCF.line)
    assert res == repairS3(badCF, res, max(res)+1)

@fixture
def s3MaxCounts(s2MaxCounts):
    # The s3 tests are really slow
    return 1

#too slow :(
# def test_repairS3WorksFromBadCF(foundry, badCF, s3BadCF, s3MaxCounts, highSpeciesGamut):
#     badSpecs = getAllBadSpecs(s3BadCF, s3MaxCounts)
#     for badSpec in badSpecs:
#         foundry = Foundry(Optimize()).applySpec(badSpec)
#         s3BadCF = foundry.extractPitches(badSpec.line)
#         assert checkS3(badCF, repairS3(badCF, s3BadCF, highSpeciesGamut)).isValid() == True
#
# def test_repairS3WorksFromGoodCF(foundry, goodCF, s3GoodCF, s3MaxCounts, highSpeciesGamut):
#     badSpecs = getAllBadSpecs(s3GoodCF, s3MaxCounts)
#     for badSpec in badSpecs:
#         foundry = Foundry(Optimize()).applySpec(badSpec)
#         s3GoodCF = foundry.extractPitches(badSpec.line)
#         assert checkS3(goodCF, repairS3(goodCF, s3GoodCF, highSpeciesGamut)).isValid() == True

