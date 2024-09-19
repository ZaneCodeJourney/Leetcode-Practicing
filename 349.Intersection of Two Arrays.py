#
# @lc app=leetcode.cn id=349 lang=python3
#
# [349] Intersection of Two Arrays
#


# @lc code=start
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        nums1dict, nums2dict = {}, {}
        for num in nums1:
            nums1dict[num] = 1
        for num in nums2:
            nums2dict[num] = 1
        for key in nums1dict:
            if nums1dict.get(key, 0) == nums2dict.get(key, 0):
                res.add(key)
        return res


# @lc code=end
