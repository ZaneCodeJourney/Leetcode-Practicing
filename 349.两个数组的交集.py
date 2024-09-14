#
# @lc app=leetcode.cn id=349 lang=python3
#
# [349] Intersection of Two Arrays
#

# @lc code=start
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # return list(set(nums1) & set(num2))
        a,b=dict(),dict()
        for char in nums1:
            if char not in a:
                a[char] = 1
        for char in nums2:
            if char not in b:
                b[char] = 1
        result = []
        for key in a:
            if a.get(key, 0) and b.get(key, 0):
                result.append(key)
        return result
# @lc code=end

