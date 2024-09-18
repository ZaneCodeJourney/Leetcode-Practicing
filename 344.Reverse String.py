#
# @lc app=leetcode.cn id=344 lang=python3
#
# [344] Reverse String
#


# @lc code=start
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        for i in range(0, len(s)):
            if i % 2 and i == s // 2 + 1:
                return None
            for i in range(0, len(s) // 2):
                temp = s[i]
                s[i] = s[len(s) - 1 - i]
                s[len(s) - 1 - i] = temp
            return None


# @lc code=end
