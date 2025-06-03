"""
Given two strings s and t, return true if t is an anagram of s, and false otherwise.
"""
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # not much code but slow
        return sorted(s) == sorted(t)
    
    def solution2(self, s:str, t:str) -> bool:
        # slightly faster
        if len(s) != len(t):
            return False
        sa = sorted(s)
        ta = sorted(t)
        for i in range(len(s)):
            if sa[i] != ta[i]:
                return False
            
        return True

    
def main():
    sol = Solution()
    s = 'anagram'
    t = 'nagaram'
    a = 'rat'
    b = 'car'
    print(sol.isAnagram(s,t))
    print(sol.isAnagram(a,b))
    print(sol.solution2(s,t))

if __name__ == '__main__':
    main()