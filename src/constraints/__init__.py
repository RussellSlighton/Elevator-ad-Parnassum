from src.constraints.beginning import firstNoteIsTonic, firstNoteAccompaniesCantusTonic
from src.constraints.climax import hasClimaxPitch, climaxMax
from src.constraints.conclusion import conclusionSteps, conclusionIsTonicOrOctave, conclusionIsTonic, \
    conclusionIsInTriad
from src.constraints.distinctness import distinctFromExample
from src.constraints.gamut import uniquePitchCounts, pitchesWithinGamut, pitchesOnScale
from src.constraints.motion import steps, leaps, skips
from src.constraints.pitch import isIntervalOrSmaller, isIntervalOrLarger, isStep, isConsonant, isTriadic, isSixth, \
    isFifth, isFourth, isLeap, isNthInterval, isOctave, isSecond, isSeventh, isThird, isUnison, \
    isMotionUp, isMotionDown,pitchesLetterValueValid
from src.constraints.simultaneity import unisonOnlyBeginningAndEnd, noDissonantIntervals, fourths, \
    unaccentedPassingNotesMayBeDissonant, dissonances
