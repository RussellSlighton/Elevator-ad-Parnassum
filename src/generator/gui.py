from typing import Dict

from src.generator import Generator
from src.specs import *
from src.types import ConstPitch

class GUI:
    def __init__(self):
        self.generators = {}

    def createNew(self, species, length, gamutLength, cf):
        if species == cf:
            cf = ()
        cf = tuple(cf)

        key = (species, length, gamutLength, cf)
        if key in self.generators:
            return self.generators[key].createNew()
        else:
            if species == 'cf':
                g = Generator(cantusSpec(length, gamutLength, 'cf'))
            elif species == 's1':
                g = Generator(firstSpeciesSpec([ConstPitch(x) for x in cf], gamutLength, 's1'))
            elif species == 's2':
                g = Generator(secondSpeciesSpec([ConstPitch(x) for x in cf], gamutLength, 's2'))
            else:
                g = Generator(thirdSpeciesSpec([ConstPitch(x) for x in cf], gamutLength, 's3'))

            self.generators[key] = g
            return g.createNew()