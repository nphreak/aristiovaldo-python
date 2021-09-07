import sys
import random

# Import modules

from PySide6 import QtCore, QtWidgets, QtGui

class Window(QtWidgets.QWidget):




    def __init__(self):
        super().__init__()

        self.hello = ["Hallo Welt", "Hello World", "Salve"]
        self.button = QtWidgets.QPushButton("Click me")
        self.text = QtWidgets.QLabel("Hallo Welt", alignment=QtCore.Qt.AlignCenter)
        self.textbox= QtWidgets.QLineEdit()

        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.addWidget(self.text)
        self.layout.addWidget(self.textbox)
        self.layout.addWidget(self.button)

        self.button.clicked.connect(self.magic)

    @QtCore.Slot()
    def magic(self):
        self.text.setText(random.choice(self.hello))


if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    widget = Window()
    widget.resize(800, 600)
    widget.show()

    sys.exit(app.exec())