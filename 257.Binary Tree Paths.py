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

    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        stack, path_st, result = [root], [str(root.val)], []

        while stack:
            cur = stack.pop()
            path = path_st.pop()

            if not (cur.left or cur.right):
                result.append(path)
            if cur.right:
                stack.append(cur.right)
                path_st.append(path + "->" + str(cur.right.val))
            if cur.left:
                stack.append(cur.left)
                path_st.append(path + "->" + str(cur.left.val))

        return result


# @lc code=end
