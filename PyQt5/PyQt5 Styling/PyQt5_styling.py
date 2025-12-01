import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout


class MainWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyQt5 Styling")
        self.resize(400, 200)

        # create widgets - label, button,
        self.label = QLabel("Hover over the button")
        self.button = QPushButton("Click Me!")

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.button)
        self.setLayout(layout)


if __name__ == '__main__':

    app = QApplication(sys.argv)

    # Global Style Sheet
    app.setStyleSheet(""" 
        QWidget{
                    background-color:#2b2b2b;      
                }
                      
        QLabel {
                    color: white;
                    font-size: 18px;
                    font-family: Arial;
                    font-weight: bold;
                      }
        QPushButton{
                    background-color: purple;
                    color: white;
                    font-size: 20px;
                    border-radius: 10;
                    padding: 15px,
                      }
        QPushButton:hover {
                    background-color: hsl(273, 97%, 68%)
                      }
""")
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
