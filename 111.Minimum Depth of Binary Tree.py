#
# @lc app=leetcode.cn id=111 lang=python3
#
# [111] Minimum Depth of Binary Tree
#


# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        queue = deque([root])
        level = 0
        while queue:
            level += 1
            for _ in range(len(queue)):
                cur = queue.popleft()

                if not cur.left and not cur.right:
                    return level

                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)

        return level


# @lc code=end
