import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic, QtGui
from PyQt5.Qt import QPixmap

form_class = uic.loadUiType("pyomok01.ui")[0]

class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pb.clicked.connect(self.myclick2)
        self.pb2.clicked.connect(self.myclick2)
        
    def myclick2(self):
        self.sender().setIcon(QtGui.QIcon('1.png'))
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()