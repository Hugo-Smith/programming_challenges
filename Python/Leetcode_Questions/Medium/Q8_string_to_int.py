class Solution:
    def myAtoi(self, s: str) -> int:
        res = 0
        num_found = False
        neg_num = False
        stripped_str = s.strip()
        
        for c in s:
            if c.isdigit() == True == num_found == False:
                


