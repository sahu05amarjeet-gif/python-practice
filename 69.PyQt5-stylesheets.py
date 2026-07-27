import sys
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QApplication, QMainWindow, QPushButton

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # self.setGeometry(0, 0, 500, 500)
        self.button1 = QPushButton("#1")
        self.button2 = QPushButton("#2")
        self.button3 = QPushButton("#3")
        self.initUI()
    def initUI(self):
        central_wid = QWidget()
        self.setCentralWidget(central_wid)

        hbox = QHBoxLayout()
        hbox.addWidget(self.button1)
        hbox.addWidget(self.button2)
        hbox.addWidget(self.button3)

        central_wid.setLayout(hbox)

        self.button1.setObjectName("button1")
        self.button2.setObjectName("button2")
        self.button3.setObjectName("button3")

        self.setStyleSheet("""
            QPushButton{
                font-size: 40px;
                font-family: Rubik;
                padding: 15px 75px;
                margin: 25px;
                border: 3px solid;
                border-radius: 15px;

            }

            QPushButton#button1{
                background-color: red;
            }

            QPushButton#button2{
                background-color: cyan;
            }

            QPushButton#button3{
                background-color: wheat;
            }

            QPushButton#button1:hover{
                background-color: hsl(352, 98%, 63%);
            }

            QPushButton#button2:hover{
                background-color: hsl(194, 94%, 84%);
            }

            QPushButton#button3:hover{
                background-color: hsl(143, 97%, 63%);
            }
        
        """)

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()