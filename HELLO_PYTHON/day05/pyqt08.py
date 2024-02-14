import sys

from PyQt5 import uic
from PyQt5.QtWidgets import *
from random import random


form_class = uic.loadUiType("pyqt08.ui")[0]

class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        self.pb1.clicked.connect(self.myclick1)
        self.pb2.clicked.connect(self.myclick2)
        self.pb3.clicked.connect(self.myclick3)
        self.pb4.clicked.connect(self.myclick4)
        self.pb5.clicked.connect(self.myclick5)
        self.pb6.clicked.connect(self.myclick6)
        self.pb7.clicked.connect(self.myclick7)
        self.pb8.clicked.connect(self.myclick8)
        self.pb9.clicked.connect(self.myclick9)
        self.pb0.clicked.connect(self.myclick0)
        self.pb_call.clicked.connect(self.mycall)
        
    def myclick1(self):
        self.le.setText(self.le.text()+str(1))
    def myclick2(self):
        self.le.setText(self.le.text()+str(2))
    def myclick3(self):
        self.le.setText(self.le.text()+str(3))
    def myclick4(self):
        self.le.setText(self.le.text()+str(4))
    def myclick5(self):
        self.le.setText(self.le.text()+str(5))
    def myclick6(self):
        self.le.setText(self.le.text()+str(6))
    def myclick7(self):
        self.le.setText(self.le.text()+str(7))
    def myclick8(self):
        self.le.setText(self.le.text()+str(8))
    def myclick9(self):
        self.le.setText(self.le.text()+str(9))
    def myclick0(self):
        self.le.setText(self.le.text()+str(0))
        
    def mycall(self):
        QMessageBox.information(self, "ok", "calling"+"\n"+self.le.text())
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()