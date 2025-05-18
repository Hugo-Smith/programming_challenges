from typing import List

class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        result = []

        l, r = 0, len(products) - 1
        curr_search = ''
        for i in range(len(searchWord)):
            curr_search += searchWord[i]

            while l <= r and not products[l].startswith(curr_search):
                l += 1
            while l <= r and not products[r].startswith(curr_search):
                r -= 1

            result.append(products[l:min(l + 3, r + 1)])

        return result

def main():
    s = Solution()
    products = ['mobile', 'mouse', 'moneypot', 'monitor', 'mousepad']
    sw = 'mouse'
    print(s.suggestedProducts(products, sw))

if __name__ == '__main__':
    main()
