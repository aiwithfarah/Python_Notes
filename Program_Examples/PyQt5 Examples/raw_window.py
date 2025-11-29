# # Goal: Prove you understand the relationship between QApplication and QWidget without using a class .
# Import sys, QApplication, and QWidget.

# Create the QApplication object (pass sys.argv).

# Create a QWidget object.

# Set the window title to "I am the Boss".

# Resize the window to 600 width and 400 height.

# Crucial Step: Show the window.

# Crucial Step: Start the event loop (app.exec_()).


import sys
from PyQt5.QtWidgets import QApplication, QWidget

app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle("Hi There!")
window.resize(600, 400)

window.show()
sys.exit(app.exec_())
