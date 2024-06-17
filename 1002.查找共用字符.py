#
# @lc app=leetcode.cn id=1002 lang=python3
#
# [1002] 查找共用字符
#
from typing import List
# @lc code=start
class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        sdict1 = {}
        for char in words[0]:
            if char in sdict1:
                sdict1[char] += 1
            else:
                sdict1[char] = 1

        for i in range(1, len(words)):
            sdict2 = {}  # 每次处理新单词前重置 sdict2
            for char in words[i]:
                if char in sdict2:
                    sdict2[char] += 1
                else:
                    sdict2[char] = 1
            for key in list(sdict1.keys()):  # 这里使用 list 来避免在迭代过程中修改字典
                if key in sdict2:
                    sdict1[key] = min(sdict1[key], sdict2[key])
                else:
                    del sdict1[key]  # 删除 sdict1 中那些不在 sdict2 中的键

        wordslist = []
        for key, value in sdict1.items():
            wordslist.extend([key] * value)  # 更简洁的添加重复字符的方式

        return wordslist

# @lc code=end

