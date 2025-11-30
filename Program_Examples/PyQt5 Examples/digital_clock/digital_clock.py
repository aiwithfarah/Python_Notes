# Python PyQt5 Digital Clock Example

import sys  # provides variables used and maintained by python intrepretor
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QVBoxLayout
from PyQt5.QtCore import QTimer, QTime, Qt
from PyQt5.QtGui import QFont, QFontDatabase


class DigitalClock(QWidget):

    def __init__(self):
        super().__init__()  # constructor of the parent
        self.time_label = QLabel(self)
        self.timer = QTimer(self)
        self.initUI()

        # here we will be constructing the entities of the digital clock

    # here we will design the layout of the digital clock
    def initUI(self):
        self.setWindowTitle("Digital Clock")
        self.setGeometry(600, 400, 300, 200)

        vbox = QVBoxLayout()
        vbox.addWidget(self.time_label)

        self.setLayout(vbox)

        # center align horizontally
        self.time_label.setAlignment(Qt.AlignCenter)
        self.time_label.setStyleSheet(
            "font-size: 150px;" "color: hsl(111, 100%, 50%);")

        # change bg color of clock. self applies to the window
        self.setStyleSheet("background-color:black;")

        # set custom font
        # QFontDatabase class available for mamaging and querying fonts available to the application
        font_id = QFontDatabase.addApplicationFont(
            "D:\AI Billionaire\Python - Zero to Mastery\Program_examples\PyQt5 Examples\digital_clock\DS-DIGIT.TTF")
        font_family = QFontDatabase.applicationFontFamilies(font_id)[0]
        my_font = QFont(font_family, 150)
        self.time_label.setFont(my_font)

        # to get the clock to update every second we need time widget to a slot (update_time)
        self.timer.timeout.connect(self.update_time)
        self.timer.start(1000)  # for 1000 millisecon

        self.update_time()

    def update_time(self):
        current_time = QTime.currentTime().toString("hh:mm:ss AP")
        self.time_label.setText(current_time)


if __name__ == '__main__':  # this statement will be true if we are running this program directly
    app = QApplication(sys.argv)
    clock = DigitalClock()
    clock.show()  # shows uo for a brief second
    sys.exit(app.exec_())
