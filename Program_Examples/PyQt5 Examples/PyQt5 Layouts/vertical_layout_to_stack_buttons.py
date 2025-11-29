import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Tiny Window")
        self.resize(200, 200)

        # create widget but dont move them
        btn1 = QPushButton("Top Button!")
        btn2 = QPushButton("Middle Button!")
        btn3 = QPushButton("Bottom Button!")

        # create the manager (vertical box)
        layout = QVBoxLayout()

        # ad widgets to the manager
        layout.addWidget(btn1)
        layout.addWidget(btn2)
        layout.addWidget(btn3)

        # create a generic container
        container = QWidget()

        # Put the layout in the container
        container.setLayout(layout)

        # Put the container in the center of the main window
        self.setCentralWidget(container)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()

    sys.exit(app.exec_())
