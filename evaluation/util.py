from interruptingcow import timeout
from timeit import default_timer as timer

def timeWithTimeout(function, time):
    try:
        with timeout(time, exception=RuntimeError):
            start = timer()
            output = function()
            end = timer()
            timeTaken = end - start
            return output, timeTaken
    except RuntimeError:
        return None,None