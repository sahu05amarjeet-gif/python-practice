import sys
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow, QPushButton, QWidget, QVBoxLayout, QLineEdit, QHBoxLayout
from PyQt5.QtGui import QIntValidator
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Student Information")
        self.setGeometry(0, 0, 500, 500)
        self.label = QLabel("Student Information", self)
        self.name_label = QLabel("Name", self)
        self.age_label = QLabel("Age", self)
        self.result_label = QLabel("")
        self.name_input = QLineEdit()
        self.age_input = QLineEdit()
        self.age_input.setValidator(QIntValidator(1, 120))
        self.name_input.setPlaceholderText("Enter your name")
        self.age_input.setPlaceholderText("Enter your age")
        self.button = QPushButton("Submit", self)
        self.clear_button = QPushButton("Clear", self)
        self.initUI()

    def initUI(self):

        central_wid = QWidget()
        self.setCentralWidget(central_wid)
        self.button.clicked.connect(self.on_click)
        self.clear_button.clicked.connect(self.clear_form)
        self.label.setStyleSheet("font-size: 26px;"
                                 "font-weight: bold;")
        self.name_label.setStyleSheet("font-size: 18px;")
        self.age_label.setStyleSheet("font-size: 18px;")
        self.name_input.setStyleSheet("font-size: 15px;"
                                      "padding: 8px;"
                                      "border: 1px solid grey;"
                                      "border-radius: 5px;")
        self.age_input.setStyleSheet("font-size: 15px;"
                                      "padding: 8px;"
                                      "border: 1px solid grey;"
                                      "border-radius: 5px;")
        self.button.setStyleSheet("font-size: 10px;"
                                  "padding: 12px;"
                                  "border-radius: 8px;"
                                  "background-color: green;"
                                  "color: white;")
        self.clear_button.setStyleSheet("font-size: 10px;"
                                  "padding: 12px;"
                                  "border-radius: 8px;"
                                  "background-color: red;"
                                  "color: white;")

        self.result_label.setStyleSheet("font-size: 14px;"
                                        "border: 1px solid grey;"
                                        "padding: 8px;"
                                        )

        vbox = QVBoxLayout()
        hbox = QHBoxLayout()
        vbox.addWidget(self.label, alignment=Qt.AlignHCenter | Qt.AlignTop)
        vbox.addWidget(self.name_label)
        vbox.addWidget(self.name_input)
        vbox.addWidget(self.age_label)
        vbox.addWidget(self.age_input)
        vbox.addWidget(self.result_label)
        vbox.setSpacing(10)


        central_wid.setLayout(vbox)

        vbox.addLayout(hbox)
        hbox.addWidget(self.button)
        hbox.addWidget(self.clear_button)

    def clear_form(self):
        self.name_input.clear()
        self.age_input.clear()
        self.result_label.clear()



        

    def on_click(self):
        name = self.name_input.text()
        age = self.age_input.text()
        rename = name.replace(" ", "")

        if name == "" or age == "":
            self.result_label.setText("Please fill in all fields")
        elif rename.isalpha():
            self.result_label.setText(f"Name: {name} \nAge: {age} years")
            self.name_input.clear()
            self.age_input.clear()
        else:
            self.result_label.setText("Please enter a valid name")



def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
