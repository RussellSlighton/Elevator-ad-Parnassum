import pytest

from src.repair.util import *
from src.types import pitch

@pytest.fixture
def cf():
    return [1, 2, 3]

@pytest.fixture
def s1():
    return [1, 2, 3]

# Need to actually test if this produces a cf...
def test_cf_spec(cf):
    cfs = cfSpec(cf)
    assert type(cfs[0]) == type(Optimize())
    assert type(cfs[1][0]) == type(pitch(''))

def test_s1_spec(cf, s1):
    s1s = s1Spec(cf, s1)
    assert type(s1s[0]) == type(Optimize())
    assert type(s1s[1][0]) == type(pitch(''))
