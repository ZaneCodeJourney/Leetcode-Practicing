#
# @lc app=leetcode.cn id=349 lang=python3
#
# [349] 两个数组的交集
#
from typing import List

# @lc code=start
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dict1 = {}
        dict2 = {}
        output = []
        
        # 填充字典，记录每个元素的存在性
        for num in nums1:
            dict1[num] = True
        
        for num in nums2:
            dict2[num] = True
        
        # 检查键是否同时存在于两个字典中
        for key in dict1:
            if key in dict2:
                output.append(key)
        
        return output
            
# @lc code=end

