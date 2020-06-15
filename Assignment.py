from numpy import array
# Adding two array using for loop
a = array([2,1,4,5,3])
b = array([8,4,0,2,3])

for i in range(5):
    temp = a[i] + b[i]
    print(temp,end=" ")

# Max value from an array
max = a[0]
for i in range(1,5):
    if max < a [i]:
        max = a[i]
print(max) 
