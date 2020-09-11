class Solution:
    def trap(self, height: List[int]) -> int:
        if not height or len(height) <= 2:
            return 0
        left = 1
        right = len(height) - 2
        left_max = height[0]
        right_max = height[len(height) - 1]
        res = 0
        while left <= right:
            if left_max < right_max:
                if left_max > height[left]:
                    res += left_max - height[left]
                left_max = max(left_max, height[left])
                left += 1
            else:
                if right_max > height[right]:
                    res += right_max - height[right]
                right_max = max(right_max, height[right])
                right -= 1
        return res