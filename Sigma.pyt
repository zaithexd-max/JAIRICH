import sys
import secrets
import requests
from PyQt5.QtWidgets import ( QApplication, QMainWindow, QWidget, QLabel, QLineEdit, QPushButton,
QVBoxLayout, QMessageBox, QHBoxLayout
)
from PyQt5.QtCore import QSettings

BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

class WeatherApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Weather App for Cs major 💔💔😞")
        self.setGeometry(500, 300, 420, 260)

        
        self.settings = QSettings("JaiRich", "SigmaWeatherApp")

       
        self.client_token = self.settings.value("client_token", "")
        if not self.client_token:
            self.client_token = secrets.token_hex(16)
            self.settings.setValue("client_token", self.client_token)


        central = QWidget()
        self.setCentralWidget(central)
        layout = QVBoxLayout(central)

  
        token_layout = QHBoxLayout()
        token_label = QLabel("Install token:")
        self.token_display = QLineEdit(self.client_token)
        self.token_display.setReadOnly(True)
        token_layout.addWidget(token_label)
        token_layout.addWidget(self.token_display)
        layout.addLayout(token_layout)

        api_layout = QHBoxLayout()
        api_label = QLabel("OpenWeather API key:")
        self.api_input = QLineEdit()
        self.api_input.setPlaceholderText("4c6ce90fdcad403de4ea66606185ed65")
        self.api_input.setEchoMode(QLineEdit.Normal)  
        api_layout.addWidget(api_label)
        api_layout.addWidget(self.api_input)
        layout.addLayout(api_layout)

 
        stored_key = self.settings.value("api_key", "")
        if stored_key:
            self.api_input.setText(stored_key)


        self.save_button = QPushButton("Save API Key")
        self.save_button.clicked.connect(self.save_api_key)
        layout.addWidget(self.save_button)


        self.city_input = QLineEdit()
        self.city_input.setPlaceholderText("Enter city name (e.g. London)")
        layout.addWidget(self.city_input)

        self.search_button = QPushButton("Get Weather")
        self.search_button.clicked.connect(self.get_weather)
        layout.addWidget(self.search_button)

        self.result_label = QLabel("Weather info will appear here.")
        self.result_label.setWordWrap(True)
        layout.addWidget(self.result_label)

    def save_api_key(self):
        key = self.api_input.text().strip()
        if not key:
            QMessageBox.warning(self, "No key", "Please enter an API key before saving.")
            return
        self.settings.setValue("api_key", key)
        QMessageBox.information(self, "Saved", "API key saved to settings.")

    def get_weather(self):
        city = self.city_input.text().strip()
        if not city:
            QMessageBox.warning(self, "Error", "Please enter a city name.")
            return

        api_key = self.settings.value("api_key", "")
        if not api_key:

            QMessageBox.warning(
                self, "API Key missing",
                "No OpenWeatherMap API key saved. Paste one in the field and click 'Save API Key'.\n\n"
                f"This install token (for your reference): {self.client_token}"
            )
            return

        params = {
            "q": city,
            "appid": api_key,
            "units": "metric"
        }

        try:
            resp = requests.get(BASE_URL, params=params, timeout=8)
            data = resp.json()
            if data.get("cod") != 200:
                QMessageBox.warning(self, "API Error", f"{data.get('message', 'Unknown error')}")
                return

            temp = data["main"]["temp"]
            feels_like = data["main"]["feels_like"]
            humidity = data["main"]["humidity"]
            description = data["weather"][0]["description"].capitalize()
            country = data["sys"]["country"]

            self.result_label.setText(
                f"City: {city}, {country}\n"
                f"Temperature: {temp}°C\n"
                f"Feels like: {feels_like}°C\n"
                f"Humidity: {humidity}%\n"
                f"Condition: {description}\n\n"
                f"(Install token: {self.client_token})"
            )

        except requests.RequestException as e:
            QMessageBox.critical(self, "Network error", f"Failed to fetch data:\n{e}")

def main():
    app = QApplication(sys.argv)
    w = WeatherApp()
    w.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()