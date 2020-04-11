from pytest import fixture

from src.checker import CheckerResult

@fixture
def validCheckResult():
    return CheckerResult([])

@fixture
def invalidReasons():
    return ['a', 'b']
@fixture
def invalidCheckResult(invalidReasons):
    return CheckerResult(invalidReasons)

def test_ConstructorForValidResult(validCheckResult):
    assert validCheckResult.isValid() == True
    assert validCheckResult.reasons == []

def test_ConstructorForInvalidResult(invalidCheckResult, invalidReasons):
    assert invalidCheckResult.isValid() == False
    assert invalidCheckResult.reasons == invalidReasons

def test_reprForValid(validCheckResult):
    assert str(validCheckResult) == "Line is valid"

def test_reprForInvalid(invalidCheckResult):
    assert str(invalidCheckResult) == "Line fails to satisfy the following properties: \n\ta\n\tb\n"
