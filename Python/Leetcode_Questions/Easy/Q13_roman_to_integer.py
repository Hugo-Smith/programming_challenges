class Solution:
    def romanToInt(self, s: str) -> int:
        result = 0
        number_map = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        for i in range(len(s)):
            
            cur_num = number_map[s[i]]
            print('i: ' + str(i) + '    Letter:' + str(number_map[s[i]]))

            if i < len(s)-1:
                nxt_num = number_map[s[i+1]]

                if cur_num < nxt_num:
                    result -= cur_num
                    print('Result 1: ' + str(result))
                    continue
            
            result += cur_num
            print('result: ' + str(result))

        return result

def main():
    num1 = "III"
    num2 = "LVIII"
    num3 = "MCMXCIV"
    solution = Solution()
    print(solution.romanToInt(num1))
    print(solution.romanToInt(num2))
    print(solution.romanToInt(num3))

if __name__ == '__main__':
    main()
           
