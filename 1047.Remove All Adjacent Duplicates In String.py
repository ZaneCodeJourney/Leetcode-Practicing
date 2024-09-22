#
# @lc app=leetcode.cn id=1047 lang=python3
#
# [1047] Remove All Adjacent Duplicates In String
#


# @lc code=start
class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []
        for char in s:
            if not stack:
                stack.append(char)
            else:
                if char == stack[-1]:
                    stack.pop()
                else:
                    stack.append(char)
        return "".join(stack)


# @lc code=end
