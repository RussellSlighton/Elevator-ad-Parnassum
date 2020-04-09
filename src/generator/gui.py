import sys

from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QHBoxLayout, QLineEdit, QLabel, QMessageBox

from src import playVoice, playPiece
from src.generator import Generator
from src.specs import *
from src.types2 import ConstPitch, makeTemporalisedLine, NoteLength

class GUI:
    def __init__(self):
        print("Generator GUI starting")
        self.creator = Creator()
        self.lastCF = []

        self.app = QApplication(sys.argv)
        self.app.setApplicationName("SM(Bach)")
        self.window = QWidget()
        self.window.setWindowTitle("SM(Bach)")
        self.speciesLayout = QHBoxLayout()

        ###

        self.cfLayout = QVBoxLayout()
        self.cfInfo = QLabel("Press this first")
        self.cfLayout.addWidget(self.cfInfo)

        self.cfButton = QPushButton('Create new Cantus Firmus', self.window)
        self.cfButton.clicked.connect(lambda : self.makeCF())
        self.cfLayout.addWidget(self.cfButton)

        self.cfLengthLabel = QLabel("Number of notes")
        self.cfLengthTextBox = QLineEdit()
        self.cfLengthTextBox.setText("8")
        self.cfLayout.addWidget(self.cfLengthLabel)
        self.cfLayout.addWidget(self.cfLengthTextBox)

        self.cfGamutLabel = QLabel("Max semitones from tonic")
        self.cfGamutTextBox = QLineEdit()
        self.cfGamutTextBox.setText("7")
        self.cfLayout.addWidget(self.cfGamutLabel)
        self.cfLayout.addWidget(self.cfGamutTextBox)

        ###

        self.s1Layout = QVBoxLayout()
        self.s1Button = QPushButton('Create new first species (using last CF)', self.window)
        self.s1Button.clicked.connect(lambda : self.makeS1())
        self.s1Layout.addWidget(self.s1Button)

        self.s1LengthLabel = QLabel("Number of notes")
        self.s1LengthTextBox = QLineEdit()
        self.s1LengthTextBox.setText("8")
        self.s1Layout.addWidget(self.s1LengthLabel)
        self.s1Layout.addWidget(self.s1LengthTextBox)

        self.s1GamutLabel = QLabel("Max semitones from tonic")
        self.s1GamutTextBox = QLineEdit()
        self.s1GamutTextBox.setText("13")
        self.s1Layout.addWidget(self.s1GamutLabel)
        self.s1Layout.addWidget(self.s1GamutTextBox)

        ###

        self.s2Layout = QVBoxLayout()
        self.s2Button = QPushButton('Create new second species (using last CF)', self.window)
        self.s2Button.clicked.connect(lambda : self.makeS2())
        self.s2Layout.addWidget(self.s2Button)

        self.s2LengthLabel = QLabel("Number of notes")
        self.s2LengthTextBox = QLineEdit()
        self.s2LengthTextBox.setText("8")
        self.s2Layout.addWidget(self.s2LengthLabel)
        self.s2Layout.addWidget(self.s2LengthTextBox)

        self.s2GamutLabel = QLabel("Max semitones from tonic")
        self.s2GamutTextBox = QLineEdit()
        self.s2GamutTextBox.setText("13")
        self.s2Layout.addWidget(self.s2GamutLabel)
        self.s2Layout.addWidget(self.s2GamutTextBox)

        ###

        self.s3Layout = QVBoxLayout()
        self.s3Warning = QLabel("Careful, this is VERY slow")
        self.s3Layout.addWidget(self.s3Warning)

        self.s3Button = QPushButton('Create new third species (using last CF)', self.window)
        self.s3Button.clicked.connect(lambda : self.makeS3())
        self.s3Layout.addWidget(self.s3Button)

        self.s3LengthLabel = QLabel("Number of notes")
        self.s3LengthTextBox = QLineEdit()
        self.s3LengthTextBox.setText("8")
        self.s3Layout.addWidget(self.s3LengthLabel)
        self.s3Layout.addWidget(self.s3LengthTextBox)

        self.s3GamutLabel = QLabel("Max semitones from tonic")
        self.s3GamutTextBox = QLineEdit()
        self.s3GamutTextBox.setText("13")
        self.s3Layout.addWidget(self.s3GamutLabel)
        self.s3Layout.addWidget(self.s3GamutTextBox)

        ###

        self.speciesLayout.addLayout(self.cfLayout)
        self.speciesLayout.addLayout(self.s1Layout)
        self.speciesLayout.addLayout(self.s2Layout)
        self.speciesLayout.addLayout(self.s3Layout)

        self.window.setLayout(self.speciesLayout)
        self.window.show()
        self.app.exec_()
        print("Generator GUI started")


    def makeCF(self):
        try:
            length = int(self.cfLengthTextBox.text())
            gamutLength = int(self.cfGamutTextBox.text())
            cf = self.creator.createNew('cf', length, gamutLength, [])
            self.lastCF = cf
            print(cf)
            playVoice(cf)
            if cf == []:
                m = QMessageBox()
                m.setText("Nothing could be composed - try another pair of numbers");
                m.exec_()
        except Exception:
            m = QMessageBox()
            m.setText("Nothing could be composed - try another pair of numbers");
            m.exec_()

    def makeS1(self):
        try:
            length = int(self.s1LengthTextBox.text())
            gamutLength = int(self.s1GamutTextBox.text())
            s1 = self.creator.createNew('s1', length, gamutLength, self.lastCF)
            tCF = makeTemporalisedLine(self.lastCF, NoteLength.WHOLE)
            tS1 = makeTemporalisedLine(s1, NoteLength.WHOLE)
            print(self.lastCF, tS1)
            playPiece([tCF, tS1])
        except Exception:
            m = QMessageBox()
            m.setText("Nothing could be composed - try another pair of numbers or create a new CF");
            m.exec_()

    def makeS2(self):
        try:
            length = int(self.s2LengthTextBox.text())
            gamutLength = int(self.s2GamutTextBox.text())
            s2 = self.creator.createNew('s2', length, gamutLength, self.lastCF)
            tCF = makeTemporalisedLine(self.lastCF, NoteLength.WHOLE)
            tS2 = makeTemporalisedLine(s2, NoteLength.HALF)
            print(self.lastCF, tS2)
            playPiece([tCF, tS2])
        except Exception:
            m = QMessageBox()
            m.setText("Nothing could be composed - try another pair of numbers or create a new CF");
            m.exec_()
        
    def makeS3(self):
        try:
            length = int(self.s3LengthTextBox.text())
            gamutLength = int(self.s3GamutTextBox.text())
            s3 = self.creator.createNew('s3', length, gamutLength, self.lastCF)
            tCF = makeTemporalisedLine(self.lastCF, NoteLength.WHOLE)
            tS3 = makeTemporalisedLine(s3, NoteLength.QUARTER)
            print(self.lastCF, tS3)
            playPiece([tCF, tS3])
        except Exception:
            m = QMessageBox()
            m.setText("Nothing could be composed - try another pair of numbers or create a new CF");
            m.exec_()

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
    gui = GUI()
    gui.run()