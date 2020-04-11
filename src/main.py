import sys

from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QPushButton, QVBoxLayout, QLabel

from src.generator import GUI as generator
from src.checker import GUI as checker

if __name__ == "__main__":
    print("Selector GUI starting")

    app = QApplication(sys.argv)
    app.setApplicationName("Checker")
    window = QWidget()
    window.setWindowTitle("Select Tool")

    selectGenerator = QPushButton("Generator")
    selectGenerator.clicked.connect(lambda: generator())
    selectChecker = QPushButton("Checker")
    selectChecker.clicked.connect(lambda: checker())
    selectRepairer = QPushButton("Repairer")
    #selectGenerator.clicked.connect(lambda: repairer())


    selectLayout = QHBoxLayout()
    selectLayout.addWidget(selectGenerator)
    selectLayout.addWidget(selectChecker)
    selectLayout.addWidget(selectRepairer)

    label = QLabel("Select Tool")

    outerLayout = QVBoxLayout()
    outerLayout.addWidget(label)
    outerLayout.addLayout(selectLayout)

    window.setLayout(outerLayout)
    window.show()
    app.exec_()



    # print("Running Generator")
    # generator()
    # print("Running Generator")
    # checker()

