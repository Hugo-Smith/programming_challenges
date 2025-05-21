"""
Given an integer array nums of length n and an integer target, find three integers in nums such that the sum is closest to target.

Return the sum of the three integers.

You may assume that each input would have exactly one solution.
"""
from typing import List

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        res = nums[0] + nums[1] + nums[2]
        min_dist = abs(target - res)

        for i in range(len(nums)):
            tmp = 0
            lp = i +1
            rp = len(nums)-1
                
            while lp < rp:
                tmp = nums[i] + nums[lp] + nums[rp] 

                if abs(tmp - target) < min_dist:
                    min_dist = abs(tmp - target)
                    res = tmp
                if tmp < target:
                    lp += 1
                elif tmp > target:
                    rp -= 1
                else:
                    return tmp  
        return res
        
def main():
    s = Solution()

    nums = [0,1,2]
    target = 0    
    print(s.threeSumClosest(nums, target))

if __name__ == '__main__':
    main()


                


        