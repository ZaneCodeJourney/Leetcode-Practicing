#
# @lc app=leetcode.cn id=242 lang=python3
#
# [242] 有效的字母异位词
#

# @lc code=start
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        sdict = {}
        for char in s:
            if char in sdict:
                sdict[char] += 1
            else:
                sdict[char] = 1
        for char in t:
            if char in sdict:
                sdict[char] -= 1
            else:
                # 如果t中的字符在s中没有出现过，直接返回False
                return False
        for value in sdict.values():
            if value != 0:
                return False
        return True
            
        


# @lc code=end

