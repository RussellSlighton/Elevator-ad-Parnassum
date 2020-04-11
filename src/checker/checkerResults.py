from typing import List

class CheckerResult:
    def __init__(self, reasons : List[int]):
        self.reasons = reasons

    def isValid(self):
        return len(self.reasons) == 0

    def __repr__(self):
        if self.isValid():
            return "Line is valid"
        else:
            reason = "Line fails to satisfy the following properties: \n"
            for r in self.reasons:
                reason += "\t" + r +'\n'
            return reason