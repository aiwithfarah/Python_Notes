import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QFont  # to work with fonts
# Qlabel is used to create label widgets that can display text or images
from PyQt5.QtCore import Qt  # Qt class is used for alignment


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setGeometry(150, 300, 550, 450)

        label = QLabel("Hello", self)
        label.setFont(QFont("Arial", 30))  # font,fontsie
        label.setGeometry(0, 0, 500, 100)
        # can use RGB or Hexadecimal values as well
        label.setStyleSheet(
            "color: red;" "background-color: yellow;" "font-weight:bold;" "font-style:italic;" "text-decoration:underline")

        # center label vertically at top
        # label.setAlignment(Qt.AlignTop)  # -->Aligns text vertically to the top

        # for horizontal alignment
        # label.setAlignment(Qt.AlignRight)  # --> Horizontally right
        # label.setAlignment(Qt.AlignCenter)  # --> Align Horizontally Center

        # combine both horiontal and vertical positioning
        # align center and top
        label.setAlignment(Qt.AlignCenter | Qt.AlignTop)


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
