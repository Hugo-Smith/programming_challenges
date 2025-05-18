class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        strip_string =s.strip()
        num = 0
        for char in strip_string[::-1]:
            if char == " ":
                break
            num += 1
        return num
    
class Alt:
    def lengthOfLastWord(self, s: str):
        word_arr = s.strip().split(" ")
        n = len(word_arr.pop())
        return n