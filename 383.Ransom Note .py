#
# @lc app=leetcode.cn id=383 lang=python3
#
# [383] Ransom Note
#


# @lc code=start
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        count = dict()
        for char in magazine:
            if char not in count:
                count[char] = 1
            else:
                count[char] += 1
        for char in ransomNote:
            if char not in count or count[char] == 0:
                return False
            else:
                count[char] -= 1
        return True


# @lc code=end
