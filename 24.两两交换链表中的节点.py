#
# @lc app=leetcode.cn id=24 lang=python3
#
# [24] 两两交换链表中的节点
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
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 什么时候创建头结点？
        if head is None or head.next is None:
                return head
        node1 = head
        node2 = head.next
        node3 = node2.next

        node1.next = self.swapPairs(node3)
        node2.next = node1
        return node2


# @lc code=end

