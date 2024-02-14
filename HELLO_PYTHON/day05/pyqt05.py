import sys

from PyQt5 import uic
from PyQt5.QtWidgets import *
from random import random


form_class = uic.loadUiType("pyqt05.ui")[0]

class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        self.pb.clicked.connect(self.myclick)
        
    def getStar(self, cnt):
        ret = ""
        for i in range(cnt):
            ret += "♥"
        ret += "\n"
        return ret
        
    def myclick(self):
        print(self.lbl_first.text())
        
        f = int(self.le_first.text())
        l = int(self.le_last.text())
        print(f)
        print(l)
        
        txt = ""
        
        # txt += self.getStar(1)
        # txt += self.getStar(2)
        
        for i in range(f,l+1):
            txt += self.getStar(i)
        
        self.pte.setPlainText(txt)
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()