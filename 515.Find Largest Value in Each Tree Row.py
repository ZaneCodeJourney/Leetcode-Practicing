#
# @lc app=leetcode.cn id=515 lang=python3
#
# [515] Find Largest Value in Each Tree Row
#


# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque


class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        queue = deque([root])
        result = []
        while queue:
            max_val = float("-inf")
            for _ in range(len(queue)):
                cur = queue.popleft()
                max_val = max(max_val, cur.val)
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
            result.append(max_val)
        return result


# @lc code=end
