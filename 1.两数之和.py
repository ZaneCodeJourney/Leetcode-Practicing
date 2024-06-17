#
# @lc app=leetcode.cn id=1 lang=python3
#
# [1] 两数之和
#
from typing import List

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_index = {}  # 使用具体的变量名替代 dict
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in num_index:
                return [num_index[complement], i]
            num_index[nums[i]] = i
# @lc code=end

