from typing import List
class Solution:
    def twoPointers(self, nums: List[int], target: int) -> List[int]:
        left = 0
        right = len(nums) - 1

        while left < right:
            sum = nums[left] + nums[right]
            if sum > target:
                right -= 1
            elif sum < target:
                left += 1
            else:
                return [left, right]
        
        return []

    def removeDuplicates(self, arr: List[int]) -> int:
        if not arr:
            return 0

        left = 0  # Slow pointer

        for right in range(1, len(arr)):
            if arr[right] != arr[left]:
                left += 1
                arr[left] = arr[right]

        return left + 1
    

def main():
    s = Solution()
    target = 11
    arr =[1,2,3,5,9,12,14,90]
    arr2 = [1,2,3,4,4,5,6,7,7,8]

    print(s.twoPointers(arr,target))
    print(s.removeDuplicates(arr2))
    print(arr2)

if __name__ == '__main__':
    main()