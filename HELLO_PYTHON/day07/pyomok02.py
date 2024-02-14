import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic, QtGui
from PyQt5.Qt import QPixmap, QSize

form_class = uic.loadUiType("pyomok02.ui")[0]

class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.flag = True
        self.btn = []
        self.setupUi(self)
        
        for i in range(10):
            for j in range(10):
                btn = QPushButton("", self)
                btn.setIcon(QtGui.QIcon('0.png'))
                btn.setIconSize(QSize(40, 40))
                btn.setGeometry(40*i,40*j,40,40)
                btn.clicked.connect(self.myclick2)
        
        self.pb.clicked.connect(self.myreset)
        
    def myreset(self):
         for i in range(10):
            for j in range(10):
                self.btn = QPushButton("", self)
                self.btn.setIcon(QtGui.QIcon('0.png'))
                self.btn.setIconSize(QSize(40, 40))
                self.btn.setGeometry(40*i,40*j,40,40)
        
    def myclick2(self):
        if self.flag:
            self.sender().setIcon(QtGui.QIcon('1.png'))
        else :
            self.sender().setIcon(QtGui.QIcon('2.png'))
        self.flag = not self.flag
            
if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()