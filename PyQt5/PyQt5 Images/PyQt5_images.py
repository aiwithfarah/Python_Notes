import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QPixmap
# --> QPixmap class is used for handling images provides functionality for loading, manipualting and displaying images


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setGeometry(700, 300, 500, 500)

        label = QLabel(self)  # self refers to the window object
        label.setGeometry(0, 0, 100, 100)

        pixmap = QPixmap("PyQT5\PyQt5 Images\profile.png")
        # we have to add pixmap object to the label
        label.setPixmap(pixmap)
        # to scale the image according to the size of the label use setScaledContents method
        label.setScaledContents(True)


``
label.setGeometry((self.width() - label.width()) // 2,
                  self.height() - label.height() // 2,
                  label.width(),
                  label.height())


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
