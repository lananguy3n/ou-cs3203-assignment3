import math

#Get input as list from user
list = [] #Initalize Empty List

n=int(input("Number of elements: "))

for i in range (0,n):       #Loop to iterate until given input range
        e = int(input())
        list.append(e)

print (list)

#Sum Function
def _sum(arr):
    sum = 0     #Loop to iterate through each number in array
 
    for i in arr:
        sum = sum + i
 
    return(sum)
 
 
# Array length
n = len(list)
 
ans = _sum(list)
 
#Print sum
print('Sum of the array is ', ans)

