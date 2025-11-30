# The Goal: Create a "Mirror App". Whatever you type in the box should instantly appear on a Label below it.

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QLineEdit, QLabel, QVBoxLayout


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Mirror App")
        self.setGeometry(300, 700, 500, 500)

        # create the widgets line edit adn label
        self.input_box = QLineEdit(self)
        self.input_box.setPlaceholderText("Type something here...")

        # create a lable, starts with empty
        self.label = QLabel("", self)

        # create vertical layout - the manager
        vbox = QVBoxLayout()

        # add widgets to the layout
        vbox.addWidget(self.input_box)
        vbox.addWidget(self.label)

        # create a generic container
        container = QWidget()

        # add layout to the contaner
        container.setLayout(vbox)

        # put container in the center of the main window
        self.setCentralWidget(container)

        # the wiring
        self.input_box.textChanged.connect(self.mirror_text)
    # the slot

    def mirror_text(self, text):
        self.label.setText(f"You Typed: {text}")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
