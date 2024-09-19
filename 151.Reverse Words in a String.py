#
# @lc app=leetcode.cn id=151 lang=python3
#
# [151] Reverse Words in a String
#


# @lc code=start
class Solution:
    def reverseWords(self, s: str) -> str:
        strs = s.split()
        left, right = 0, len(strs) - 1
        while left < right:
            strs[left], strs[right] = strs[right], strs[left]
            left += 1
            right -= 1
        return " ".join(strs)


# @lc code=end
