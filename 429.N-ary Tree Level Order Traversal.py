#
# @lc app=leetcode.cn id=429 lang=python3
#
# [429] N-ary Tree Level Order Traversal
#

# @lc code=start


# Definition for a Node.
class Node:
    def __init__(
        self, val: Optional[int] = None, children: Optional[List["Node"]] = None
    ):
        self.val = val
        self.children = children


class Solution:
    def levelOrder(self, root: "Node") -> List[List[int]]:
        if not root:
            return []
        queue = deque([root])
        result = []
        while queue:
            level = []
            for _ in range(len(queue)):
                cur = queue.popleft()
                level.append(cur.val)
                if cur.children:
                    for child in cur.children:
                        queue.append(child)
            result.append(level)
        return result


# @lc code=end
