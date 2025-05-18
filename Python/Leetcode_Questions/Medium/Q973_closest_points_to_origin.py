"""
Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane and an integer k, return the k closest points to the origin (0, 0).

The distance between two points on the X-Y plane is the Euclidean distance (i.e., √(x1 - x2)2 + (y1 - y2)2).

You may return the answer in any order. The answer is guaranteed to be unique (except for the order that it is in).
"""

from typing import List
from math import sqrt
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dist_lst = []
        res = []

        for x,y in points:
            curr_dist = sqrt((x**2)+ (y**2))
            dist_lst.append([[x,y],curr_dist])
        print(dist_lst)
        dist_lst.sort(key=lambda x: x[1])
        print(f'Sorted: f{dist_lst}')
        for i in range(k):
            res.append(dist_lst[i][0])
        
        return res

def main():
    s = Solution()
    points = [[3,3],[5,-1],[-2,4]]
    print(s.kClosest(points,2))

if __name__ == '__main__':
    main()