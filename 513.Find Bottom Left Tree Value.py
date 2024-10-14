#
# @lc app=leetcode.cn id=513 lang=python3
#
# [513] Find Bottom Left Tree Value
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
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        queue = deque([root])
        while queue:
            for i in range(len(queue)):
                cur = queue.popleft()
                if i == 0:
                    res = cur.val
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
        return res


# @lc code=end
