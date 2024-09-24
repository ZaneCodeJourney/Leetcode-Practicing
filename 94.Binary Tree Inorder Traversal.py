#
# @lc app=leetcode.cn id=94 lang=python3
#
# [94] Binary Tree Inorder Traversal
#


# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        def dps(node):
            if node is None:
                return
            dps(node.left)
            res.append(node.val)
            dps(node.right)

        dps(root)
        return res


# @lc code=end
