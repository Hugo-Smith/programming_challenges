from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        l_po = 0
        r_po = len(height) -1
        max_water = 0

        while r_po > l_po:
            dist = r_po - l_po
            curr_water = dist* min(height[r_po],height[l_po])

            max_water = max(max_water, curr_water)

            if height[r_po] < height[l_po]:
                r_po -= 1
            else:
                l_po += 1
        
        return max_water

                
           
        
    
    
def main():
    arr = [1,8,6,2,5,4,8,3,7]
    s = Solution()
    print(s.maxArea(arr))

if __name__ == '__main__':
    main()