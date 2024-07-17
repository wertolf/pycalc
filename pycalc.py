"""PyCalc is a simple calculator built with Python and PyQt."""

import sys

from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget

WINDOW_SIZE = 235

class PyCalcWindow(QMainWindow):
    """PyCalc's main window (GUI or view)."""

    def __init__(self):
        super().__init__(parent=None)
        self.setWindowTitle("PyCalc")
        self.setFixedSize(WINDOW_SIZE, WINDOW_SIZE)
        centralWidget = QWidget(parent=self)
        self.setCentralWidget(centralWidget)

def main():
    """PyCalc's main function."""
    app = QApplication([])
    window = PyCalcWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
