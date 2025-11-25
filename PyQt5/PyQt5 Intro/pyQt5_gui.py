import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QIcon  # to work with icons


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("My First Cook GUI")
        # x,y,width,height --> since x and y are 0 the window willbe displayed in the top-left corner
        self.setGeometry(700, 300, 500, 500)
        self.setWindowIcon(
            QIcon("D:\AI Billionaire\Python - Zero to Mastery\PyQT5\profile.png"))


def main():
    # allows us to pass command line arguments to the app
    app = QApplication(sys.argv)
    window = MainWindow()  # default behavior of a window isto hide it
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
