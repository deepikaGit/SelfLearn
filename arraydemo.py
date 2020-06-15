from array import array 
arr = array('i',[2,7,12,4])
#Copying an array
newArr = array(arr.typecode,(a for a in arr))
#Getting input from user
val = int(input("How many elements would you like to add ?"))
for i in range(val):
    newArr.append(int(input("Value ?")))
# using for loop
for a in newArr:
    print(a)
#Remove element
r = int(input("Enter the element to be removed"))
newArr.remove(r)
# using for loop
for a in newArr:
    print(a)

