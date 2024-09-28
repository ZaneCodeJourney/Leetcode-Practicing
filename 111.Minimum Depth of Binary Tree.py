#
# @lc app=leetcode.cn id=111 lang=python3
#
# [111] Minimum Depth of Binary Tree
#


# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        return self.getDepth(root)

    def getDepth(self, node):
        if node is None:
            return 0

        leftDepth = self.getDepth(node.left)
        rightDepth = self.getDepth(node.right)

        if not node.left and node.right:
            return rightDepth + 1
        if not node.right and node.left:
            return leftDepth + 1

        result = min(leftDepth, rightDepth) + 1

        return result


# @lc code=end
