#
# @lc app=leetcode.cn id=20 lang=python3
#
# [20] Valid Parentheses
#


# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for brac in s:
            if brac == "(" or brac == "{" or brac == "[":
                stack.append(brac)
            else:
                if not stack:
                    return False
                if brac == ")":
                    if stack.pop() != "(":
                        return False
                if brac == "]":
                    if stack.pop() != "[":
                        return False
                if brac == "}":
                    if stack.pop() != "{":
                        return False
        return not stack


# @lc code=end
