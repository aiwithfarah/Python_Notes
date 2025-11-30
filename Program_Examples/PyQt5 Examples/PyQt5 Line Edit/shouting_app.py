# Your Challenge: Modify this code to create a "Shouting App".

# Whatever the user types, the label should show it in UPPERCASE.

# Hint: Python strings have a method called .upper(). Use that inside the update_label function.

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton, QLabel, QLineEdit


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Shouting App")
        self.setGeometry(300, 700, 500, 500)

        # create widgets
        self.input_box = QLineEdit(self)
        self.input_box.setPlaceholderText("Type Something here....")

        # empty label to start with
        self.label = QLabel("", self)

        # create the manage / Vbox Layout
        layout = QVBoxLayout()

        # add widgets to the layout
        layout.addWidget(self.input_box)
        layout.addWidget(self.label)

        # create generic container
        container = QWidget()

        # add layout to the container
        container.setLayout(layout)

        # add container to the central widget
        self.setCentralWidget(container)

        # the wiring
        self.input_box.textChanged.connect(self.update_text)

    def update_text(self, text):
        self.label.setText(f"Upper Case Text: {text.upper()}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
