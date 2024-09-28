#
# @lc app=leetcode.cn id=559 lang=python3
#
# [559] Maximum Depth of N-ary Tree
#

# @lc code=start
from collections import deque


# Definition for a Node.
class Node:
    def __init__(
        self, val: Optional[int] = None, children: Optional[List["Node"]] = None
    ):
        self.val = val
        self.children = children


class Solution:
    def maxDepth(self, root: "Node") -> int:
        if not root:
            return 0
        max_depth = 1
        for child in root.children:
            max_depth = max(max_depth, self.maxDepth(child) + 1)
        return max_depth


# @lc code=end
