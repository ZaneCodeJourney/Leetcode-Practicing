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
        if not root.children:
            return 1
        children_depth = [self.maxDepth(node) for node in root.children]
        return max(children_depth) + 1


# @lc code=end
