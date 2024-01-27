# 출력할 단 수를 넣으세요 4
# 4*1=4
# 4*9=36


dan = int(input("출력할 단 수를 넣으세요 "))

for i in range(1,9+1):
    print("{}*{}={}".format(dan,i,dan*i))
