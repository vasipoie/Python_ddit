class Animal:
    def __init__(self):
        self.age = 1
    def go1year(self):
        self.age += 1
        
class Human(Animal):
    def __init__(self):
        super().__init__()
        self.flag_w = False
    def momstouch(self):
        self.flag_w = True

if __name__ == '__main__':
    h = Human()
    print("flag_w : ",h.flag_w)
    print("age : ",h.age)
    h.go1year()
    h.momstouch()
    print("flag_w : ",h.flag_w)
    print("age : ",h.age)
    
    