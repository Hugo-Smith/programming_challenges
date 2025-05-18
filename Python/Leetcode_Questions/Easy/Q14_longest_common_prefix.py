class Solution:
    def longestCommonPrefix(self, strs) -> str:
        if not strs:
            return ''

        prefix = ''

        sortedList = sorted(strs)
        iniStr = sortedList[0]
        finStr = sortedList[-1]

        for i in range(len(iniStr)):
            if iniStr[i] == finStr[i]:
                prefix += iniStr[i]
            else:
                break
        return prefix







def main():
    strs1 = ["flower","flow","flight"]
    strs2 = ["dog","racecar","car"]
    solution = Solution()
    print(solution.longestCommonPrefix(strs1))
    print(solution.longestCommonPrefix(strs2))


if __name__ == '__main__':
    main()