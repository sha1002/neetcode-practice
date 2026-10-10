class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        left_maximum = height[left]
        right_maximum = height[right]
        water = 0

        while left < right:
            if left_maximum < right_maximum:
                left += 1
                left_maximum = max(left_maximum, height[left])
                water += left_maximum - height[left]
            else:
                right -= 1
                right_maximum = max(right_maximum, height[right])
                water += right_maximum - height[right]
        
        return water