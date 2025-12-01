import sys
import os
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PyQt5.QtGui import QFont, QFontDatabase


class MainWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.resize(400, 300)
        self.setWindowTitle("Custom Fonts")

        # 1. FinD the file
        current_folder = os.path.dirname(__file__)
        path_to_file = os.path.join(current_folder, "DS-DIGIT.TTF")

        # 2. Load the file
        font_id = QFontDatabase.addApplicationFont(path_to_file)

        # 3. Get the Real Name
        if font_id != -1:
            real_name = QFontDatabase.applicationFontFamilies(font_id)[0]
            print(f"Loaded : {real_name}")

            # create font object
            custom_font = QFont(real_name, 40)
        else:
            # Failure. Use a backup
            print("Failed to Load Font")
            custom_font = QFont("Arial", 40)

        # 4 The Usage
        self.label = QLabel("Hello World", self)
        self.label.setFont(custom_font)

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        self.setLayout(layout)


if __name__ == '__main__':

    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
