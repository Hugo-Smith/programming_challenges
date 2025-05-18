"""
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this:

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:
"""

class Solution:
    def zigzagConversion(self, s: str, rows: int) -> str:
        res = ''

        if rows <= 1:
            return s

        num_rows = ['']*rows
        step = 1
        curr_row = 0

        for c in s:
            if curr_row == 0:
                num_rows[curr_row] += c
                step = 1
                curr_row += step

            elif curr_row == rows -1:
                num_rows[curr_row] += c
                step = -1
                curr_row += step
            else:
                num_rows[curr_row] += c
                curr_row += step

        res = ''.join(num_rows)
        
        return res


def main():
    s = '123456789ab'
    r= 3
    s2 = "PAYPALISHIRING"
    r2 =4
    sol = Solution()
    print(sol.zigzagConversion(s,r))
    print(sol.zigzagConversion(s2, r2))
    

if __name__ == '__main__':
    main()