# 첫 수를 입력하시오 1
# 끝 수를 입력하시오 10
# 1에서 10까지의 합은 55입니다.

a = input("첫 수를 입력하시오 ")
b = input("끝 수를 입력하시오 ")
sum = 0
for i in range(int(a),int(b)+1):
    sum += i
print("{}에서 {}까지의 합은 {}입니다.".format(a,b,sum))
