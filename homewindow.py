from PyQt5.QtWidgets import QWidget,QMainWindow,QPushButton,QLineEdit,QLabel,QVBoxLayout,QHBoxLayout,QFrame,QGridLayout,QComboBox,QTableWidget,QTableWidgetItem
from DataBaseOperation import DBOperation
from PyQt5.QtWidgets import QHeaderView
from PyQt5.Qt import *
from PyQt5.QtGui import *
class homescreen(QMainWindow):
    def __init__(self):
        super(homescreen, self).__init__()
        self.setWindowTitle("vehicle parking")
        self.dboperation=DBOperation()

        widget=QWidget()
        widget.setStyleSheet("background:#000")
        layout_horizontal=QHBoxLayout()


        menu_vertical_layout = QVBoxLayout()
        self.btn_home=QPushButton("Dashboard ADMIN")
        self.btn_add=QPushButton("Add Vehicle")
        self.btn_manage=QPushButton("Manage Vehicle")
        self.btn_history=QPushButton("History")

        menu_vertical_layout.setContentsMargins(0,0,0,0)
        menu_vertical_layout.setSpacing(0)
        self.btn_home.setStyleSheet("width:300px;height:180px;font-size:30px;background:blue;color:#fff;font-weight:bold;border:2px solid black")
        self.btn_add.setStyleSheet("width:300px;height:180px;font-size:30px;background:blue;color:#fff;font-weight:bold;border:2px solid black")
        self.btn_manage.setStyleSheet("width:300px;height:180px;font-size:30px;background:blue;color:#fff;font-weight:bold;border:2px solid black")
        self.btn_history.setStyleSheet("width:300px;height:180px;font-size:30px;background:blue;color:#fff;font-weight:bold;border:2px solid black")


        self.btn_home.clicked.connect(self.showhome)
        self.btn_add.clicked.connect(self.showadd)
        self.btn_manage.clicked.connect(self.showmanage)
        self.btn_history.clicked.connect(self.showhistory)


        menu_frame=QFrame()
        menu_vertical_layout.addWidget(self.btn_home)
        menu_vertical_layout.addWidget(self.btn_add)
        menu_vertical_layout.addWidget(self.btn_manage)
        menu_vertical_layout.addWidget(self.btn_history)
        menu_vertical_layout.addStretch()
        menu_frame.setLayout(menu_vertical_layout)
        #menu_frame.setMinimumWidth(200)
        #menu_frame.setMaximumHeight(200)


        parent_vertical=QVBoxLayout()
        parent_vertical.setContentsMargins(0,0,0,0)
        self.vertical_1=QVBoxLayout()
        self.addhomepage()


        self.vertical_2=QVBoxLayout()
        self.vertical_2.setContentsMargins(0,0,0,0)
        self.addvehicle()

        self.vertical_3=QVBoxLayout()
        self.vertical_3.setContentsMargins(0,0,0,0)
        self.addmanage()


        self.vertical_4=QVBoxLayout()
        self.vertical_4.setContentsMargins(0,0,0,0)
        self.addhistory()


        self.frame_1=QFrame()
        self.frame_1.setMinimumWidth(self.width())
        self.frame_1.setMaximumWidth(self.width())
        self.frame_1.setMaximumHeight(self.width())
        self.frame_1.setMaximumHeight(self.width())

        self.frame_1.setLayout(self.vertical_1)
        self.frame_2=QFrame()
        self.frame_2.setLayout(self.vertical_2)
        self.frame_3=QFrame()
        self.frame_3.setLayout(self.vertical_3)
        self.frame_4=QFrame()
        self.frame_4.setLayout(self.vertical_4)

        parent_vertical.addWidget(self.frame_1)
        parent_vertical.addWidget(self.frame_2)
        parent_vertical.addWidget(self.frame_3)
        parent_vertical.addWidget(self.frame_4)

        layout_horizontal.addWidget(menu_frame)
        layout_horizontal.addLayout(parent_vertical)
        layout_horizontal.setContentsMargins(0,0,0,0)
        parent_vertical.setContentsMargins(0,0,0,0)
        parent_vertical.addStretch()
        #menu_vertical_layout.addStretch()
        layout_horizontal.addStretch()

        widget.setLayout(layout_horizontal)
        self.frame_1.show()
        self.frame_2.hide()
        self.frame_3.hide()
        self.frame_4.hide()
        self.setCentralWidget(widget)

    def showhistory(self):
        self.btn_home.setStyleSheet("width:300px;height:180px;font-size:30px;background:blue;color:#fff;font-weight:bold;border:1px solid white")
        self.btn_add.setStyleSheet("width:300px;height:180px;font-size:30px;background:blue;color:#fff;font-weight:bold;border:1px solid white")
        self.btn_manage.setStyleSheet("width:300px;height:180px;font-size:30px;background:blue;color:#fff;font-weight:bold;border:1px solid white")
        self.btn_history.setStyleSheet("width:300px;height:180px;font-size:30px;background:red;color:#fff;font-weight:bold;border:1px solid white")

        self.frame_1.hide()
        self.frame_2.hide()
        self.frame_3.hide()
        self.frame_4.show()

    def showmanage(self):
        self.btn_home.setStyleSheet("width:300px;height:180px;font-size:30px;background:blue;color:#fff;font-weight:bold;border:1px solid white")
        self.btn_add.setStyleSheet("width:300px;height:180px;font-size:30px;background:blue;color:#fff;font-weight:bold;border:1px solid white")
        self.btn_manage.setStyleSheet("width:300px;height:180px;font-size:30px;background:red;color:#fff;font-weight:bold;border:1px solid white")
        self.btn_history.setStyleSheet("width:300px;height:180px;font-size:30px;background:blue;color:#fff;font-weight:bold;border:1px solid white")

        self.frame_1.hide()
        self.frame_2.hide()
        self.frame_3.show()
        self.frame_4.hide()


    def showadd(self):
        self.btn_home.setStyleSheet("width:300px;height:180px;font-size:30px;background:blue;color:#fff;font-weight:bold;border:1px solid white")
        self.btn_add.setStyleSheet("width:300px;height:180px;font-size:30px;background:red;color:#fff;font-weight:bold;border:1px solid white")
        self.btn_manage.setStyleSheet("width:300px;height:180px;font-size:30px;background:blue;color:#fff;font-weight:bold;border:1px solid white")
        self.btn_history.setStyleSheet("width:300px;height:180px;font-size:30px;background:blue;color:#fff;font-weight:bold;border:1px solid white")

        self.frame_1.hide()
        self.frame_2.show()
        self.frame_3.hide()
        self.frame_4.hide()


    def showhome(self):
        self.btn_home.setStyleSheet("width:300px;height:180px;font-size:30px;background:red;color:#fff;font-weight:bold;border:1px solid white")
        self.btn_add.setStyleSheet("width:300px;height:180px;font-size:30px;background:blue;color:#fff;font-weight:bold;border:1px solid white")
        self.btn_manage.setStyleSheet("width:300px;height:180px;font-size:30px;background:blue;color:#fff;font-weight:bold;border:1px solid white")
        self.btn_history.setStyleSheet("width:300px;height:180px;font-size:30px;background:blue;color:#fff;font-weight:bold;border:1px solid white")
        self.frame_1.show()
        self.frame_2.hide()
        self.frame_3.hide()
        self.frame_4.hide()



    def refreshhome(self):
        while self.gridLayout.count():
            child=self.gridLayout.takeAt(0)
            if child.widget():
                child.widget().deleteLater()
        row = 0
        i = 0
        alldata = self.dboperation.slotspace()
        for data in alldata:
            label = QPushButton("SLOT" + str(data[0])+" \n "+str(data[1]))

            if data[3] == 1:
                label.setStyleSheet("background-color:green;color:white;padding:5px;width:100px;height:220px;border:1px solid white;text-align:center;font-weight:bold")
            else:

                label.setStyleSheet("background-color:red;color:white;padding:5px;width:100px;height:220px;border:1px solid white;text-align:center;font-weight:bold")

            if i % 5 == 0:
                i = 0
                row = row + 1
            self.gridLayout.addWidget(label, row, i)
            i = i + 1

    def addhomepage(self):
        self.vertical_1.setContentsMargins(0,0,0,0)
        button=QPushButton("REFRESH")
        button.setStyleSheet("color:#fff;padding:8px 0px;font-size:20px;background:green;border:1px solid white")
        button.clicked.connect(self.refreshhome)
        vertical_layout=QVBoxLayout()
        vertical_layout.setContentsMargins(0,0,0,0)

        frame=QFrame()
        horziontal=QHBoxLayout()
        horziontal.setContentsMargins(0,0,0,0)
        label=QLabel("home")
        label.setStyleSheet("background:black;color:#fff;font-size:20px;font-weight:bold;width:500px;height:30px;padding:10px")
        horziontal.addWidget(label)
        vertical_layout.addLayout(horziontal)

        alldata=self.dboperation.slotspace()
        print(alldata)
        self.gridLayout=QGridLayout()
        self.gridLayout.setContentsMargins(0,0,0,0)
        self.gridLayout.setHorizontalSpacing(0)
        self.gridLayout.setVerticalSpacing(0)
        vertical_layout.addWidget(button)
        vertical_layout.addLayout(self.gridLayout)

        row=0
        i=0
        for data in alldata:
            label=QPushButton("SLOT"+str(data[0])+" \n "+str(data[1]))

            if data[3]==1:
                label.setStyleSheet("background-color:green;color:white;padding:5px;width:100px;height:220px;border:1px solid white;text-align:center;font-weight:bold")
            else:

              label.setStyleSheet("background-color:red;color:white;padding:5px;width:100px;height:220px;border:1px solid white;text-align:center;font-weight:bold")

            if i%5==0:
                i=0
                row=row+1
            self.gridLayout.addWidget(label,row,i)
            i=i+1


        frame.setLayout(vertical_layout)
        self.vertical_1.addWidget(frame)
        self.vertical_1.addStretch()
        frame1 = QFrame()
        vertical_layout = QVBoxLayout()
        first_label = QLabel(" Slots 1-25 : 2 Wheeler")
        first_label.setStyleSheet("color:#fff;padding:4px 0px;font-size:20px;align:right")
        second_label = QLabel("Slots 26-50 : 4 Wheeler")
        second_label.setStyleSheet("color:#fff;padding:4px 0px;font-size:20px;align:right")
        vertical_layout.addWidget(first_label)
        vertical_layout.addWidget(second_label)
        frame1.setLayout(vertical_layout)
        self.vertical_1.addWidget(frame1)
        self.vertical_1.addStretch()

    def addvehicle(self):
        layout=QVBoxLayout()
        frame=QFrame()
        label=QLabel("Add Vehicle")
        label.setStyleSheet("background:black;color:#fff;font-size:20px;font-weight:bold;width:500px;height:30px;padding:10px")
        name_label=QLabel("Enter Name:")
        name_label.setStyleSheet("color:#fff;padding:8px 0px;font-size:20px")
        mobile_label = QLabel("Enter Mobile Number:")
        mobile_label.setStyleSheet("color:#fff;padding:8px 0px;font-size:20px")
        vehicle_label = QLabel("Enter Vehicle Number:")
        vehicle_label.setStyleSheet("color:#fff;padding:8px 0px;font-size:20px")
        vehicle_type = QLabel("Enter Vehicle Type:")
        vehicle_type.setStyleSheet("color:#fff;padding:8px 0px;font-size:20px")
        self.error_label=QLabel("")
        self.error_label.setStyleSheet("color:red;padding:8px 0px;font-size:20px")

        self.name_input=QLineEdit(self)
        reg = QRegExp("^[A-Za-z]{10}$")
        self.name_input.setMaxLength(10)
        input_va = QRegExpValidator(reg, self.name_input)
        self.name_input.setValidator(input_va)
        self.name_input.setStyleSheet("color:#fff;padding:8px 0px;font-size:20px")
        self.mobile_input = QLineEdit(self)
        self.mobile_input.setStyleSheet("color:#fff;padding:8px 0px;font-size:20px")
        self.mobile_input.setValidator(QIntValidator())
        reg = QRegExp("^[0-9]{10}$")
        self.mobile_input.setMaxLength(10)
        input_va = QRegExpValidator(reg, self.mobile_input)
        self.mobile_input.setValidator(input_va)
        self.vehicle_input = QLineEdit()
        self.vehicle_input.setStyleSheet("color:#fff;padding:8px 0px;font-size:20px")
        self.vehicle_input.setMaxLength(4)
        self.vtype=QComboBox()
        self.vtype.setStyleSheet("color:#fff;padding:8px 0px;font-size:20px;border:1px solid white")
        self.vtype.addItem("2 Wheeler")
        self.vtype.addItem("4 Wheeler")



        self.button=QPushButton("Add Vehicle")
        self.button.setStyleSheet("padding:7px;font-size:20px;background:green;color:#fff;border:1px solid white")

        layout.addWidget(label)
        layout.addWidget(name_label)
        layout.addWidget(self.name_input)
        layout.addWidget(mobile_label)
        layout.addWidget(self.mobile_input)
        layout.addWidget(vehicle_label)
        layout.addWidget(self.vehicle_input)
        layout.addWidget(vehicle_type)
        layout.addWidget(self.vtype)
        layout.addWidget(self.button)
        layout.addWidget(self.error_label)

        layout.setContentsMargins(0,0,0,0)
        frame.setMinimumHeight(self.height())
        frame.setMinimumWidth(self.width())


        layout.addStretch()

        frame.setLayout(layout)
        self.button.clicked.connect(self.check)
        self.vertical_2.addWidget(frame)

    def check(self):

        if self.name_input.text() == "":
            self.error_label.setText("Enter correct input for name")
            return
        if self.mobile_input.text() == "":
            self.error_label.setText("Enter correct input for mobile")
            return
        if len(self.mobile_input.text()) != 10:
            self.error_label.setText("Number Not valid")
            return
        if self.vehicle_input.text() == "":
            self.error_label.setText("Enter correct input for vehicle")
            return
        if len(self.vehicle_input.text()) != 4:
            self.error_label.setText("Invalid Vehicle Number")
            return

        self.button.clicked.connect(lambda:self.addVehicle(self.name_input.text(),self.vehicle_input.text(),self.mobile_input.text(),self.vtype.currentIndex(),self.error_label))




    def addVehicle(self, name, vehicleno, mobile, index, error_label):
        vtp = 2
        if index == 0:
            vtp = 2
        else:
            vtp = 4

        data = self.dboperation.AddVehicle(name,vehicleno,mobile,str(vtp))
        if data == True:
            error_label.setText("Added Successfully")
        elif data == False:
            error_label.setText("Failed to Add Vehicle")
        else:
            error_label.setText(str(data))

    def addmanage(self):
        data=self.dboperation.currentvehicle()
        self.table=QTableWidget()
        self.table.setStyleSheet("background:#fff")
        self.table.setRowCount(len(data))
        self.table.setColumnCount(7)

        button = QPushButton("REFRESH")
        button.setStyleSheet("color:#fff;padding:8px 0px;font-size:20px;background:green;border:1px solid white")
        button.clicked.connect(self.refreshmanage)

        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
        self.table.setHorizontalHeaderItem(0,QTableWidgetItem("ID"))
        self.table.setHorizontalHeaderItem(1,QTableWidgetItem("NAME OF OWNER "))
        self.table.setHorizontalHeaderItem(2,QTableWidgetItem("VEHICLE NO"))
        self.table.setHorizontalHeaderItem(3,QTableWidgetItem("MOBILE NO"))
        self.table.setHorizontalHeaderItem(4,QTableWidgetItem("VEHICLE TYPE"))
        self.table.setHorizontalHeaderItem(5,QTableWidgetItem("ENTRY TIME "))
        self.table.setHorizontalHeaderItem(6,QTableWidgetItem("ACTION"))



        loop=0
        for smalldata in data:
            self.table.setItem(loop,0,QTableWidgetItem(str(smalldata[0])))
            self.table.setItem(loop,1,QTableWidgetItem(str(smalldata[1])))
            self.table.setItem(loop,2,QTableWidgetItem(str(smalldata[6])))
            self.table.setItem(loop,3,QTableWidgetItem(str(smalldata[2])))
            self.table.setItem(loop,4,QTableWidgetItem(str(smalldata[7])))
            self.table.setItem(loop,5,QTableWidgetItem(str(smalldata[3])))
            self.button_exit=QPushButton("EXIT")
            self.button_exit.setStyleSheet("color:#fff;padding:8px 0px;font-size:10px;background:green;border:1px solid white")
            self.table.setCellWidget(loop,6,self.button_exit)
            self.button_exit.clicked.connect(self.exitCall)

            loop=loop+1

            frame=QFrame()
            layout=QVBoxLayout()
            layout.setContentsMargins(0,0,0,0)
            layout.setSpacing(0)
            layout.addWidget(button)
            layout.addWidget(self.table)
            frame.setLayout(layout)
            frame.setContentsMargins(0,0,0,0)
            frame.setMaximumWidth(self.width())
            frame.setMinimumWidth(self.width())
            self.vertical_3.addWidget(frame)
            self.vertical_3.addStretch()

    def refreshmanage(self):
        data = self.dboperation.currentvehicle()
        self.table.setRowCount(len(data))
        self.table.setColumnCount(7)
        loop = 0
        for smalldata in data:
            self.table.setItem(loop, 0, QTableWidgetItem(str(smalldata[0])))
            self.table.setItem(loop, 1, QTableWidgetItem(str(smalldata[1])))
            self.table.setItem(loop, 2, QTableWidgetItem(str(smalldata[6])))
            self.table.setItem(loop, 3, QTableWidgetItem(str(smalldata[2])))
            self.table.setItem(loop, 4, QTableWidgetItem(str(smalldata[7])))
            self.table.setItem(loop, 5, QTableWidgetItem(str(smalldata[3])))
            self.button_exit = QPushButton("EXIT")
            self.table.setCellWidget(loop, 6, self.button_exit)
            self.button_exit.clicked.connect(self.exitCall)
            loop = loop + 1



    def refreshhistory(self):
        self.table1.clearContents()
        data = self.dboperation.allvehicle()
        loop = 0
        self.table1.setRowCount(len(data))
        self.table1.setColumnCount(7)
        for smalldata in data:
            self.table1.setItem(loop, 0, QTableWidgetItem(str(smalldata[0])))
            self.table1.setItem(loop, 1, QTableWidgetItem(str(smalldata[1])))
            self.table1.setItem(loop, 2, QTableWidgetItem(str(smalldata[6])))
            self.table1.setItem(loop, 3, QTableWidgetItem(str(smalldata[2])))
            self.table1.setItem(loop, 4, QTableWidgetItem(str(smalldata[7])))
            self.table1.setItem(loop, 5, QTableWidgetItem(str(smalldata[3])))
            self.table1.setItem(loop, 6, QTableWidgetItem(str(smalldata[4])))
            loop = loop + 1



    def addhistory(self):
        data = self.dboperation.allvehicle()
        self.table1 = QTableWidget()
        self.table1.setRowCount(len(data))
        self.table1.setStyleSheet("background:#fff")
        self.table1.setColumnCount(7)

        button=QPushButton("REFRESH")
        button.setStyleSheet("color:#fff;padding:8px 0px;font-size:20px;background:green;border:1px solid white")
        button.clicked.connect(self.refreshhistory)

        self.table1.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
        self.table1.setHorizontalHeaderItem(0, QTableWidgetItem("ID"))
        self.table1.setHorizontalHeaderItem(1, QTableWidgetItem("NAME OF OWNER "))
        self.table1.setHorizontalHeaderItem(2, QTableWidgetItem("VEHICLE NO"))
        self.table1.setHorizontalHeaderItem(3, QTableWidgetItem("MOBILE NO"))
        self.table1.setHorizontalHeaderItem(4, QTableWidgetItem("VEHICLE TYPE"))
        self.table1.setHorizontalHeaderItem(5, QTableWidgetItem("ENTRY TIME "))
        self.table1.setHorizontalHeaderItem(6, QTableWidgetItem("EXIT TIME"))

        loop = 0
        for smalldata in data:
            self.table1.setItem(loop, 0, QTableWidgetItem(str(smalldata[0])))
            self.table1.setItem(loop, 1, QTableWidgetItem(str(smalldata[1])))
            self.table1.setItem(loop, 2, QTableWidgetItem(str(smalldata[6])))
            self.table1.setItem(loop, 3, QTableWidgetItem(str(smalldata[2])))
            self.table1.setItem(loop, 4, QTableWidgetItem(str(smalldata[7])))
            self.table1.setItem(loop, 5, QTableWidgetItem(str(smalldata[3])))
            self.table1.setItem(loop, 6, QTableWidgetItem(str(smalldata[4])))
            loop = loop + 1

            self.frame5 = QFrame()
            self.layout1 = QVBoxLayout()
            self.layout1.setContentsMargins(0,0,0,0)
            self.layout1.setSpacing(0)
            self.layout1.addWidget(button)
            self.layout1.addWidget(self.table1)
            self.frame5.setLayout(self.layout1)
            self.frame5.setContentsMargins(0,0,0,0)
            self.frame5.setMaximumWidth(self.width())
            self.frame5.setMinimumWidth(self.width())

            self.vertical_4.addWidget(self.frame5)
            self.vertical_4.addStretch()

    def exitCall(self):
        btton=self.sender()
        if btton:
            row=self.table.indexAt(btton.pos()).row()
            id=str(self.table.item(row,0).text())
            self.dboperation.exitvehicle(id)
            self.table.removeRow(row)








