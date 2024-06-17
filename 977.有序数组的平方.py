#
# @lc app=leetcode.cn id=977 lang=python3
#
# [977] 有序数组的平方
#

# @lc code=start
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        for i in range(0, len(nums)):
            nums[i] = nums[i] ** 2
        return sorted(nums)
# @lc code=end

