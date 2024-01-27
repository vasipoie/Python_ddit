class Moon:
    def __init__(self):
        self.cnt_book = 10000
        self.money = 10000
    
    def sell(self,cnt):
        self.money += cnt*10000
        self.cnt_book -= cnt
    
class JDragon:
    def __init__(self):
        self.cnt_factory = 20
    
    def buildFactory(self): 
        self.cnt_factory += 1
        
class ChaEunWoo:
    def __init__(self):
        self.cnt_cm = 10
    
    def kki(self):
        self.cnt_cm += 1
        
        
class YS(Moon, JDragon, ChaEunWoo):
    def __init__(self):
        Moon.__init__(self)
        JDragon.__init__(self)
        ChaEunWoo.__init__(self)
    
if __name__ == '__main__':
    ys = YS()
    print("cnt_book :",ys.cnt_book)
    print("money :",ys.money)
    ys.sell(500)
    print("cnt_book :",ys.cnt_book)
    print("money :",ys.money)
    
    print("cnt_factory :",ys.cnt_factory)
    ys.buildFactory()
    print("cnt_factory :",ys.cnt_factory)
    
    print("cnt_cm :",ys.cnt_cm)
    ys.kki()
    print("cnt_cm :",ys.cnt_cm)
    
    
    