import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic, QtGui
from PyQt5.Qt import QPixmap, QMouseEvent, QSize, Qt
from sqlalchemy.sql.expression import false

form_class = uic.loadUiType("pyomok04_19.ui")[0]

class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.flag_bw = True
        self.flag_over = False
        self.arr2d=[
            [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0, 0,0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0, 0,0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0, 0,0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0, 0,0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0, 0,0,0,0,0],
            
            [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0, 0,0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0, 0,0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0, 0,0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0, 0,0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0, 0,0,0,0,0],
            
            [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0, 0,0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0, 0,0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0, 0,0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0, 0,0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0, 0,0,0,0,0],
            
            [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0, 0,0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0, 0,0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0, 0,0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0, 0,0,0,0,0],
        ]
        self.pb2d = []
        
        
        self.setupUi(self)
        for i in range(19):
            line = []
            for j in range(19):
                btn = QPushButton("", self)
                btn.setIcon(QtGui.QIcon('0.png'))
                btn.setIconSize(QSize(40,40))
                btn.setGeometry(j*40,i*40,40,40)
                btn.setToolTip("{},{}".format(i,j))
                btn.clicked.connect(self.myclick)
                line.append(btn)
            self.pb2d.append(line)
                
        self.pb.clicked.connect(self.myreset)
        self.myrender()
        
    def myreset(self):
        for i in range(19):
            for j in range(19):
                self.arr2d[i][j]=0
        self.flag_over = False
        self.flag_bw = True
        self.myrender()
    
    
    def myrender(self):
        for i in range(19):
            for j in range(19):
                if self.arr2d[i][j] == 0:
                    self.pb2d[i][j].setIcon(QtGui.QIcon('0.png'))
                if self.arr2d[i][j] == 1:
                    self.pb2d[i][j].setIcon(QtGui.QIcon('1.png'))
                if self.arr2d[i][j] == 2:
                    self.pb2d[i][j].setIcon(QtGui.QIcon('2.png'))
        
        
    def getUp(self,i,j,stone):
        ret = 0
        try:
            while True:
                # print("up i",i)
                i -= 1
                if i < 0:
                    return ret
                if self.arr2d[i][j] == stone: 
                    ret += 1
                else:
                    return ret
        except:
            return ret
                
    def getDw(self,i,j,stone):
        ret = 0
        try:
            while True:
                # print("dw i",i)
                i += 1
                if i < 0:
                    return ret
                if self.arr2d[i][j] == stone: 
                    ret += 1
                else:
                    return ret
        except:
            return ret
        
    def getLe(self,i,j,stone):
        ret = 0
        try:
            while True:
                j -= 1
                if j < 0:
                    return ret
                if self.arr2d[i][j] == stone: 
                    ret += 1
                else:
                    return ret
        except:
            return ret
        
    def getRi(self,i,j,stone):
        ret = 0
        try:
            while True:
                j += 1
                if j < 0:
                    return ret
                if self.arr2d[i][j] == stone: 
                    ret += 1
                else:
                    return ret
        except:
            return ret
        
    def getUl(self,i,j,stone):
        ret = 0
        try:
            while True:
                i -= 1
                j -= 1
                if i < 0:
                    return ret
                if j < 0:
                    return ret
                if self.arr2d[i][j] == stone: 
                    ret += 1
                else:
                    return ret
        except:
            return ret
        
    def getUr(self,i,j,stone):
        ret = 0
        try:
            while True:
                i -= 1
                j += 1
                if i < 0:
                    return ret
                if j < 0:
                    return ret
                if self.arr2d[i][j] == stone: 
                    ret += 1
                else:
                    return ret
        except:
            return ret
        
    def getDl(self,i,j,stone):
        ret = 0
        try:
            while True:
                i += 1
                j -= 1
                if i < 0:
                    return ret
                if j < 0:
                    return ret
                if self.arr2d[i][j] == stone: 
                    ret += 1
                else:
                    return ret
        except:
            return ret
        
    def getDr(self,i,j,stone):
        ret = 0
        try:
            while True:
                i += 1
                j += 1
                if i < 0:
                    return ret
                if j < 0:
                    return ret
                if self.arr2d[i][j] == stone: 
                    ret += 1
                else:
                    return ret
        except:
            return ret
    
    def myclick(self):
        if self.flag_over:
            return
        str_ij = self.sender().toolTip()
        arr_ij = str_ij.split(",")
        i = int(arr_ij[0])
        j = int(arr_ij[1])
        # 자리에 이미 돌이 있다면 (0보다 크다면? 무시!)
        if self.arr2d[i][j] > 0:
            return
        
        stone = -1
        if self.flag_bw:
            self.arr2d[i][j] = 1
            stone = 1
        else:
            self.arr2d[i][j] = 2
            stone = 2
            
        up = self.getUp(i,j,stone)
        dw = self.getDw(i,j,stone)
        le = self.getLe(i,j,stone)
        ri = self.getRi(i,j,stone)
        ul = self.getUl(i,j,stone)
        ur = self.getUr(i,j,stone)
        dl = self.getDl(i,j,stone)
        dr = self.getDr(i,j,stone)
        print("up",up)
        print("dw",dw)
        print("le",le)
        print("ri",ri)
        print("ul",ul)
        print("ur",ur)
        print("dl",dl)
        print("dr",dr)
        print("--------")
        
        d1 = up+dw+1
        d2 = le+ri+1
        d3 = ul+dr+1
        d4 = ur+dl+1
        
        self.myrender()
        
        if d1 == 5 or d2 == 5 or d3==5 or d4==5:
            self.flag_over = True
            if self.flag_bw:
                QMessageBox.about(self,'오목','게임 종료~! 흑돌 승!')
            else:
                QMessageBox.about(self,'오목','게임 종료~! 백돌 승!')
                
        self.flag_bw = not self.flag_bw
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()