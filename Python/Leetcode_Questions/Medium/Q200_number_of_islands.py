"""
Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), 
return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally
or vertically. You may assume all four edges of the grid are all surrounded by water.
"""
"""
Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), 
return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally
or vertically. You may assume all four edges of the grid are all surrounded by water.
"""
from typing import List
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        cols = len(grid[0])
        rows = len(grid)

        visited = []
        res = 0

        def dfs(r,c):
            if [r,c] in visited:
                return
            visited.append([r,c])

            directions = [[1,0], [-1,0], [0,1], [0,-1]]
            for dr, dc in directions:
                nr = r + dr
                nc = c + dc
                if nr in range(rows) and nc in range(cols) and grid[nr][nc] == '1':
                    dfs(nr, nc) 

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1' and [r,c] not in visited:
                    res += 1
                    dfs(r,c)
        return res