from src.repair.repair import *
from src.repair import *
from tests.repair.fixtureUtils import *

def dummyToMakeImportsNotSeemUseless():
    goodCF()

def test_revpowset():
    assert list(revpowset([1, 2])) == [(1, 2), (1,), (2,), ()]

def test_repairGoodCFDoesNothing(goodCF):
    assert repairCF(goodCF) == goodCF

def test_repairBadCFFixesMinimally(badCF, goodCF):
    assert repairCF(badCF) == goodCF

def test_repairGoodCfGoodS1DoesNothing(goodCF, GGs1):
    cf, s1 = repairS1(goodCF, GGs1)
    assert cf == goodCF
    assert s1 == GGs1

def test_repairGoodCfBadS1FixesF1(goodCF, GBS1):
    cf, s1 = repairS1(goodCF, GBS1)
    assert cf == goodCF
    assert s1Valid(cf,s1)

def test_repairBadCFGoodS1DoesNothing(badCF, BGS1):
    cf, s1 = repairS1(badCF, BGS1)
    assert cf == badCF
    assert s1 == BGS1

def test_repairBadCFBadS1FixesOnlyS1(prettyBadCF):
    cf, s1 = repairS1(prettyBadCF, prettyBadCF)
    assert cfValid(cf)
    assert s1Valid(cf,s1)

# TODO: Make sure this fails due to gamut stuff only!
def test_repairReallyBadCFCompletelyFails(reallyBadCF):
    assert repairCF(reallyBadCF) is None

def test_repairPrettyBadCFWorks(prettyBadCF):
    assert cfValid(repairCF(prettyBadCF))