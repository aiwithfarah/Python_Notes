# <!-- Goal: Place a widget inside the window using self as the parent.

# Instructions:

# Copy your code from Exercise 2.

# Add QLabel to your imports.

# Inside the __init__ method:

# Create a QLabel with the text "I am inside!".

# Important: Make sure you pass self as the second argument to the Label so it knows where to sit.

# Move the label to x=50, y=50 using .move(50, 50).

# (If you run this and don't see the text, you probably forgot to pass self to the label!) -->

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel


class TinyWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Tiny Window")
        self.resize(200, 200)

        self.label = QLabel("I am inside", self)
        self.label.move(50, 50)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = TinyWindow()
    window.show()

    sys.exit(app.exec_())
