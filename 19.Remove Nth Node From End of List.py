#
# @lc app=leetcode.cn id=19 lang=python3
#
# [19] Remove Nth Node From End of List
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        size = 0
        cur = head
        while cur:
            cur = cur.next
            size += 1
        num = size - n
        prev = dummy
        cur = head
        for _ in range(num): #num = 1
            prev = cur
            cur = cur.next
        prev.next = cur.next
        return dummy.next
           
            
# @lc code=end

