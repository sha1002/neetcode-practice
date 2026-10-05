from collections import Counter

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freq = Counter(nums)
        limit = len(nums) / 2

        for num, count in freq.items():
            if count > limit:
                return num