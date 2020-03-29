from src.types.pitch.varPitch import VarPitch

class Line:
    def __init__(self, lineLength: int, name: str):
        self.lineLength = lineLength
        self.name = name
        self.pitches = [VarPitch(name + "_" + str(i)) for i in range(0, lineLength)]

    def __getitem__(self, item):
        return self.pitches[item]

    def __iter__(self):
        return (x for x in self.pitches)

    def __repr__(self):
        return str("name: " + repr(self.pitches))

    def __len__(self):
        return len(self.pitches)
