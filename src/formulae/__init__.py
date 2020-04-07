from src.formulae.beginning import firstNoteIsTonic
from src.formulae.climax import hasClimaxPitch, climaxMax
from src.formulae.conclusion import conclusionSteps, conclusionIsTonicOrOctave, conclusionIsTonic, \
    conclusionIsInTriad
from src.formulae.gamut import maximisesUniquePitchCount, pitchesWithinGamut, pitchesOnScale
from src.formulae.motion import maximiseSteps, minimiseLeaps
from src.formulae.pitch import isIntervalOrSmaller, isIntervalOrLarger, isStep, isConsonant, isTriadic, isSixth, \
    isFifth, isFourth, isLeap, isNthInterval, isOctave, isSecond, isSeventh, isThird, isUnison, \
    isMotionUp, isMotionDown
from src.formulae.simultaneity import unisonOnlyBeginningAndEnd, noDissonantIntervals, avoidsFourths, isDissonant, \
    unaccentedPassingNotesMayBeDissonant, avoidsDissonance
