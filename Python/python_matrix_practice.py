"""
Add two matrices of same size
"""
def add_matrices(mtx_1, mtx_2):
    res = []
    for x in range(len(mtx_1)):
        row = []
        for y in range(len(mtx_1[x])):

            row.append(mtx_1[x][y] + mtx_2[x][y])
        res.append(row)
    return res

"""
For a much more time efficient process you can convert to numpy arrays and use vectorised addition
e.g. np.array(mtx)  
     res = np_mtx + np_mtx_2 
"""
"""

"""


if __name__ == '__main__':
    X= [[1,2,3],
    [4 ,5,6],
    [7 ,8,9]]
 
    Y = [[9,8,7],
        [6,5,4],
        [3,2,1]]
    
    print(add_matrices(X,Y))