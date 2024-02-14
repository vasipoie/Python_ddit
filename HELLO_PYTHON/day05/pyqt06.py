import sys

from PyQt5 import uic
from PyQt5.QtWidgets import *
from random import random


form_class = uic.loadUiType("pyqt06.ui")[0]

class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        self.pb.clicked.connect(self.myclick)
        
    def myclick(self):
        f = int(self.le01.text())
        l = int(self.le02.text())
        b = int(self.le03.text())
        
        sum = 0
        
        for i in range(f, l+1):
            if(i % b == 0):
                sum += i
                
        print(sum)
        self.le04.setText(str(sum))
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()