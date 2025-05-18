"""
Remove duplicates from a array sorted in increasing order,return the number 
of unique numbers and array with just the unique numbers
"""
from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 0
        numArray = []
        length = len(nums)

        for i in range(length-1):
            
            if nums[i] != nums[i+1]:
                k += 1
                numArray.append(nums[i])
            
            continue
        if nums[-1] != nums[-2]:
            k += 1
            numArray.append(nums[-1])
        
        return k, numArray

    def removeDupes(self, nums: List[int]) -> int:
        k = 0
        length = len(nums)
        for i in range(length-1):
            if nums[i] == nums[i+1]:
                nums[i] = 
                

def main():
    s = Solution()
    n = [0,0,1,1,1,2,2,3,3,4]
    k, nums = s.removeDuplicates(n)
    print("K: " + str(k))
    print(nums)
    
if __name__ == '__main__':
    main()
