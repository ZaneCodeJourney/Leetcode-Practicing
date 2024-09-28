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
        ans = 0

        def dfs(node: Optional[Node], depth: int):
            if node is None:
                return
            depth += 1
            nonlocal ans
            ans = max(ans, depth)
            for child in node.children:
                dfs(child, depth)

        dfs(root, 0)
        return ans


# @lc code=end
