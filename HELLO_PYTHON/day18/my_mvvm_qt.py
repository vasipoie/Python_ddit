import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
from day18.daobus import DaoBus
from day18.daobline import DaoBLine


form_class = uic.loadUiType("my_mvvm_qt.ui")[0]

class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.db = DaoBus()
        self.dbl = DaoBLine()
        self.driver= webdriver.Chrome()
        self.driver.get('https://topis.seoul.go.kr/map/openBusMap.do')
        
        self.setupUi(self)
        self.pb_one.clicked.connect(self.myclick)
        
    def myclick(self):
        try:
            div = self.driver.find_elements(By.CSS_SELECTOR, "#pop_content")[0]
            span = div.find_elements(By.CSS_SELECTOR, "span")[0]
            strong = div.find_elements(By.CSS_SELECTOR, "strong")[0]
            
            updown = "1"
            tab0 = self.driver.find_elements(By.CSS_SELECTOR, ".tabs")[0]
            li0 = tab0.find_elements(By.CSS_SELECTOR, "li")[0]
            str_class = li0.get_attribute('class')
            if str_class == "active":
                updown = "0"
            bus_id = span.text+"_"+strong.text+"_"+updown
            print(bus_id)
            
            table = self.driver.find_elements(By.CSS_SELECTOR, ".tby03")[0]
            tbody = table.find_elements(By.CSS_SELECTOR, "tbody")[0]
            tr = tbody.find_elements(By.CSS_SELECTOR, "tr")[0]
            td = tr.find_elements(By.CSS_SELECTOR, "td")[1]
            my_minute = td.text.replace("분","");
            print(my_minute)
            self.db.insert(bus_id, my_minute)
            
            ul = self.driver.find_elements(By.CSS_SELECTOR, ".busloclist")[0]
            lis = ul.find_elements(By.CSS_SELECTOR, "li")
            for idx,li in enumerate(lis):
                a = li.find_elements(By.CSS_SELECTOR, "a")[0]
                str_all = a.get_attribute('onclick')
                str_right = str_all.split("(")[1]
                str_info = str_right.split(")")[0]
                # print(str_info)
                
                arr_info = str_info.split(",")
                # print(arr_info)
                
                s_id = arr_info[0].replace("\"","").strip()
                s_name = arr_info[1].replace("\"","").strip()
                lng = arr_info[2].replace("\"","").strip()
                lat = arr_info[3].replace("\"","").strip()
                nod = arr_info[6].replace("\"","").strip()
                print(idx,s_id,s_name,lng,lat,nod)
            
                self.dbl.insert(bus_id, idx, s_id, s_name, lng, lat, nod)
            
        except:
            print("에러발생")
        
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()