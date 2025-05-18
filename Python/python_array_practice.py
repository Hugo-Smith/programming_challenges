"""
Array Questions
"""
#Find the sum of the individual parts of an array
def sum_array(lst):
    return sum(lst)

#find largest element in an array
def find_largest_in_array(lst):
    return max(lst)

#rotate numbers in an array
def rotate_array(lst):
    x = len(lst)
    new_lst = lst[1:x]
    new_lst.append(lst[0])
    return new_lst

#rotate array by certain number
def rotate_array_by_num(lst,n):
    return (lst[n:] + lst[:n])

#find remainer of array after multiplying
def mult_then_div_array(lst, n):
    total = 1
    for i in range(len(lst)):
        total = total * lst[i]
    return total%n

#check if an array is monotonic (constant equal/increase/decrease)
def check_monotonic_array(arr):
    return all(arr[i] <= arr[i+1] for i in range(len(arr)-1)) or \
           all(arr[i] >= arr[i+1] for i in range(len(arr)-1))


def maxSubarraySum(arr):
    res = arr[0]
  
    # Outer loop for starting point of subarray
    for i in range(len(arr)):
        currSum = 0
      
        # Inner loop for ending point of subarray
        for j in range(i, len(arr)):
            currSum = currSum + arr[j]
          
            # Update res if currSum is greater than res
            res = max(res, currSum)
          
    return res

"""
Interview question to find the amount of water that would collect in an area.
The array represents the height of objects in the area, you must find the water between them
eg. [4, 0, 2] would look like []
                              []
                              []      []
                              []      []
                              ##########
In this case it would store 2 water.
"""
def findWater(arr):
    #first initialise the left & right arrays
    n = len(arr)
    leftArr  = [0] * n
    rightArr = [0] * n
    res = 0

    leftArr[0] = arr[0]
    rightArr[n-1] = arr[-1]

    #populate the max left value array
    for i in range(1, n):
        leftArr[i] = max(arr[i],leftArr[i-1])
    
    #populate the max right value array
    for i in range(n-2, -1, -1):
        rightArr[i] = max(arr[i], rightArr[i+1])
    
    for i in range(1, n-1):
        lesser = min(leftArr[i-1], rightArr[i+1])
        if lesser > arr[i]:
            res += lesser - arr[i]
    
    return res

"""
Function to find the majority element of an array determined by whether it appears 
more than the arr.size()/2 times in the array. If no majority is found it returns -1
Can use a hash map to achieve a better time complexity but worse space complexity
"""
def majorityElement(arr):
    copyArr = arr.copy()
    
    copyArr.sort()
    res = -1
    count = 0

    for i in range(1, len(copyArr)):
        
        if copyArr[i -1] == copyArr[i]:
            count += 1
        else:
            if count > len(copyArr) // 2:
                return copyArr[i-1]
            count = 1
    
    #check the last element in the array
    if count > len(copyArr) // 2:
        return copyArr[-1]
    return -1

"""
Function to construct a product array res[] (of the same size) such that res[i] is 
equal to the product of all the elements of arr[] except arr[i]. 
"""
def productConstruct(arr):

    n = len(arr)
    totalProduct = arr[0]
    res = [0] * n

    for i in range(1, n):
        totalProduct *= arr[i]

    for i in range(0, n):
        res[i] = totalProduct//arr[i]
    
    return res

if __name__ == '__main__':
    lst = [1,2,3,4,5]
    big_lst = [1,2,3,4,5,6,7,8,9,10]
    arr = [2, 3, -8, 7, -1, 2, 3]
    rainArr = [5,0,1,4,0,2]
    input = [10,3,5,6,2]

    #print(find_largest_in_array(lst))
    #print(rotate_array(lst))
    #print(rotate_array_by_num(big_lst,3))
    #print(mult_then_div_array(lst, 7))
    #print(maxSubarraySum(arr))
    print(findWater(rainArr))
    print(productConstruct(input))
