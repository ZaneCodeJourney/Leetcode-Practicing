#
# @lc app=leetcode.cn id=24 lang=python3
#
# [24] Swap Nodes in Pairs
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        cur = head
        while cur and cur.next:
            first = cur
            second = cur.next
            
            first.next = second.next
            second.next = first
            prev.next = second
            
            prev = first
            cur = first.next
            
        return dummy.next        
# @lc code=end

