from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout
import sys
# from PyQt5.QtWidgets import QApplication, QWidget, QLabel

# # create the application (the manager)
# # sys.argv allows us to pass Command Line Arguments to the app
# app = QApplication(sys.argv)

# # 2. Create the window (the object)
# window = QWidget()
# window.setWindowTitle("My First App")
# window.resize(400, 300)  # Width, Height

# # 3. Add Content. A Label
# label = QLabel("Hello World", window)  # pass window as the parent
# label.move(150, 300)  # X, Y Coordinates

# # 4. Show the Window
# window.show()

# # 5.Start the Event Lopp (the infinite wait)
# sys.exit(app.exec_())

print("-------------------------------------------------")
print("The OOP Way - using Inheritence!")


class MyApp(QWidget):
    def __init__(self):
        super().__init__()  # initialize the parent QWidget

    # Setup the UI
        self.setWindowTitle("OOP Window")
        self.resize(200, 300)

        # Create Widget
        self.label = QLabel("Click the button below")
        self.button = QPushButton("Click Me!")

        # Layouts Organizing things
        # without a layout widgets stack on top of each other
        # QVBoxLayout = "Vertical Box Layout" (stacks items top to bottom)

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.button)

        self.setLayout(layout)


# Run the app
app = QApplication(sys.argv)
my_window = MyApp()  # create an instance of our class
my_window.show()
sys.exit(app.exec_())
