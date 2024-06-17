#
# @lc app=leetcode.cn id=142 lang=python3
#
# [142] 环形链表 II
#
from typing import Optional
# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        p = head
        result = None
        while p:
            if type(p.val) is float:
                result = p
                break
            else:
                p.val = float(p.val)
                p = p.next
        
        while head:
            if type(head.val) is float:
                head.val = int(head.val)
                head = head.next
            else:
                break
        
        return result
# @lc code=end

