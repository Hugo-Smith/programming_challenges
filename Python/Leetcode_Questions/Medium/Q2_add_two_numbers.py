"""
You are given two non-empty linked lists representing two non-negative integers. 
The digits are stored in reverse order, and each of their nodes contains a single digit. 
Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.
"""
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val #The stored value
        self.next = next #pointer to the next node


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        temp_head = ListNode(0)
        current = temp_head
        carry = 0

        while l1 or l2 or carry:
            value1 = l1.val if l1 else 0
            value2 = l2.val if l1 else 0

            total = value1 + value2 + carry
            carry = total // 10
            current.next = ListNode(total % 10)
            current = current.next

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        return temp_head.next



def main():
    l1 = [2,4,3]
    l2 = [5,6,4]

    sol = Solution()

    sum_list = sol.addTwoNumbers(l1,l2)
    print(sum_list)

if __name__ == "__main__":
    main()