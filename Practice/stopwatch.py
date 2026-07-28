import sys
from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QVBoxLayout, QHBoxLayout, QPushButton
from PyQt5.QtCore import Qt, QTime, QTimer

class StopWatch(QWidget):
    def __init__(self):
        super().__init__()
        self.time = QTime(0, 0, 0, 0)
        self.time_label = QLabel("00:00:00.00", self)
        self.start_btn = QPushButton("Start", self)
        self.stop_btn = QPushButton("Stop", self)
        self.reset_btn = QPushButton("Reset", self)
        self.timer = QTimer()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Stopwatch")

        vbox = QVBoxLayout()
        vbox.addWidget(self.time_label, alignment=Qt.AlignCenter)

        self.setLayout(vbox)

        hbox = QHBoxLayout()

        hbox.addWidget(self.start_btn)
        hbox.addWidget(self.stop_btn)
        hbox.addWidget(self.reset_btn)

        vbox.addLayout(hbox)

        self.setStyleSheet("""

            QPushButton, QLabel{
                padding: 20px;
                font-weight: bold;
                font-family: calibri;
            }

            QPushButton{
                font-size: 50px;

            }

            QLabel{
                font-size: 120px;
                background-color: hsl(200, 100%, 85%);
                border-radius: 20px;
            }
        """)

        self.start_btn.clicked.connect(self.start)
        self.stop_btn.clicked.connect(self.stop)
        self.reset_btn.clicked.connect(self.reset)

        self.timer.timeout.connect(self.update_display)

    def start(self):
        self.timer.start(10)

    def stop(self):
        self.timer.stop()

    def reset(self):
        self.timer.stop()
        self.time = QTime(0, 0, 0, 0)
        self.time_label.setText(self.format_label(self.time))

    def format_label(self, time):
        hours = time.hour()
        minutes = time.minute()
        seconds = time.second()
        milisec = time.msec() // 10

        return f"{hours:02}:{minutes:02}:{seconds:02}:{milisec:02}"

    def update_display(self):
        self.time = self.time.addMSecs(10)
        self.time_label.setText(self.format_label(self.time))

    

if __name__ == "__main__":
    app = QApplication(sys.argv)
    stopwatch = StopWatch()
    stopwatch.show()
    sys.exit(app.exec_())