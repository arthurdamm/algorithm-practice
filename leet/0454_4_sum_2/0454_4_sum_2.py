# LeetCode 454. 4Sum II
# https://leetcode.com/problems/4sum-ii/
# O(n^2) time-and-space
class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        n = len(nums1)
        combos = defaultdict(int)
        solutions = 0
        for i in range(n):
            for j in range(n):
                combos[nums1[i] + nums2[j]] += 1
        for i in range(n):
            for j in range(n):
                target = 0 - (nums3[i] + nums4[j])
                solutions += combos[target]
        return solutions
