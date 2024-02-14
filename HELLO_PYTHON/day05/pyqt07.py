import sys

from PyQt5 import uic
from PyQt5.QtWidgets import *
from random import random


form_class = uic.loadUiType("pyqt07.ui")[0]

class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        self.pb.clicked.connect(self.myclick)
        self.le_mine.returnPressed.connect(self.myclick)
        
    def myclick(self):
        me = self.le_mine.text()
        print(me)
        
        i = random()
        if(i>=0.66):
            com = self.le_com.setText("가위")
        elif(i>0.33 and i<0.66):
            com = self.le_com.setText("바위")
        else:
            com = self.le_com.setText("보")
                
        
        ccom = self.le_com.text()
        print(ccom)
                
        if(me==ccom):
            self.le_res.setText("비겼습니다")
        elif(me=="가위" and ccom=="바위"):
            self.le_res.setText("졌습니다")
        elif(me=="바위" and ccom=="보"):
            self.le_res.setText("졌습니다")
        elif(me=="보" and ccom=="가위"):
            self.le_res.setText("이겼습니다")
        elif(me=="바위"and ccom == "가위"):
            self.le_res.setText("이겼습니다")
        elif(me=="보"and ccom == "바위"):
            self.le_res.setText("이겼습니다")
        elif(me=="가위" and ccom=="보"):
            self.le_res.setText("이겼습니다")
        
        
        # mine = self.le_mine.text()
        # com = ""
        # result = ""
        #
        # rnd = random()
        # if rnd > 0.66 :
        #     com = "가위"
        # elif rnd > 0.33 :
        #     com = "바위"
        # else:
        #     com = "보"
        #
        # if mine == "가위" and com == "가위" : result="비김"
        # if mine == "가위" and com == "바위" : result="짐"
        # if mine == "가위" and com == "보" : result="이김"
        #
        # if mine == "바위" and com == "가위" : result="이김"
        # if mine == "바위" and com == "바위" : result="비김"
        # if mine == "바위" and com == "보" : result="짐"
        #
        # if mine == "보" and com == "가위" : result="짐"
        # if mine == "보" and com == "바위" : result="이김"
        # if mine == "보" and com == "보" : result="비김"
        #
        # self.le_com.setText(com)
        # self.le_result.setText(result)
        
        
        
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()