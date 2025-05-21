import math

class Solution:
    def intToRoman(self, num: int) -> str:
        roman_dict = {
            1: 'I',
            5: 'V',
            10: 'X',
            50: 'L',
            100: 'C',
            500: 'D',
            1000: 'M'
        }
        num_str = str(num)
        len_num = len(num_str)
        res = ''
        while len_num > 0:
            if len_num == 4:
                res += num[0] * roman_dict[1000]
                num_str = num_str[1:]
            else:
                print()
                


def main():
    print(len(str(1000)))

if __name__ == '__main__':
    main()