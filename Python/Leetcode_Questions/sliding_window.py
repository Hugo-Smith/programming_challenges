

class Solution:
    def slidingWindow(self, size, arr):

        if size > len(arr):
            return None
        
        maxSum = 0
        currSum = 0

        #initialise the first window

        for i in range(size):
            currSum += arr[i]
        maxSum = currSum

        for i in range(size, len(arr)):
            currSum += (arr[i] - arr[i-size])
            maxSum = max(currSum, maxSum)

        
        return maxSum
    

def main():
    s = Solution()
    k = 3
    arr = [2,1,5,1,3,2]
    print(s.slidingWindow(k, arr))
    

if __name__ == '__main__':
    main()