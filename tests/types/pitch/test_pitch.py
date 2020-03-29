from pytest import fixture
from z3 import Int

from src.types import *

@fixture
def variablePitch():
    return Pitch(Int("a"), Int('b'))

@fixture
def constantPitch():
    return Pitch(1, 2)

def test_VariableConstructor(variablePitch):
    assert variablePitch.letter == Int('a')
    assert variablePitch.octave == Int('b')

def test_ConstantConstructor(constantPitch):
    assert constantPitch.octave == 2
    assert constantPitch.letter == 1

def test_flattened(constantPitch):
    assert constantPitch.flattened() == 25

def test_equality(variablePitch, constantPitch):
    assert constantPitch == constantPitch
    assert variablePitch == variablePitch
    assert not constantPitch == Pitch(constantPitch.letter + 1, constantPitch.octave)

def test_ne(variablePitch, constantPitch):
    assert not constantPitch != constantPitch
    assert constantPitch != Pitch(constantPitch.letter + 1, constantPitch.octave)

def test_lte(constantPitch):
    assert True == (constantPitch <= constantPitch)
    assert constantPitch <= Pitch(constantPitch.letter + 1, constantPitch.octave)
    assert not Pitch(constantPitch.letter + 1, constantPitch.octave) <= constantPitch

def test_lt(constantPitch):
    assert not constantPitch < constantPitch
    assert constantPitch < Pitch(constantPitch.letter + 1, constantPitch.octave)
    assert not Pitch(constantPitch.letter + 1, constantPitch.octave) < constantPitch

def test_repr(constantPitch):
    assert str(constantPitch) == 'P(1,2)'
