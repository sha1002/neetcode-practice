class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1

        max_capacity = 0

        while left < right:
            area = min(heights[left], heights[right]) * (right - left)

            max_capacity = max(max_capacity, area)

            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1

        return max_capacity