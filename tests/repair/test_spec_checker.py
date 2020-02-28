from src.repair.specChecker import *
from tests.repair.fixtureUtils import *

def dummyToMakeImportsNotSeemUseless():
    goodCF()

def test_CFValidWorksOnValid(goodCF):
    assert cfValid(goodCF), "goodCF0 should be valid"

def test_CFValidFailsOnInvalid(badCF):
    assert not cfValid(badCF), "badCF0 should be invalid"

def test_s1ValidWorksOnCorrectCFAndS1(goodCF, GGs1):
    assert s1Valid(goodCF, GGs1)

def test_s1ValidFailsOnCorrectCFAndInvalidS1(goodCF, GBS1):
    assert not s1Valid(goodCF, GBS1)

def test_s1ValidWorksOnIncorrectCFAndValidS1(badCF, BGS1):
    assert s1Valid(badCF, BGS1)

def test_s1ValidFailsOnIncorrectCFAndInvalidS1(badCF, BBS1):
    assert not s1Valid(badCF, BBS1)
