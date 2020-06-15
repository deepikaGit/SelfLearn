from numpy import array
from numpy import logspace
from numpy import linspace
from numpy import zeros
from numpy import ones
from numpy import arange
from numpy import sqrt
from numpy import sin
from numpy import log10
from numpy import sort
from numpy import square
from numpy import concatenate
from numpy import matrix
from numpy import diagonal
#Declaring 1D array
arr = array([1,2,3,4,5,6,7])
print("Array :", end ="")
print(arr)
#Printing its type
print("Array Type:", end ="")
print(arr.dtype)
#When only 1 float is there auto conversion happens
arr1 = array([1,2,3,4,5.0])
print("Array Auto conversion:", end ="")
print(arr1)
print(arr1.dtype)
#linspace(start,stop,part)
arr2 = linspace(0,16,17)
print("linspace :", end ="")
print(arr2)
#logspace(start, stop, part) - difference between values are of log
arr3 = logspace(1,10,8)
print("logspace :", end ="")
print(arr3)
print('%.2f'%arr3[0])
print('%.2f'%arr3[4])
#arange(start,stop,step)
arr2 = arange(0,15,2)
print(arr2)
#Zero's , specify int if u want array in int
arr5 = zeros(5)
print("Zero's default :", end ="")
print(arr5)
arr5 = zeros(5,int)
print("Zero's defining as int :", end ="")
print(arr5)
#One's , specify int if u want array in int
arr5 = ones(5)
print("One's default :", end ="")
print(arr5)
arr5 = ones(5,int)
print("One's defining as int :", end ="")
print(arr5)

########################
#### Array Addition ####
########################

arr = array([1,2,3,4,5])
arr1 = array([3,2,5,6,6])
#arr = arr + 2
arr2 = arr + arr1
print("Array Addition",end ="")
print(arr2)
print("Array min",end ="")
print(min(arr1))
print("Array max",end ="")
print(max(arr1))
print("Array sum",end ="")
print(sum(arr1))
print("Array sqrt",end ="")
print(sqrt(arr1))
print("Array sin",end ="")
print(sin(arr1))
print("Array log",end ="")
print(log10(arr1))
print("Array sort",end ="")
print(sort(arr1))
print("Array square",end ="")
print(square(arr1))
print("Array concatenation", end="")
print(concatenate([arr,arr1]))

#Copying an array
# shallow copy
arr6 = arr.view() 
#Deep copy
arr7 = arr.copy()
print(arr6)
print(id(arr6))
print(id(arr))
print(id(arr7))
arr[1] = 12
print(arr)
print(arr6)
print(arr7)


#### Multi dimensional Array

a = array( [
[5,3,6,4],
[1,5,6,3],
[4,5,5,6]] )

print(a.ndim)
print(a.shape)
b= a.flatten()
print(b)
c = a.reshape(3,4)
print("The array is ",c)

f1 = matrix('1 2 3 ; 4 5 6 ; 7 8 9')
f2 = matrix('1 2 3 ; 4 5 6 ; 7 8 9')
print("The diagonal of f1 is ", diagonal(f1))
print("Multiplication of matrix is ", f1*f2)
print("Max of matrix is ", f1.max())