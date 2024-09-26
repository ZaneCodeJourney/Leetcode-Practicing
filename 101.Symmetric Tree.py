#
# @lc app=leetcode.cn id=101 lang=python3
#
# [101] Symmetric Tree
#

# @lc code=start
# Definition for a binary tree node.
from collections import deque


# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        queue = deque([root.left, root.right])

        while queue:
            left = queue.popleft()
            right = queue.popleft()

            if not left and not right:
                continue

            if not left or not right or left.val != right.val:
                return False

            queue.append(left.left)
            queue.append(right.right)
            queue.append(left.right)
            queue.append(right.left)

        return True


# @lc code=end
