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
        res = 0
        queue = deque([root])
        while queue:
            cur = queue.popleft()
            if cur.left:
                if not cur.left.left and not cur.left.right:
                    res += cur.left.val
                queue.append(cur.left)
            if cur.right:
                queue.append(cur.right)
        return res


# @lc code=end
