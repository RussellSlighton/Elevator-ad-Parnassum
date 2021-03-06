from z3 import Optimize

from src.lib.constraints import distinctFromExample
from src.lib.types2 import Foundry, Spec, ConstPitch

# creates new examples of a given spec - species, length, gamutlength ... (all parameters fixed)
class Generator():
    def __init__(self, spec: Spec):
        self.foundry = Foundry(Optimize())
        self.foundry.applySpec(spec)
        self.spec = spec

    def createNew(self):
        try:
            pitches = self.foundry.extractPitches(self.spec.line)
        except Exception:
            return []
        self.foundry.apply(distinctFromExample(self.spec.line, [ConstPitch(x) for x in pitches]))
        return pitches
