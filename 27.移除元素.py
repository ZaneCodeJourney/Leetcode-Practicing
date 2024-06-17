#
# @lc app=leetcode.cn id=27 lang=python3
#
# [27] 移除元素
#
from typing import List

# @lc code=start
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        fast = 0
        slow = 0
        size = len(nums)
        while fast < size:
            if nums[fast] != val:
                nums[slow] = nums[fast]
                slow += 1
            fast += 1
        return slow
# @lc code=end

