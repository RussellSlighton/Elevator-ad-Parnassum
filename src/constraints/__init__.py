from src.constraints.beginning import firstNoteIsTonic
from src.constraints.climax import hasClimaxPitch
from src.constraints.conclusion import conclusionSteps, conclusionIsTonicOrOctave, conclusionIsTonic
from src.constraints.gamut import maximisesUniquePitchCount, pitchesWithinGamut
from src.constraints.motion import maximiseSteps, minimiseLeaps
from src.constraints.pitch import isIntervalOrSmaller, isIntervalOrLarger, isStep, isConsonant, isTriadic, \
    isPalestrinaPerfect, isSixth, isFifth, isFourth, isLeap, isNApart, isOctave, isSecond, isSeventh, isThird, isUnison, \
    isMotionUp, isMotionDown
