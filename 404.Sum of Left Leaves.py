#
# @lc app=leetcode.cn id=404 lang=python3
#
# [404] Sum of Left Leaves
#

# @lc code=start
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        leftValue = self.sumOfLeftLeaves(root.left)
        if root.left is not None and root.left.left is None and root.left.right is None:
            leftValue = root.left.val
        rightValue = self.sumOfLeftLeaves(root.right)
        res = leftValue + rightValue
        return res


# @lc code=end
