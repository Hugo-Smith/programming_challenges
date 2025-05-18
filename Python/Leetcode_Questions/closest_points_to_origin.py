"""
Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane and an integer k, 
return the k closest points to the origin (0, 0).

The distance between two points on the X-Y plane is the Euclidean distance (i.e., √(x1 - x2)2 + (y1 - y2)2).

You may return the answer in any order. The answer is guaranteed to be unique (except for the order that it is in).
"""
from typing import List
from math import sqrt

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        dist_dict = {}
        dist_lst =[]
        res = []

        for i in range(len(points)):
            x, y= points[i][0],  points[i][1]
            
            dist = sqrt(x**2 + y**2)
            dist_lst.append(dist)
            dist_dict[x,y] = dist
        dist_lst.sort()
        dist_lst.pop(k,len(points))

        
    


