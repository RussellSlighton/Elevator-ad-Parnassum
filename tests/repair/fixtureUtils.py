import pytest

@pytest.fixture
def goodCF():
    return [1, 4, 5, 8, 6, 3, 2, 1]

@pytest.fixture
def badCF():
    # does not end on tonic
    return [1, 4, 5, 8, 6, 3, 2, 3]

@pytest.fixture
def reallyBadCF(badCF):
    return [1, 2, 1, 1]

@pytest.fixture
def prettyBadCF(badCF):
    return [1, 1, 3, 2, 2]

# GGG -> good cf, good s1, good s2, ...
# GBG -> good cf, bad s1, good s2,...
# ...
@pytest.fixture
def GGs1(goodCF):
    return [1, 2, 5, 6, 8, 7, 4, 3]

@pytest.fixture
def GBS1(goodCF):
    # all unisons
    return goodCF

@pytest.fixture
def BGS1(badCF):
    return [1, 2, 3, 6, 4, 5, 7, 8]

@pytest.fixture
def BBS1(badCF):
    # all unisons
    return badCF
