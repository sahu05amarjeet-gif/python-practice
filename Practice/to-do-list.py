import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel, QLineEdit, QCheckBox
from PyQt5.QtCore import Qt

class ToDo_List(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("To-Do-List")
        self.resize(500, 500)
        self.top_label = QLabel("MY TASKS", self)
        self.tasks_left = QLabel("0 tasks left", self)
        self.textbox = QLineEdit(self)
        self.textbox.setPlaceholderText("Enter a new task")
        self.add_task_btn = QPushButton("Add Task", self)
        self.del_btn =QPushButton("Delete Completed",self)
        self.clear_all = QPushButton("Clear All", self)
        self.task_completed = []
        self.initUI()



    def initUI(self):
        self.add_task_btn.clicked.connect(self.add_task)
        self.del_btn.clicked.connect(self.on_click)
        self.textbox.returnPressed.connect(self.add_task)
        self.clear_all.clicked.connect(self.clear_all_task)

        self.vbox = QVBoxLayout()
        self.vbox.addWidget(self.top_label, alignment=Qt.AlignCenter | Qt.AlignTop)
        self.vbox.addWidget(self.tasks_left, alignment=Qt.AlignCenter | Qt.AlignTop)
        self.vbox.addWidget(self.textbox)
        self.vbox.addWidget(self.add_task_btn)
        self.vbox.addWidget(self.clear_all)
        self.vbox.addWidget(self.del_btn)
        self.vbox.setSpacing(20)
        self.del_btn.hide()
        self.setLayout(self.vbox)

        self.top_label.setObjectName("top_label")
        self.tasks_left.setObjectName("task_left")
        self.add_task_btn.setObjectName("add_task_btn")
        self.del_btn.setObjectName("del_btn")
        self.clear_all.setObjectName("clear_all")

        self.setStyleSheet("""

            QWidget{
                background-color: #080503;
            }

            QLabel#top_label{
                font-family: Calibri;
                font-weight: Bold;
                font-size: 32px;
            }

            QLabel#task_left{
                font-size: 16px;
                color: grey;
                font-family: Calibri;
            }

            QPushButton#add_task_btn{
                font-family: Calibri;
                border-radius: 20px;
                background-color: #8a36eb;
                padding: 14px;
                color: white;
            }

            QPushButton#add_task_btn:hover{
                background-color: #721fd1;
            }

            QPushButton#del_btn{
                font-family: Calibri;
                border-radius: 20px;
                background-color: #29cc36;
                padding: 14px;
                color: black;
            }

            QPushButton#del_btn:hover{
                background-color: #3ade47;
            }

            QPushButton#clear_all{
                font-family: Calibri;
                border-radius: 20px;
                background-color: #c92037;
                padding: 14px;
                color: black;
            }

            QPushButton#clear_all:hover{
                background-color: #d92b42;
            }

            QLineEdit{
                padding: 14px;
                font-size: 16px;
                border: 3px solid grey;
                border-radius: 20px;
            }

            QLineEdit:focus{
                border: 3px solid #caa0fa; 
            }

            QLineEdit::placeholder{
                font-weight: light;
            }

            QCheckBox{
                font-size: 16px;
                padding: 14px;
                color: grey;
            }

            QCheckBox:hover{
                color: white;
            }

    
    """)

    def add_task(self):
        text = self.textbox.text()

        if text.strip(): 
            checkbox = QCheckBox(text)
            self.vbox.addWidget(self.checkbox)
            self.task_completed.append(self.checkbox)
            checkbox.stateChanged.connect(self.on_check)

        
        self.update_task_left()
        self.textbox.clear()

    def update_dlt_btn(self):
        on_checked = False
        for task in self.task_completed:
            if task.isChecked():
                on_checked = True
        if on_checked:
            self.del_btn.show()
        else:
            self.del_btn.hide()

    def update_task_left(self):
        if len(self.task_completed) == 1:
            self.tasks_left.setText(f"{len(self.task_completed)} task left")
        else:
            self.tasks_left.setText(f"{len(self.task_completed)} tasks left")

    def on_check(self):
        checkbox = self.sender()
        font = checkbox.font()
        if checkbox.isChecked():
            font.setStrikeOut(True)
            checkbox.setFont(font)
        else:
            font.setStrikeOut(False)
            checkbox.setFont(font)
        self.update_task_left()
        self.update_dlt_btn()

    def on_click(self):
        for task in self.task_completed.copy():
            if task.isChecked(): 
                task.deleteLater()
                self.task_completed.remove(task)
        self.update_task_left()
        self.update_dlt_btn()

    def clear_all_task(self):
        for task in self.task_completed.copy():
            task.deleteLater()
            self.task_completed.remove(task)
        self.update_task_left()
        self.update_dlt_btn()
            
if __name__ == "__main__":
    app = QApplication(sys.argv)
    todo_window = ToDo_List()
    todo_window.show()
    sys.exit(app.exec_())

#If you need to remove items from a list while looping through it, don't loop directly over the list you're modifying. use copy()