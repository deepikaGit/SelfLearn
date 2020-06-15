from functools import reduce
def person(name , **data):
    print(name)
    for i,j in data.items():
        print("Key: ",i," value: ",j)

person("Deepika",age="26", mob ="89797664", Gender ="F")

# list function

lst = list(range(1,15,2))
print(lst)
def count(lst):
    even = 0
    odd = 0
    for i in lst:
        if i %2 == 0:
            even += 1
        else:
            odd += 1
    return even, odd   


even , odd =count(lst)
print("Even: ", even, "Odd: ", odd)

# fibonacci series

def fibbo(n):
    a = 0
    b = 1
    if n < 0:
        print("Invalid input")
    else:
        print(a)
        print(b)
        for i in range(2,n):
            c = a + b
            if c > n:
                break
            a = b
            b = c
            print(c)

fibbo(3)
#Lambda function

f = lambda a : a*a
e = lambda a,b : a+b
res = f(4)
adr = e(5,6)
print("lambda square:",res)
print("lambda add:",adr)

# Filter , map, reduce

lst = list(range(1,10))
iseven = lambda a : a%2 == 0
res = list(filter(iseven,lst))
doubles = list(map(lambda a : a*2, lst))
sum = reduce(lambda a ,b : a+b ,lst)
print("Even: ",res)
print("Doubles:",doubles)
print("Sum",sum)