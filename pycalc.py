"""PyCalc is a simple calculator built with Python and PyQt."""

import sys
from functools import partial

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QApplication,
    QGridLayout,
    QLineEdit,
    QMainWindow,
    QPushButton,
    QVBoxLayout,
    QWidget,
)

ERROR_MSG = "ERROR"
WINDOW_SIZE = 235
DISPLAY_HEIGHT = 35
BUTTON_SIZE = 40

class PyCalcWindow(QMainWindow):
    """PyCalc's main window (GUI or view)."""

    # some type hints (optional but useful for IDEs)
    buttonMap: dict[str, QPushButton]

    def __init__(self):
        super().__init__(parent=None)
        self.setWindowTitle("PyCalc")
        self.setFixedSize(WINDOW_SIZE, WINDOW_SIZE)
        self.generalLayout = QVBoxLayout()
        centralWidget = QWidget(parent=self)
        centralWidget.setLayout(self.generalLayout)
        self.setCentralWidget(centralWidget)
        self._createDisplay()
        self._createButtons()
    
    def _createDisplay(self):
        self.display = QLineEdit()
        self.display.setFixedHeight(DISPLAY_HEIGHT)
        self.display.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.display.setReadOnly(True)
        self.generalLayout.addWidget(self.display)
    
    def _createButtons(self):
        self.buttonMap = {}
        buttonsLayout = QGridLayout()
        keyBoard = [
            ["7", "8", "9", "/", "C"],
            ["4", "5", "6", "*", "("],
            ["1", "2", "3", "-", ")"],
            ["0", "00", ".", "+", "="],
        ]

        for row, keys in enumerate(keyBoard):
            for col, key in enumerate(keys):

                # create the button
                button = QPushButton(text=key)
                button.setFixedSize(BUTTON_SIZE, BUTTON_SIZE)

                # add the button to buttonsLayout
                buttonsLayout.addWidget(button, row, col)

                # add the button to self.buttonMap
                self.buttonMap[key] = button

        self.generalLayout.addLayout(buttonsLayout)

    def setDisplayText(self, text):
        """Set the display's text."""
        self.display.setText(text)
        self.display.setFocus()
    
    def getDisplayText(self):
        """Get the display's text."""
        return self.display.text()

    def clearDisplay(self):
        """Clear the display."""
        self.setDisplayText("")

def evaluateExpression(expr):
    """Evaluate an expression (Model)."""
    try:
        result = str(eval(expr, {}, {}))
    except Exception:
        result = ERROR_MSG
    return result

class PyCalc:
    """PyCalc's controller class."""

    def __init__(self, model, view: PyCalcWindow):
        self._evaluate = model
        self._view = view
        self._connectSignalsAndSlots()
    
    def _calculateResult(self):
        expression = self._view.getDisplayText()
        result = self._evaluate(expression)
        self._view.setDisplayText(result)
    
    def _buildExpression(self, subExpression):
        text = self._view.getDisplayText()
        if text == ERROR_MSG:
            # do nothing if already error (Press C to clear display)
            return
        
        expression = text + subExpression
        self._view.setDisplayText(expression)
    
    def _connectSignalsAndSlots(self):
        for keySymbol, button in self._view.buttonMap.items():
            if keySymbol not in {"=", "C"}:
                button.clicked.connect(
                    partial(self._buildExpression, keySymbol)
                )
        self._view.buttonMap["C"].clicked.connect(self._view.clearDisplay)
        self._view.buttonMap["="].clicked.connect(self._calculateResult)

        # returnPressed means "pressed the RETURN/ENTER key"
        self._view.display.returnPressed.connect(self._calculateResult)
        

def main():
    """PyCalc's main function."""
    app = QApplication([])
    window = PyCalcWindow()
    window.show()
    PyCalc(model=evaluateExpression, view=window)
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
