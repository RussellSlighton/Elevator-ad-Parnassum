import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QVBoxLayout, QLabel, QLineEdit, QPushButton, QListWidget

from src import playVoice
from src.lib import makeTemporalisedLine, NoteLength, playPiece
from src.repairer.repairer import repairCF, repairS1, repairS2, repairS3

class GUI:
    def __init__(self):
        print("Repairer GUI starting")

        self.app = QApplication(sys.argv)
        self.app.setApplicationName("Repairer")
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

        ### showing ###

        self.outerLayout.addLayout(self.inputLayout)
        self.outerLayout.addLayout(self.repairLayout)


        self.window.setLayout(self.outerLayout)
        self.window.show()
        self.app.exec_()

    def doRepairCF(self):
        print("Rpaired CF")
        cf = [int(x) for x in self.cfInput.text().split(',')]
        fixed = repairCF(cf)
        print(fixed)
        playVoice(cf)
        self.repairedCF.setText(','.join([str(x) for x in fixed]))

    def doRepairS1(self):
        print("Repaired S1")
        cf = [int(x) for x in self.cfInput.text().split(',')]
        s1 = [int(x) for x in self.s1Input.text().split(',')]
        fixed = repairS1(cf,s1)
        print(fixed)
        tCF = makeTemporalisedLine(cf, NoteLength.WHOLE)
        tS1 = makeTemporalisedLine(s1, NoteLength.WHOLE)
        playPiece([tCF, tS1])
        self.repairedS1.setText(','.join([str(x) for x in fixed]))

    def doRepairS2(self):
        print("Repairing S2")
        cf = [int(x) for x in self.cfInput.text().split(',')]
        s2 = [int(x) for x in self.s2Input.text().split(',')]
        fixed = repairS1(cf,s2)
        print(fixed)
        tCF = makeTemporalisedLine(cf, NoteLength.WHOLE)
        tS2 = makeTemporalisedLine(s2, NoteLength.HALF)
        playPiece([tCF, tS2])
        self.repairedS2.setText(','.join([str(x) for x in fixed]))

    def doRepairS3(self):
        print("Repairing S3")
        cf = [int(x) for x in self.cfInput.text().split(',')]
        s3 = [int(x) for x in self.s3Input.text().split(',')]
        fixed = repairS1(cf,s3)
        print(fixed)
        tCF = makeTemporalisedLine(cf, NoteLength.WHOLE)
        tS3 = makeTemporalisedLine(s3, NoteLength.QUARTER)
        playPiece([tCF, tS3])
        self.repairedS3.setText(','.join([str(x) for x in fixed]))

    def getLayout(self):
        return self.outerLayout


if __name__ == "__main__":
    GUI()