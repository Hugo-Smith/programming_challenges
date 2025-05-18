class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ''
        start = -1
        sublen = 0
        low = 0
        high = 0
        length = len(s)

        for i in range(length):

            for j in range(2):
                low = i
                high = i + j

                while low >= 0 and high < length and s[high] == s[low]:
                    currlen = high-low +1

                    if currlen > sublen:
                        start = low
                        sublen = high - low + 1 
                    high += 1
                    low -= 1

        if start > -1:
            res = s[start: start+sublen]
        
        return res
