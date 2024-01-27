#첫 수를 입력하시오 5
#끝 수를 입력하시오 6
#5와 6의 합은 11입니다.

a = input("첫 수를 입력하시오 ")
b = input("끝 수를 입력하시오 ")
print()
c = int(a)
d = int(b) 
print(c)
print(d)
sum = c+d
print(sum)
print()
print(a+"와 "+b+"의 합은 "+str(sum)+"입니다.")
print(a+"와 "+b+"의 합은 "+str(int(a)+int(b))+"입니다.")

print("{}과 {}의 합은 {}입니다.".format(a,b,c+d))