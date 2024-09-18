#
# @lc app=leetcode.cn id=18 lang=python3
#
# [18] 4Sum
#


# @lc code=start
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0)
        ans = set()
        for i in range(0, len(nums)):
            for j in range(i + 1, len(nums)):
                for k in range(j + 1, len(nums)):
                    val = target - nums[i] - nums[k] - nums[j]
                    if val in freq:
                        count = (nums[i] == val) + (nums[k] == val) + (nums[j] == val)
                        if count <= freq[val]:
                            ans.add(tuple(sorted([nums[i], nums[j], nums[k], val])))
        return [list(x) for x in ans]


# @lc code=end
