from src.constraints.beginning import firstNoteIsTonic
from src.constraints.climax import hasClimaxPitch, climaxMax
from src.constraints.conclusion import conclusionSteps, conclusionIsTonicOrOctave, conclusionIsTonic, \
    conclusionIsInTriad
from src.constraints.gamut import maximisesUniquePitchCount, pitchesWithinGamut, pitchesOnScale
from src.constraints.motion import maximiseSteps, minimiseLeaps
from src.constraints.pitch import isIntervalOrSmaller, isIntervalOrLarger, isStep, isConsonant, isTriadic, isSixth, \
    isFifth, isFourth, isLeap, isNthInterval, isOctave, isSecond, isSeventh, isThird, isUnison, \
    isMotionUp, isMotionDown
from src.constraints.simultaneity import unisonOnlyBeginningAndEnd, noDissonantIntervals, avoidsFourths, isDissonant, \
    unaccentedPassingNotesMayBeDissonant, avoidsDissonance