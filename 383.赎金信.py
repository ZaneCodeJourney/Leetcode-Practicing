#
# @lc app=leetcode.cn id=383 lang=python3
#
# [383] 赎金信
#

# @lc code=start
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        dict_magazine = {}
        for char in magazine:
            if char not in dict_magazine:
                dict_magazine[char] = 1
            else:
                dict_magazine[char] += 1
        for char in ransomNote:
            if char in dict_magazine.keys() and dict_magazine[char] > 0:
                dict_magazine[char] -= 1
            else:
                return False
        return True

# @lc code=end

