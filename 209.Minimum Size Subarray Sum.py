#
# @lc app=leetcode.cn id=209 lang=python3
#
# [209] Minimum Size Subarray Sum
# 

# @lc code=start
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        j = 0
        summ = 0
        minn = float('inf')
        for i in range(len(nums)):
            summ += nums[i]
            
            while summ >= target:
                minn = min(minn, i-j+1)
                summ -= nums[j]
                j+=1
        return 0 if minn == float('inf') else minn
# @lc code=end

