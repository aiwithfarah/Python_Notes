# Goal: Create a custom class that builds itself.

# Instructions:

# Create a class named TinyWindow that inherits from QWidget.

# Inside __init__:

# Call super().__init__() (The Foundation).

# Set the title to "Tiny Window".

# Resize it to 100x100.

# Outside the class:

# Create the QApplication.

# Create an instance of TinyWindow.

# Show it and run the loop.

import sys
from PyQt5.QtWidgets import QApplication, QWidget


class TinyWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Tiny Window")
        self.resize(100, 100)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = TinyWindow()
    window.show()
    sys.exit(app.exec_())
