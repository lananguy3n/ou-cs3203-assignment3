import math
import array as arr

def main():
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

    #Product Function !!!!
    def _prod(arr):
        prod = 0

        for i in arr:
            prod = prod + i

            return (prod)

    # Array length !!
    n = len(list)
    
    product = math.prod(list)
    
    #Print product
    print('Product of the array is ', product)

    #Print reverse function
    list.reverse()
    print("Reversed list: ", list)

if __name__ == "__main__":
    main()



