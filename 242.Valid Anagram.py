#
# @lc app=leetcode.cn id=242 lang=python3
#
# [242] Valid Anagram
#

# @lc code=start
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        a,b=dict(),dict()
        for char in s:
            if char in a:
                a[char] += 1
            else:
                a[char] = 1
        for char in t:
            if char in b:
                b[char] += 1
            else:
                b[char] = 1
        for key in a:
            if a[key] == b.get(key, 0):
                b[key] = 0
            else:
                return False
        for key in b:
            if b[key]:
                return False
        return True
# @lc code=end

