class Pen:
    def __init__(self):
        self.volume = 20
        #print("생성자")
    def write(self):
        self.volume -= 1
    def __del__(self):
        #print("소멸자")
        pass
    def __str__(self):
        return "volume:"+str(self.volume)


class BallPen(Pen):
    def __init__(self):
        super().__init__()
        self.flag = False
    def toktak(self):
        self.flag = not self.flag

if __name__ == '__main__':
    bp = BallPen()
    print("volume",bp.volume)
    print("flag",bp.flag)
    bp.write()
    bp.toktak()
    print("volume",bp.volume)
    print("flag",bp.flag)
    


