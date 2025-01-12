from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel, QPushButton
from PyQt5 import uic
import sys
import camera
from camera import showVideo

class UI(QMainWindow):
        def __init__(self):
                super(UI, self).__init__()
                
                # Load UI
                uic.loadUi('main.ui', self)
                self.show()
                
                self.SignInBtn.clicked.connect(self.SignInTask)
                self.SignOutBtn.clicked.connect(self.SignOutTask)
                
        def SignInTask(self):
                name = "Md Arifin Ahmed Rafi"
                id = "1024343A"
                intime="10:34"
                self.nameLabel.setText(f"Name: {name}")
                self.IdLabel.setText(f"Name: {id}")
                self.SignInTime.setText(f"Sign In Time: {intime}")
                
                
                
        def SignOutTask(self):
                print("SignOut print")
        
app = QApplication(sys.argv)
UIWindow=UI()
app.exec_()