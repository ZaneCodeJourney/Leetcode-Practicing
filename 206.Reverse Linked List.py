#
# @lc app=leetcode.cn id=206 lang=python3
#
# [206] Reverse Linked List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        record = []
        current = head
        
        while current != None:
            record.append(current.val)
            current = current.next
            
        head = ListNode(record[len(record) - 1], None)
        prev =  head
        for i in range(len(record) - 2, -1, -1):
            node = ListNode(record[i], None)
            prev.next = node
            prev = node
        return head
        
# @lc code=end

