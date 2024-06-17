#
# @lc app=leetcode.cn id=209 lang=python3
#
# [209] 长度最小的子数组
#
from typing import List

# @lc code=start
class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        if nums is None or len(nums) == 0:
            return 0
        lenf = len(nums) + 1
        total = 0
        i = j = 0
        while(j < len(nums)):
            total += nums[j]
            j += 1
            while(total >= s):
                lenf = min(j-i, lenf)
                total -= nums[i]
                i += 1
        if lenf == len(nums) + 1:
            return 0
        else:
            return lenf
# @lc code=end


