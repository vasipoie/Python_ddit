def showDan(dan):
    for i in range(1,9+1):
        dan * i
        print("{}x{}={}".format(dan, i, dan*i))
    
showDan(4)