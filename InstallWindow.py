from PyQt5.QtWidgets import QWidget,QPushButton,QVBoxLayout,QLabel,QLineEdit
from loginwindow import loginscreen
import json
from DataBaseOperation import DBOperation

class InstallWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Vehicle parking")
        self.resize(400,400)

        layout=QVBoxLayout()

        label_db_name=QLabel("database name")
        label_db_username = QLabel("database username")
        label_db_password = QLabel("database password")
        label_admin_username = QLabel("Admin username")
        label_admin_password = QLabel("Admin password")
        label_no_of_two_seater = QLabel("No of two wheeler vehicle")
        label_no_of_four_seater = QLabel("No of Four wheeler vehicle")

        self.input_db_name=QLineEdit()
        self.input_db_name.setText("vehicleparking")
        self.input_db_username = QLineEdit()
        self.input_db_username.setText("vehicle")
        self.input_db_password = QLineEdit()
        self.input_db_password.setText("vehicle_password")
        self.input_admin_username = QLineEdit()
        self.input_admin_password = QLineEdit()
        self.input_two_wheeler = QLineEdit()
        self.input_four_wheeler = QLineEdit()

        buttonsave=QPushButton("save data")

        self.error_label=QLabel()
        self.error_label.setStyleSheet("color:red")

        layout.addWidget(label_db_name)
        layout.addWidget(self.input_db_name)
        layout.addWidget(label_db_username)
        layout.addWidget(self.input_db_username)
        layout.addWidget(label_db_password)
        layout.addWidget(self.input_db_password)
        layout.addWidget(label_admin_username)
        layout.addWidget(self.input_admin_username)
        layout.addWidget(label_admin_password)
        layout.addWidget(self.input_admin_password)
        layout.addWidget(label_no_of_two_seater)
        layout.addWidget(self.input_two_wheeler)
        layout.addWidget(label_no_of_four_seater)
        layout.addWidget(self.input_four_wheeler)
        layout.addWidget(buttonsave)
        layout.addWidget(self.error_label)

        buttonsave.clicked.connect(self.showStepInfo)

        self.setLayout(layout)

    def showStepInfo(self):
        if self.input_db_name.text()=="":
            self.error_label.setText("Enter correct input for DB NAME")
            return

        if self.input_db_username.text() == "":
            self.error_label.setText("Enter correct input for DB USERNAME")
            return

        if self.input_db_password.text() == "":
            self.error_label.setText("Enter correct input for DB PASSWORD")
            return

        if self.input_admin_username.text() == "":
            self.error_label.setText("Enter correct input for ADMIN USERNAME")
            return

        if self.input_admin_password.text() == "":
            self.error_label.setText("Enter correct input for ADMIN PASSWORD")
            return

        if self.input_two_wheeler.text() == "":
            self.error_label.setText("Enter correct input for TWO WHEELER")
            return

        if self.input_four_wheeler.text() == "":
            self.error_label.setText("Enter correct input for FOUR WHEELER")
            return


        data={"username":self.input_db_username.text(),"database":self.input_db_name.text(),"password":self.input_db_password.text()}
        file=open("./config.json","w")
        file.write(json.dumps(data))
        file.close()
        dboperation=DBOperation()
        dboperation.Createtable()
        dboperation.InsertAdmin(self.input_admin_username.text(),self.input_admin_password.text())
        dboperation.INSERTONETIMEDATA(int(self.input_two_wheeler.text()),int(self.input_four_wheeler.text()))

        self.close()
        self.login=loginscreen()
        self.login.showloginscreen()
        print("save data")
