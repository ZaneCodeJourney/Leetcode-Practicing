#
# @lc app=leetcode.cn id=28 lang=python3
#
# [28] Find the Index of the First Occurrence in a String
#


# @lc code=start
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        needleLen = len(needle)
        if needleLen == 0:
            return 0
        for i in range(0, len(haystack) - needleLen + 1):
            if haystack[i : i + needleLen] == needle:
                return i
        return -1


# @lc code=end
