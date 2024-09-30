#
# @lc app=leetcode.cn id=257 lang=python3
#
# [257] Binary Tree Paths
#


# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def getPath(self, root, path, res):
        if not root:
            return None
        path += str(root.val)
        if root.left is None and root.right is None:
            res.append(path)
        else:
            path += "->"
            self.getPath(root.left, path, res)
            self.getPath(root.right, path, res)

    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        res = []
        self.getPath(root, "", res)
        return res


# @lc code=end
