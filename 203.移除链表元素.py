#
# @lc app=leetcode.cn id=203 lang=python3
#
# [203] 移除链表元素
#

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        # 处理头节点的特殊情况
        while head and head.val == val:
            head = head.next

        # 初始化当前节点和前一个节点
        node = head
        nodeBefore = None

        # 遍历链表
        while node:
            if node.val == val:
                # 删除当前节点
                nodeBefore.next = node.next
            else:
                # 更新前一个节点
                nodeBefore = node
            # 移动到下一个节点
            node = node.next

        return head

# @lc code=end

