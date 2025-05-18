"""
Given a string s, find the length of the longest substring without duplicate characters.
"""

class Solution:
    def longest_unique_substring(s: str) -> int:
        start = 0
        max_len = 0
        seenChar = {}

        for i in range(len(s)):

            if s[i] in seenChar and seenChar[s[i]] >= start:
                start = seenChar[s[i]] + 1
                
            seenChar[s[i]] = i
            max_len = max(max_len, i - start + 1)

        return max_len 