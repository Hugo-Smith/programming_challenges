from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        
        length = len(nums)
        if target > nums[-1]:
            return length
        for i in range(length):

            if nums[i] == target:
                return i
            elif nums[i] >= target:
                return i
            else:
                continue
        return -1
