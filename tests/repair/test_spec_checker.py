import pytest
from src.repair.specChecker import *
from src.main import createFirstSpecies

@pytest.fixture
def goodCF():
    return [1, 3, 6, 7, 8, 5, 2, 1]

@pytest.fixture
def badCF():
    # does not end on tonic
    return [1, 3, 6, 7, 8, 5, 2, 3]

# GGG -> good cf, good s1, good s2, ...
# GBG -> good cf, bad s1, good s2,...
# ...
@pytest.fixture
def GGs1(goodCF):
    return [8, 7, 4, 5, 3, 2, 0, 1]

@pytest.fixture
def GBS1(goodCF):
    # all unisons
    return goodCF

@pytest.fixture
def BGS1(badCF):
    return [8, 7, 4, 5, 3, 2, 0, 1]

@pytest.fixture
def BBS1(badCF):
    # all unisons
    return badCF

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
