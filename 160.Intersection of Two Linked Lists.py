#
# @lc app=leetcode.cn id=160 lang=python3
#
# [160] Intersection of Two Linked Lists
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        lenA, lenB = 0, 0
        curA, curB = headA, headB
        
        while curA:
            lenA += 1
            curA = curA.next
            
        while curB:
            lenB += 1
            curB = curB.next
        
        curA, curB = headA, headB

        if lenA > lenB:
            for _ in range(lenA - lenB):
                curA = curA.next
        else:
            for _ in range(lenB - lenA):
                curB = curB.next

        while curA and curB:
            if curA == curB:
                return curA
            curA = curA.next
            curB = curB.next
        
        return None
            
        
        
# @lc code=end

