import math
num = 11
a = int(math.sqrt(num))
print(math.sqrt(num))
for i in range(2,a+1):
    if num % i == 0 :
        print("Not prime")
        break
else:
    print("prime")