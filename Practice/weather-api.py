import sys
import requests
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout
from PyQt5.QtCore import Qt

class WeatherApp(QWidget):
    def __init__(self):
        super().__init__()
        self.city_label = QLabel("Enter city name: ", self)
        self.city_input = QLineEdit(self)
        self.city_input.setPlaceholderText("Ex. Mumbai")
        self.get_weather_btn = QPushButton("Get Weather", self)
        self.temp_label = QLabel(self)
        self.emoji_label = QLabel(self)
        self.descrition_label = QLabel(self)   
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Weather App")
        vbox = QVBoxLayout()
        vbox.addWidget(self.city_label, alignment= Qt.AlignCenter)
        vbox.addWidget(self.city_input, alignment= Qt.AlignCenter)
        vbox.addWidget(self.get_weather_btn)
        vbox.addWidget(self.temp_label, alignment= Qt.AlignCenter)
        vbox.addWidget(self.emoji_label, alignment= Qt.AlignCenter)
        vbox.addWidget(self.descrition_label, alignment= Qt.AlignCenter)
        self.setLayout(vbox)

        self.city_label.setObjectName("city_label")
        self.city_input.setObjectName("city_input")
        self.get_weather_btn.setObjectName("get_weather_btn")
        self.temp_label.setObjectName("temp_label")
        self.emoji_label.setObjectName("emoji_label")
        self.descrition_label.setObjectName("description_label")
        self.setStyleSheet("""
            QLabel, QPushButton{
                font-family: Calibri;
            }

            QLabel#city_label{
                font-size: 40px;
                font-style: italic;
            }

            QLineEdit#city_input{
                font-size: 40px;
            }

            QPushButton#get_weather_btn{
                font-size: 30px;
                font-weight: bold;
            }


            QLabel#emoji_label{
                font-size: 100px;
                font-family: Noto Emoji;
            }

            QLabel#description_label{
                font-size: 50px;
            }


        
        """)

        self.get_weather_btn.clicked.connect(self.get_weather)
        self.city_input.returnPressed.connect(self.get_weather)
    def get_weather(self):
        api_key = "d7d87d98775a4dd57e80f0b66c9a302b"
        city_name = self.city_input.text()
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}"

        try:
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()

            if data["cod"] == 200:
                self.display_weather(data)

        except requests.exceptions.HTTPError as http_error:
            match response.status_code:
                case 400:
                    self.display_error("Bad request:\nPlease check your input")
                case 401:
                    self.display_error("Unauthorized:\nInvalid API key")
                case 403:
                    self.display_error("Forbidden:\nAccess is denied")
                case 404:
                    self.display_error("Not found:\nCity not found")
                case 500:
                    self.display_error("Internal Server Error:\nPlease try again later")
                case 502:
                    self.display_error("Bad Gateway:\nInvalid response from the server")
                case 503:
                    self.display_error("Service Unavailable:\nServer is down")
                case 504:
                    self.display_error("Gateway Timeout:\nNo response from the server")
                case _:
                    self.display_error(f"HTTP error occured:\n {http_error}")
        except requests.exceptions.ConnectionError:
            self.display_error("Connection Error:\nCheck your internet connection")
        except requests.exceptions.Timeout:
            self.display_error("Timeout Error:\nThe request timed out")
        except requests.exceptions.TooManyRedirects:
            self.display_error("Too many Redirects:\nCheck your URL")
        except requests.exceptions.RequestException as req_error:
            self.display_error(f"Request Error:\n{req_error}")

    def display_error(self, message):
        self.temp_label.setStyleSheet("font-size: 32px;")
        self.temp_label.setText(message)
        self.emoji_label.clear()
        self.descrition_label.clear()

    def display_weather(self, data):
        self.temp_label.setStyleSheet("font-size: 75px;")
        temp_in_kel = data["main"]["temp"]
        temp_in_cel = temp_in_kel - 273.15
        weather_id = data["weather"][0]["id"]
        weather_description = data["weather"][0]["description"]
        self.temp_label.setText(f"{temp_in_cel:.0f}°C")
        self.emoji_label.setText(self.get_weather_emoji(weather_id))
        self.descrition_label.setText(weather_description.title())
        

    @staticmethod
    def get_weather_emoji(weather_id):
        if 200 <= weather_id <= 232:
            return "⛈️"
        elif 300 <= weather_id <= 321:
            return "🌦️"
        elif 500 <= weather_id <= 531:
            return "🌧️"
        elif 600 <= weather_id <= 622:
            return "❄️"
        elif 701 <= weather_id <= 741:
            return "🌀"
        elif weather_id == 762:
            return "🌋"
        elif weather_id == 771:
            return "💨"
        elif weather_id == 781:
            return "🌪️"
        elif weather_id == 800:
            return "☀️"
        elif 801 <= weather_id <= 804:
            return "☁️"
        else:
            return ""

if __name__ == "__main__":
    app = QApplication(sys.argv)
    weather_app = WeatherApp()
    weather_app.show()
    sys.exit(app.exec_())