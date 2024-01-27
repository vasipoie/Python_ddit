# 첫 수를 입력하시오 1
# 끝 수를 입력하시오 10
# 배수를 입력하시오 5
# 1에서 10까지의 5의 배수의 합은 15입니다.

fir = input("첫 수를 입력하시오 ")
las = input("끝 수를 입력하시오 ")
bae = input("배수를 입력하시오 ")
sum = 0

for i in range(int(fir), int(las)+1):
    if(i%int(bae)==0):
       sum += i 

print("{}에서 {}까지의 {}의 배수의 합은 {}입니다.".format(fir, las, bae, sum))