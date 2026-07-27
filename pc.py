import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QVBoxLayout, QWidget, QHBoxLayout
from PyQt5.QtCore import Qt
class MainWindow(QMainWindow):
        def __init__(self):
            super().__init__()
            self.setGeometry(0, 0, 500, 500)
            self.label = QLabel("0", self)
            self.pos_count = QPushButton("+1", self)
            self.neg_count = QPushButton("-1", self)
            self.count = 0 
            self.initUI()
            

        def initUI(self):

            self.pos_count.clicked.connect(self.increase)
            self.neg_count.clicked.connect(self.decrease)



            center_wid = QWidget()
            self.setCentralWidget(center_wid)

            vbox = QVBoxLayout()
            hbox = QHBoxLayout()
            vbox.addWidget(self.label, alignment=Qt.AlignCenter)
            center_wid.setLayout(vbox)

            vbox.addLayout(hbox)
            hbox.addWidget(self.pos_count)
            hbox.addWidget(self.neg_count)

        def increase(self):
              self.count += 1 
              self.label.setText(str(self.count))

        def decrease(self):
              self.count -= 1
              self.label.setText(str(self.count))
            

            

def main():
        app = QApplication(sys.argv)
        window = MainWindow()
        window.show()
        sys.exit(app.exec_())

if __name__ == "__main__":
        main()
