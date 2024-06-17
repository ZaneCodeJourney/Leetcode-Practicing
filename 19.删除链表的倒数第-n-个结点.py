#
# @lc app=leetcode.cn id=19 lang=python3
#
# [19] 删除链表的倒数第 N 个结点
#

from typing import List
from typing import Optional

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        count = 0
        cur = head
        while cur:
            count += 1
            cur = cur.next
        pre, cur = head, head.next
        if count <= 1:
            return None
        if n == count:
            return head.next
        for i in range(0, count - n - 1):
            pre = cur
            cur = cur.next
        pre.next = cur.next
        return head

# @lc code=end

