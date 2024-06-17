#
# @lc app=leetcode.cn id=704 lang=python3
#
# [704] 二分查找
#
from typing import List

# @lc code=start
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1  # 修正high的初始值

        while low <= high:
            mid = low + (high - low) // 2  # 使用整数除法并正确计算中间索引
            if nums[mid] == target:
                return mid
            elif target > nums[mid]:
                low = mid + 1
            else:
                high = mid - 1

        return -1
                
# @lc code=end


