"""
Given an integer array nums, return all the triplets [nums[i], nums[j], 
nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.
"""
"""
Didn't think of the right solution, reattempt at some stage... close though!
"""
from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        lp = 0
        rp = len(nums)-1
        nums.sort()
        res = []

        while lp < len(nums):
            
            for i in range( rp, lp, -1):
                sum = nums[lp]
                sum += nums[i]
                num_to_find = 0 - sum

                if num_to_find in nums[lp+1:i]:
                    lst_chk = [nums[lp], nums[i], num_to_find]
                    
                    if lst_chk not in res:
                        res.append(lst_chk)
                    continue
            lp += 1
        
        return res
                    


            
