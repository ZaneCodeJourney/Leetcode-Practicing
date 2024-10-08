#
# @lc app=leetcode.cn id=454 lang=python3
#
# [454] 4Sum II
#

# @lc code=start
class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        count = 0
        result = dict()
        for num1 in nums1:
            for num2 in nums2:
                if num1 + num2 not in result:
                    result[num1 + num2] = 1
                else:
                    result[num1 + num2] += 1
        for num3 in nums3:
            for num4 in nums4:
                if -(num3 + num4) in result:
                    count += result[-(num3 + num4)]
        return count
# @lc code=end

