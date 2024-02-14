import sys

from PyQt5 import uic
from PyQt5.QtWidgets import *
from random import random


form_class = uic.loadUiType("pyqt04.ui")[0]

class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        self.pb.clicked.connect(self.myclick)
        
    def myclick(self):
        arr = list(range(1,45+1))
        for i in range(1,1000+1):
            rnd = int(random()*45)
            a = arr[0]
            arr[0] = arr[rnd]
            arr[rnd] = a
        
        six = list(range(0,6))
        
        for x in range(0,6):
            six[x] = arr[x]
            
        self.lc01.display(six[0])
        self.lc02.display(six[1])
        self.lc03.display(six[2])
        self.lc04.display(six[3])
        self.lc05.display(six[4])
        self.lc06.display(six[5])
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()