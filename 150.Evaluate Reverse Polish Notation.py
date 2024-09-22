#
# @lc app=leetcode.cn id=150 lang=python3
#
# [150] Evaluate Reverse Polish Notation
#

from typing import List


# @lc code=start
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token.lstrip("-").isdigit():
                stack.append(int(token))
            else:
                left = stack.pop()
                right = stack.pop()
                if token == "+":
                    stack.append(left + right)
                if token == "-":
                    stack.append(right - left)
                if token == "*":
                    stack.append(left * right)
                if token == "/":
                    stack.append(int(right / left))
        return stack.pop()


# @lc code=end
