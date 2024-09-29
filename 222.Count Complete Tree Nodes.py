#
# @lc app=leetcode.cn id=222 lang=python3
#
# [222] Count Complete Tree Nodes
#

# @lc code=start
# Definition for a binary tree node.
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:  # 利用完全二叉树特性
    def countNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        count = 0
        left = root.left
        right = root.right
        while left and right:
            count += 1
            left = left.left
            right = right.right
        if not left and not right:  # 如果同时到底说明是满二叉树，反之则不是
            return (2 << count) - 1
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)


# @lc code=end
