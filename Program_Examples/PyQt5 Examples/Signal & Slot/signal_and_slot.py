# # Goal: Create a button that changes the text of a Label when clicked.
# The Code Pattern:

# Define a function inside your class (e.g., def change_text(self):).

# Connect the button's clicked signal to that function.

import sys

from PyQt5.QtWidgets import QApplication, QLabel, QPushButton, QVBoxLayout, QMainWindow, QWidget


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Magic Button")
        self.resize(200, 300)

        # create button and label widget
        self.label = QLabel("I am normal text", self)
        self.button = QPushButton("Change Text", self)

        # create the vertical box
        layout = QVBoxLayout()

        # add widget to the manager
        layout.addWidget(self.label)
        layout.addWidget(self.button)

        # create a generic container
        container = QWidget()

        # put the layout in the container
        container.setLayout(layout)

        # put container in the center of the main window
        self.setCentralWidget(container)

        # # The wiring Signal -> SLot.
        # Pass fnction name w/o parentheses
        self.button.clicked.connect(self.do_magic)
    # The slot/function

    def do_magic(self):
        self.label.setText("Text Has Changed")
        self.button.setText("Magic Done!")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
