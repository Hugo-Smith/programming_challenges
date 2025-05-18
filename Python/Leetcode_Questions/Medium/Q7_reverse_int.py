class Solution:
    def reverse(self, x: int) -> int:
        if x < 10 and x > -10:
            return x
        
        res = 0
        sign = -1 if x < 0 else 1
        
        numStr = str(x*sign)
        right = len(numStr) - 1

        res = int(numStr[::-1])

        if res> (2**31)-1:
            return 0
        else:
            return res*sign
        
def main():
    s = Solution()
    res = s.reverse(123)
    print(res)

if __name__ == '__main__':
    main()