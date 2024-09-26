#
# @lc app=leetcode.cn id=101 lang=python3
#
# [101] Symmetric Tree
#

# @lc code=start
# Definition for a binary tree node.
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self.compare(root.left, root.right)

    def compare(self, left, right):
        if left == None and right != None:
            return False
        elif left != None and right == None:
            return False
        elif left == None and right == None:
            return True
        elif left.val != right.val:
            return False

        outside = self.compare(left.left, right.right)
        inside = self.compare(left.right, right.left)
        isSame = inside and outside
        return isSame


# @lc code=end
