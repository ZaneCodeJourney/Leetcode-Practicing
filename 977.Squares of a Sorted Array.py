#
# @lc app=leetcode.cn id=977 lang=python3
#
# [977] Squares of a Sorted Array
#

# @lc code=start
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        nums1 = [0] * len(nums)
        j = 0 
        k = len(nums) - 1
        for i in range(len(nums) - 1, -1, -1):
            if abs(nums[k]) > abs(nums[j]):
                nums1[i] = nums[k] ** 2
                k -= 1
            else:
                nums1[i] = nums[j] ** 2
                j += 1
        return nums1
# @lc code=end
