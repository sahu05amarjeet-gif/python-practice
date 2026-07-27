import sys
from PyQt5.QtWidgets import QApplication, QLabel, QVBoxLayout, QMainWindow, QHBoxLayout, QGridLayout, QWidget
from PyQt5.QtCore import Qt
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Fruit List")
        self.setGeometry(0, 0, 500, 500)
        self.initUI()
    def initUI(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        label1 = QLabel("Hello")
        label2 = QLabel("World")

        

        label1.setStyleSheet("background-color: red;" "color: black;")
        label2.setStyleSheet("background-color: yellow;" "color: black;")

        vbox = QVBoxLayout()
        central_widget.setLayout(vbox)
        vbox.addWidget(label1, alignment=Qt.AlignCenter)
        vbox.addWidget(label2, alignment=Qt.AlignCenter)

        

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()





