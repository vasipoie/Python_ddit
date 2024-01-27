# 홀/짝을 입력하시오 홀
# 나 : 홀
# 컴 : 짝
# 결과 :  짐
from random import random

my = input("홀/짝을 입력하시오 ")

com = random()
if com > 0.5:
    com = "홀"
else:
    com = "짝"

res = ""

if my == com:
    res = "이김"
elif my != com:
    res = "짐"
 
print("나 : {}".format(my))   
print("컴 : {}".format(com))   
print("결과 : {}".format(res))   
