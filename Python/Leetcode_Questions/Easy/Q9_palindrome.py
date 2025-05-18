class Solution:
    def isPalindrome(self, x: int) -> bool:
        num_lst = [i for i in str(x)]
        rev_lst = num_lst.copy()
        rev_lst.reverse()

        if num_lst == rev_lst:
            return True
        else: False


def main():
    num1 = 121
    num2 = 1234
    num3 = 323
    solution = Solution()
    print(solution.isPalindrome(num1))
    print(solution.isPalindrome(num2))
    print(solution.isPalindrome(num3))

if __name__ == '__main__':
    main()