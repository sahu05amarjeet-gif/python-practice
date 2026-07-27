import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QCheckBox
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.checkbox = QCheckBox("Do you like food?", self)
        self.setGeometry(0, 0, 500, 500)
        self.initUI()


    def initUI(self):
        self.checkbox.setGeometry(10, 10, 500, 100)
        self.checkbox.setStyleSheet("font-size: 40px;"
                                    "font-family: Rubik;")
        self.checkbox.stateChanged.connect(self.on_checked)

    def on_checked(self, state):
        if state == Qt.Checked:
            print("You like the food")
        else:
            print("You don't like the FOOD")

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()