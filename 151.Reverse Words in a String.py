#
# @lc app=leetcode.cn id=151 lang=python3
#
# [151] Reverse Words in a String
#


# @lc code=start
class Solution:
    def reverseWords(self, s: str) -> str:
        # 反转整个字符串
        s = s[::-1]
        # 将字符串拆分为单词，并反转每个单词
        s = " ".join(word[::-1] for word in s.split())
        return s


# @lc code=end
