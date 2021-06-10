import sys
import os
from InstallWindow import InstallWindow
from loginwindow import loginscreen
from PyQt5.QtWidgets import QApplication,QSplashScreen,QLabel
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt,QTimer

class MainScreen():
    def showsplashscreen(self):
        self.pix=QPixmap("veh.png")
        self.splassh=QSplashScreen(self.pix,Qt.WindowStaysOnTopHint)
        self.splassh.show()


def showsetupwindow():
    mainScreen.splassh.close()
    installWindow.show()

def showloginwindow():
    mainScreen.splassh.close()
    login.showloginscreen()


app=QApplication(sys.argv)
login=loginscreen()
mainScreen=MainScreen()
mainScreen.showsplashscreen()
installWindow=InstallWindow()

if os.path.exists("./config.json"):
    QTimer.singleShot(2000,showloginwindow)
else:
    QTimer.singleShot(2000,showsetupwindow)

sys.exit(app.exec_())