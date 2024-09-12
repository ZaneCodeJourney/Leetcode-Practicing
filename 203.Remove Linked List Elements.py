#
# @lc app=leetcode.cn id=203 lang=python3
#
# [203] Remove Linked List Elements
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummyNode = ListNode(0, next=head)
        node = dummyNode
        while node.next is not None:
            if node.next.val == val:
                node.next = node.next.next
            else:
                node = node.next
        return dummyNode.next
                
# @lc code=end

