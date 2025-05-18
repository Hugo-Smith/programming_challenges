from typing import List

class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        dig_lst = []
        let_lst = []

        for i in logs:
            if i[-1].isdigit():
                dig_lst.append(i)
            else:
                let_lst.append(i)
        
        let_lst_sorted = sorted(let_lst, key= lambda x: (x.split(" ", 1)[1], x.split()[0]))

        res = let_lst_sorted + dig_lst

        return res