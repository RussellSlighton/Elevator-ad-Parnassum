import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QVBoxLayout, QLabel, QLineEdit, QPushButton, \
     QMessageBox

from src import playVoice
from src.lib import makeTemporalisedLine, NoteLength, playPiece
from src.repairer.repairer import repairCF, repairS1, repairS2, repairS3

class GUI:
    def __init__(self):
        print("Repairer GUI starting")
        self.window = QWidget()
        self.window.setWindowTitle("Repairer")
        self.outerLayout = QHBoxLayout()

        ### Left hand side ###

        self.cfLabel = QLabel("Cantus Firmus")
        self.cfInput = QLineEdit()
        self.cfInput.setText("0,0,0,0")

        self.s1Label = QLabel("First Species")
        self.s1Input = QLineEdit()
        self.s1Input.setText("0,0,0,0")

        self.s2Label = QLabel("Second Species")
        self.s2Input = QLineEdit()
        self.s2Input.setText("0,0,0,0,0,0,0,0")

        self.s3Label = QLabel("Third Species")
        self.s3Input = QLineEdit()
        self.s3Input.setText("0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0")

        self.inputLayout = QVBoxLayout()
        self.inputLayout.addWidget(self.cfLabel)
        self.inputLayout.addWidget(self.cfInput)
        self.inputLayout.addWidget(self.s1Label)
        self.inputLayout.addWidget(self.s1Input)
        self.inputLayout.addWidget(self.s2Label)
        self.inputLayout.addWidget(self.s2Input)
        self.inputLayout.addWidget(self.s3Label)
        self.inputLayout.addWidget(self.s3Input)

        ### repair and results ###

        self.repairCF = QPushButton("Repair Cantus Firmus")
        self.repairCF.clicked.connect(lambda: self.doRepairCF())

        self.repairedCF = QLabel()

        self.repairS1 = QPushButton("Repair First Species")
        self.repairS1.clicked.connect(lambda: self.doRepairS1())

        self.repairedS1 = QLabel()

        self.repairS2 = QPushButton("Repair Second Species")
        self.repairS2.clicked.connect(lambda: self.doRepairS2())

        self.repairedS2 = QLabel()

        self.repairS3 = QPushButton("Repair Third Species")
        self.repairS3.clicked.connect(lambda: self.doRepairS3())

        self.repairedS3 = QLabel()

        self.repairLayout = QVBoxLayout()
        self.repairLayout.setAlignment(Qt.AlignTop)
        self.repairLayout.addWidget(self.repairCF)
        self.repairLayout.addWidget(self.repairedCF)
        self.repairLayout.addWidget(self.repairS1)
        self.repairLayout.addWidget(self.repairedS1)
        self.repairLayout.addWidget(self.repairS2)
        self.repairLayout.addWidget(self.repairedS2)
        self.repairLayout.addWidget(self.repairS3)
        self.repairLayout.addWidget(self.repairedS3)

        ### options ###

        self.gamutMaxLabel = QLabel("Max Semitones from tonic:")
        self.gamutMax = QLineEdit()
        self.gamutMax.setText("20")

        self.optionsLayout = QVBoxLayout()
        self.optionsLayout.addWidget(self.gamutMaxLabel)
        self.optionsLayout.addWidget(self.gamutMax)

        ### showing ###

        self.optionsLayout.setAlignment(Qt.AlignTop)
        self.inputLayout.setAlignment(Qt.AlignTop)
        self.repairLayout.setAlignment(Qt.AlignTop)

        self.outerLayout.addLayout(self.optionsLayout)
        self.outerLayout.addLayout(self.inputLayout)
        self.outerLayout.addLayout(self.repairLayout)


        self.window.setLayout(self.outerLayout)
        self.window.show()

    def doRepairCF(self):
        print("Repairing CF")
        cf = [int(x) for x in self.cfInput.text().split(',')]
        try:
            fixed = repairCF(cf, self.getGamut())
            print(fixed)
            playVoice(fixed)
            self.repairedCF.setText(','.join([str(x) for x in fixed]))
        except Exception as e:
            print(e)
            m = QMessageBox()
            m.setText("Could not repair, try increasing the maximum distance from the root");
            m.exec_()

    def doRepairS1(self):
        print("Repaired S1")
        cf = [int(x) for x in self.cfInput.text().split(',')]
        s1 = [int(x) for x in self.s1Input.text().split(',')]
        try:
            fixed = repairS1(cf,s1,self.getGamut())
            print(fixed)
            tCF = makeTemporalisedLine(cf, NoteLength.WHOLE)
            tS1 = makeTemporalisedLine(fixed, NoteLength.WHOLE)
            playPiece([tCF, tS1])
            self.repairedS1.setText(','.join([str(x) for x in fixed]))
        except Exception as e:
            print(e)
            m = QMessageBox()
            m.setText("Could not repair, try increasing the maximum distance from the root or adjusting the line length")
            m.exec_()

    def doRepairS2(self):
        print("Repairing S2")
        cf = [int(x) for x in self.cfInput.text().split(',')]
        s2 = [int(x) for x in self.s2Input.text().split(',')]
        try:
            fixed = repairS2(cf,s2,self.getGamut())
            print(fixed)
            tCF = makeTemporalisedLine(cf, NoteLength.WHOLE)
            tS2 = makeTemporalisedLine(fixed, NoteLength.HALF)
            playPiece([tCF, tS2])
            self.repairedS2.setText(','.join([str(x) for x in fixed]))
        except Exception as e:
            print(e)
            m = QMessageBox()
            m.setText("Could not repair, try increasing the maximum distance from the root or adjusting the line length")
            m.exec_()

    def doRepairS3(self):
        print("Repairing S3")
        cf = [int(x) for x in self.cfInput.text().split(',')]
        s3 = [int(x) for x in self.s3Input.text().split(',')]
        try:
            fixed = repairS3(cf,s3,self.getGamut())
            print(fixed)
            tCF = makeTemporalisedLine(cf, NoteLength.WHOLE)
            tS3 = makeTemporalisedLine(fixed, NoteLength.QUARTER)
            playPiece([tCF, tS3])
            self.repairedS3.setText(','.join([str(x) for x in fixed]))
        except Exception as e:
            print(e)
            m = QMessageBox()
            m.setText("Could not repair, try increasing the maximum distance from the root or adjusting the line length")
            m.exec_()

    def getLayout(self):
        return self.outerLayout

    def getGamut(self):
        return int(self.gamutMax.text())


if __name__ == "__main__":
    app = QApplication([])
    GUI()
    app.exec_()