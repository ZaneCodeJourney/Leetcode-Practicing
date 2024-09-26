#
# @lc app=leetcode.cn id=100 lang=python3
#
# [100] Same Tree
#


# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        return self.compare(p, q)

    def compare(self, left, right):
        if left == None and right == None:
            return True
        elif left is None or right is None:
            return False
        elif left.val != right.val:
            return False

        outside = self.compare(left.left, right.left)
        inside = self.compare(left.right, right.right)
        isSame = inside and outside
        return isSame


# @lc code=end
