#
# @lc app=leetcode.cn id=704 lang=python3
#
# [704] 二分查找
#

# @lc code=start
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)
        while left < right:
            mid = (left + right) // 2
        
            if nums[mid] > target:
                right = mid 
            elif nums[mid] < target:
                left = mid + 1
            else:
                return mid
        return -1
# @lc code=end

