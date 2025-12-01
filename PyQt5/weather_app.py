# openweathermap.org - -> to get real time weather data
# Sign in - -> My API Keys - -> Copy API Key(make sure status is active)


import sys  # handles system variables for Python Interpretor
import requests  # --> make request to an API
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout

# To work with alignment
from PyQt5.QtCore import Qt


class WeatherApp(QWidget):

    def __init__(self):
        super().__init__()  # incase we have arguments to send to the parent

        # declare widgets that belong to weather app object
        self.city_label = QLabel("Enter City Name: ", self)
        self.city_input = QLineEdit(self)
        self.get_weather_button = QPushButton("Get Weather", self)
        self.temp_label = QLabel(self)
        self.emoji_label = QLabel(self)
        self.description_label = QLabel(self)
        self.initUI()

    def initUI(self):  # initialize UI
        self.setWindowTitle("Weather App")
        layout = QVBoxLayout()
        layout.addWidget(self.city_label)
        layout.addWidget(self.city_input)
        layout.addWidget(self.get_weather_button)
        layout.addWidget(self.temp_label)
        layout.addWidget(self.emoji_label)
        layout.addWidget(self.description_label)

        self.setLayout(layout)
        self.city_label.setAlignment(Qt.AlignCenter)
        self.city_input.setAlignment(Qt.AlignCenter)
        self.temp_label.setAlignment(Qt.AlignCenter)
        self.emoji_label.setAlignment(Qt.AlignCenter)
        self.description_label.setAlignment(Qt.AlignCenter)

        # apply css style based on an object name
        self.city_label.setObjectName("city_label")
        self.city_input.setObjectName("city_input")
        self.get_weather_button.setObjectName("get_weather_button")
        self.temp_label.setObjectName("temp_label")
        self.emoji_label.setObjectName("emoji_label")
        self.description_label.setObjectName("description_label")

        self.setStyleSheet(""" 
            QLabel, QPushButton {
                           font-family: Calibri;
                           }

            QLabel#city_label {
                           font-size: 40px;
                           font-style: italic;

                           } 
            QLineEdit#city_input {
                           font-size: 40px;
                           }

            QPushButton#get_weather_button {
                           font-size: 30px;
                           font-weight: bold;
                           }

            QLabel#temp_label {
                           font-size: 75px;

                           }
            QLabel#emoji_label {
                           font-size: 100px;
                           font-family: Segoe UI emoji;
                           
                           }
            QLabel#description_label{
                           font-size: 50px;
                           }
""")

    # connect signal to slot
        self.get_weather_button.clicked.connect(self.get_weather)

    def get_weather(self):
        api_key = "49032cbeca16642528485f4b45ddc2bd"
        city = self.city_input.text()
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"

        try:
            response = requests.get(url)
            response.raise_for_status()
            # convert response to json format
            data = response.json()

            if data["cod"] == 200:
                self.display_weather(data)

        except requests.exceptions.HTTPError as http_error:
            # print(response.status_code)
            match response.status_code:
                case 400:
                    self.display_error(
                        "Bad Request: \nPlease check your input")
                case 401:
                    self.display_error("UnAuthorized: \nInvalid API Key")
                case 403:
                    self.display_error("Forbidden: \nAccess is Denied!")
                case 404:
                    self.display_error("Not Found: \nCity Not Found")
                case 500:
                    self.display_error(
                        "Internal Server Error: \nPlease try again later")
                case 502:
                    self.display_error(
                        "Bad Gateway: \nInvalid Response from the server")
                case 503:
                    self.display_error("Service Unavailable: \nServer is down")
                case 504:
                    self.display_error(
                        "Gateway Timeout: \nNo Response from server")
                case _:
                    self.display_error(f"HTTP Error occured: \n{http_error}")

        except requests.exceptions.ConnectionError:
            self.display_error(
                "Connection Error\nCheck your internt connection!")
        except requests.exceptions.Timeout:
            self.display_error(
                "We have a TimeOut Error\nThe Request Timed Out")
        except requests.exceptions.TooManyRedirects:
            self.display_error("Too many redirects\nCheck the URL")
        except requests.exceptions.RequestException as req_error:
            self.display_error(f"Request Error:\n{req_error}")

    def display_error(self, message):
        self.temp_label.setStyleSheet("font-size: 30px;")
        self.temp_label.setText(message)
        self.emoji_label.clear()
        self.description_label.clear()

    def display_weather(self, data):
        self.temp_label.setStyleSheet("font-size: 75px;")
        temp_k = data['main']['temp']
        temp_c = temp_k - 273.15
        temp_f = (temp_k * 9/5) - 459.67
        weather_id = data['weather'][0]['id']
        weather_description = data['weather'][0]['description']

        self.temp_label.setText(f"{temp_f:.0f}F")
        self.emoji_label.setText(self.get_weather_emoji(weather_id))
        self.description_label.setText(weather_description)

    @staticmethod
    def get_weather_emoji(weather_id):
        if 200 <= weather_id <= 232:
            return "🌦"
        elif 300 <= weather_id <= 321:
            return "⛅"
        elif 500 <= weather_id <= 531:
            return "🌧"
        elif 600 <= weather_id <= 622:
            return "❄"
        elif 700 <= weather_id <= 741:
            return "🌫"
        elif weather_id == 762:
            return "🌋"
        elif weather_id == 771:
            return "🌊"
        elif weather_id == 781:
            return "🌪"
        elif weather_id == 800:
            return "🌞"
        elif 801 <= weather_id <= 804:
            return "☁"
        else:
            return ""


if __name__ == '__main__':

    app = QApplication(sys.argv)
    weather_app = WeatherApp()
    weather_app.show()
    sys.exit(app. exec_())
