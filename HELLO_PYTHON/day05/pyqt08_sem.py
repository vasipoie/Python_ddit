import sys

from PyQt5 import uic
from PyQt5.QtWidgets import *
from random import random


form_class = uic.loadUiType("pyqt08.ui")[0]

class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        self.pb1.clicked.connect(self.myclick)
        self.pb2.clicked.connect(self.myclick)
        self.pb3.clicked.connect(self.myclick)
        self.pb4.clicked.connect(self.myclick)
        self.pb5.clicked.connect(self.myclick)
        self.pb6.clicked.connect(self.myclick)
        self.pb7.clicked.connect(self.myclick)
        self.pb8.clicked.connect(self.myclick)
        self.pb9.clicked.connect(self.myclick)
        self.pb0.clicked.connect(self.myclick)
        
        self.pb_call.clicked.connect(self.mycall)
        
    def myclick(self):
        str_new = self.sender().text()
        str_old = self.le.text()
        
        self.le.setText(str_old+str_new)
        print(str_new)
        print(str_old)
        
    def mycall(self):
        str_tel = self.le.text()
        QMessageBox.about(self, 'calling', str_tel)
        
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()