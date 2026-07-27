import sys
import os
from PyQt5.QtWidgets import QApplication, QVBoxLayout, QWidget, QLabel
from PyQt5.QtCore import QTimer, QTime, Qt
from PyQt5.QtGui import QFont, QFontDatabase

class DigitalClock(QWidget):
    def __init__(self):
        super().__init__()
        self.time_label = QLabel(self)
        self.timer = QTimer(self)
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Digital Clock")
        self.setGeometry(600, 400, 500, 100)

        vbox = QVBoxLayout()

        vbox.addWidget(self.time_label, alignment=Qt.AlignCenter)
        self.setLayout(vbox)

        self.time_label.setStyleSheet("font-size: 150px;"
                                      "color: hsl(111, 100%, 50%)")
        
        self.setStyleSheet("background-color: black;")

        font_id = QFontDatabase.addApplicationFont("DS-DIGIT.TTF")
        font_family = QFontDatabase.applicationFontFamilies(font_id)[0]
        updated_font = QFont(font_family, 150)
        self.time_label.setFont(updated_font)

        self.timer.timeout.connect(self.update_time)
        self.timer.start(1000)


    def update_time(self):
        current_time = QTime.currentTime().toString("hh:mm:ss AP")
        self.time_label.setText(current_time)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    clock = DigitalClock()
    clock.show()
    sys.exit(app.exec_())