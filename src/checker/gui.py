import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QVBoxLayout, QLabel, QLineEdit, QPushButton, QListWidget

from src.checker.checker import checkCF, checkS1, checkS2, checkS3

class GUI:
    def __init__(self):
        print("Checker GUI starting")

        self.window = QWidget()
        self.window.setWindowTitle("Checker")
        self.outerLayout = QHBoxLayout()

        ### Left hand side ###

        self.empty = QLabel("     ")

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
        self.inputLayout.addWidget(self.empty)
        self.inputLayout.addWidget(self.cfLabel)
        self.inputLayout.addWidget(self.cfInput)
        self.inputLayout.addWidget(self.s1Label)
        self.inputLayout.addWidget(self.s1Input)
        self.inputLayout.addWidget(self.s2Label)
        self.inputLayout.addWidget(self.s2Input)
        self.inputLayout.addWidget(self.s3Label)
        self.inputLayout.addWidget(self.s3Input)

        ### check and results ###

        self.checkCF = QPushButton("Check Cantus Firmus")
        self.checkCF.clicked.connect(lambda: self.doCheckCF())

        self.checkS1 = QPushButton("Check First Species")
        self.checkS1.clicked.connect(lambda: self.doCheckS1())

        self.checkS2 = QPushButton("Check Second Species")
        self.checkS2.clicked.connect(lambda: self.doCheckS2())

        self.checkS3 = QPushButton("Check Third Species")
        self.checkS3.clicked.connect(lambda: self.doCheckS3())

        self.checkLayout = QHBoxLayout()
        self.checkLayout.setAlignment(Qt.AlignTop)
        self.checkLayout.addWidget(self.checkCF)
        self.checkLayout.addWidget(self.checkS1)
        self.checkLayout.addWidget(self.checkS2)
        self.checkLayout.addWidget(self.checkS3)

        ### results ###
        self.resultsLabel = QLabel("Problems with...")
        self.results = QListWidget()

        ### showing ###

        self.rightSide = QVBoxLayout()
        self.rightSide.addLayout(self.checkLayout)
        self.rightSide.addWidget(self.resultsLabel)
        self.rightSide.addWidget(self.results)

        self.outerLayout.addLayout(self.inputLayout)
        self.outerLayout.addLayout(self.rightSide)


        self.window.setLayout(self.outerLayout)
        self.window.show()

    def doCheckCF(self):
        print("Checking CF")
        self.results.clear()
        cf = [int(x) for x in self.cfInput.text().split(',')]
        problems = checkCF(cf)
        print(problems)
        self.resultsLabel.setText("Problems with Cantus Firmus:")
        if not problems.reasons:
            self.results.addItem("Cantus Firmus is valid!")
        else:
            for problem in problems.reasons:
                self.results.addItem(problem.split(':')[1])

    def doCheckS1(self):
        print("Checking S1")
        self.results.clear()
        cf = [int(x) for x in self.cfInput.text().split(',')]
        s1 = [int(x) for x in self.s1Input.text().split(',')]
        problems = checkS1(cf,s1)
        print(problems)
        self.resultsLabel.setText("Problems with First Species:")
        if not problems.reasons:
            self.results.addItem("First Species is valid!")
        else:
            for problem in problems.reasons:
                self.results.addItem(problem.split(':')[1])

    def doCheckS2(self):
        print("Checking S2")
        self.results.clear()
        cf = [int(x) for x in self.cfInput.text().split(',')]
        s2 = [int(x) for x in self.s2Input.text().split(',')]
        problems = checkS2(cf,s2)
        print(problems)
        self.resultsLabel.setText("Problems with Second Species:")
        if not problems.reasons:
            self.results.addItem("Second Species is valid!")
        else:
            for problem in problems.reasons:
                self.results.addItem(problem.split(':')[1])

    def doCheckS3(self):
        print("Checking S3")
        self.results.clear()
        cf = [int(x) for x in self.cfInput.text().split(',')]
        s3 = [int(x) for x in self.s3Input.text().split(',')]
        problems = checkS3(cf,s3)
        print(problems)
        self.resultsLabel.setText("Problems with Third Species:")
        if not problems.reasons:
            self.results.addItem("Third Species is valid!")
        else:
            for problem in problems.reasons:
                self.results.addItem(problem.split(':')[1])

    def getLayout(self):
        return self.outerLayout


if __name__ == "__main__":
    app = QApplication([])
    GUI()
    app.exec_()