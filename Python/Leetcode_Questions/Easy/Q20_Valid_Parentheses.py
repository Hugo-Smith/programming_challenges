class Solution:
    def isValid(self, s: str) -> bool:

        if len(s) % 2 != 0: #any odd numbered string will be false
            return False
        
        stack = []
        charDict = {')': '(', '}': '{', ']': '['}

        for char in s:

            if char in charDict.values(): #if character is opening append to stack
                stack.append(char)

            elif char in charDict:
                if not stack or stack.pop() != charDict[char]:
                    return False
            else:
                return False
        
        return not stack
        
