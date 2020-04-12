import sys

from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QHBoxLayout, QLineEdit, QLabel, QMessageBox

from src import playVoice, playPiece
from src.generator import Generator
from src.lib.specs import *
from src.lib.types2 import ConstPitch, makeTemporalisedLine, NoteLength

class GUI:
    def __init__(self):
        print("Generator GUI starting")
        self.creator = Creator()

        self.window = QWidget()
        self.window.setWindowTitle("Generator")
        self.outerLayout = QHBoxLayout()

        ###

        self.optionsLayout = QVBoxLayout()

        self.cfCurrentLabel = QLabel("Current CF")
        self.cfCurrentLabelSubtitle = QLabel("Denotes semitones from root, note only major keys supported")
        font = self.cfCurrentLabel.font()
        font.setPointSize(font.pointSize()/1.4)
        self.cfCurrentLabelSubtitle.setFont(font)
        self.cfCurrentTextBox = QLineEdit()
        self.cfCurrentTextBox.setText("12,11,12,9,11,7,9,9")
        self.optionsLayout.addWidget(self.cfCurrentLabel)
        self.optionsLayout.addWidget(self.cfCurrentTextBox)

        self.cfLengthLabel = QLabel("Number of notes")
        self.cfLengthTextBox = QLineEdit()
        self.cfLengthTextBox.setText("8")
        self.optionsLayout.addWidget(self.cfLengthLabel)
        self.optionsLayout.addWidget(self.cfLengthTextBox)

        self.cfGamutLabel = QLabel("Max semitones from tonic")
        self.cfGamutTextBox = QLineEdit()
        self.cfGamutTextBox.setText("26")
        self.optionsLayout.addWidget(self.cfGamutLabel)
        self.optionsLayout.addWidget(self.cfGamutTextBox)

        ###

        self.speciesLayout = QVBoxLayout()

        self.cfButton = QPushButton('Create new Cantus Firmus', self.window)
        self.cfButton.clicked.connect(lambda: self.makeCF())
        self.speciesLayout.addWidget(self.cfButton)

        self.s1Button = QPushButton('Create new first species (using current CF)', self.window)
        self.s1Button.clicked.connect(lambda: self.makeS1())
        self.speciesLayout.addWidget(self.s1Button)

        self.s2Button = QPushButton('Create new second species (using current CF)', self.window)
        self.s2Button.clicked.connect(lambda: self.makeS2())
        self.speciesLayout.addWidget(self.s2Button)

        self.s3Button = QPushButton('Create new third species (using current CF)', self.window)
        self.s3Button.clicked.connect(lambda: self.makeS3())
        self.speciesLayout.addWidget(self.s3Button)

        ###

        self.outerLayout.addLayout(self.optionsLayout)
        self.outerLayout.addLayout(self.speciesLayout)

        self.window.setLayout(self.outerLayout)
        self.window.show()
        print("Generator GUI started")

    def makeCF(self):
        try:
            length = int(self.cfLengthTextBox.text())
            gamutLength = int(self.cfGamutTextBox.text())
            cf = self.creator.createNew('cf', length, gamutLength, [])
            print(cf)
            self.cfCurrentTextBox.setText(",".join([str(x) for x in cf]))
            playVoice(cf)
            if not cf:
                m = QMessageBox()
                m.setText("Nothing could be composed - try another pair of numbers");
                m.exec_()
        except Exception as e:
            print(e)
            m = QMessageBox()
            m.setText("Nothing could be composed - try another pair of numbers");
            m.exec_()

    def makeS1(self):
        try:
            length = int(self.cfLengthTextBox.text())
            gamutLength = int(self.cfGamutTextBox.text())
            s1 = self.creator.createNew('s1', length, gamutLength, self.getCurrentCF())
            tCF = makeTemporalisedLine(self.getCurrentCF(), NoteLength.WHOLE)
            tS1 = makeTemporalisedLine(s1, NoteLength.WHOLE)
            print(self.getCurrentCF(), tS1)
            playPiece([tCF, tS1])
        except Exception as e:
            print(e)
            m = QMessageBox()
            m.setText("Nothing could be composed - try another gamut or create a new CF");
            m.exec_()

    def makeS2(self):
        try:
            length = int(self.cfLengthTextBox.text())
            gamutLength = int(self.cfGamutTextBox.text())
            s2 = self.creator.createNew('s2', length, gamutLength, self.getCurrentCF())
            tCF = makeTemporalisedLine(self.getCurrentCF(), NoteLength.WHOLE)
            tS2 = makeTemporalisedLine(s2, NoteLength.HALF)
            print(self.getCurrentCF(), tS2)
            playPiece([tCF, tS2])
        except Exception as e:
            print(e)
            m = QMessageBox()
            m.setText("Nothing could be composed - try another gamut or create a new CF");
            m.exec_()

    def makeS3(self):
        try:
            length = int(self.cfLengthTextBox.text())
            gamutLength = int(self.cfGamutTextBox.text())
            s3 = self.creator.createNew('s3', length, gamutLength, self.getCurrentCF())
            tCF = makeTemporalisedLine(self.getCurrentCF(), NoteLength.WHOLE)
            tS3 = makeTemporalisedLine(s3, NoteLength.QUARTER)
            print(self.getCurrentCF(), tS3)
            playPiece([tCF, tS3])
        except Exception as e:
            print(e)
            m = QMessageBox()
            m.setText("Nothing could be composed - try another gamut or create a new CF");
            m.exec_()

    def getCurrentCF(self):
        return [int(x) for x in self.cfCurrentTextBox.text().split(',')]

    def getLayout(self):
        return self.outerLayout

class Creator:

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

if __name__ == "__main__":
    app = QApplication([])
    GUI()
    app.exec_()