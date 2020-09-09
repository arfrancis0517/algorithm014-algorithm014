class Solution:
    def maxArea(self, height: List[int]) -> int:
## 
## 左右边界 O(n) 左右夹逼
## 
        l = 0 
        r = len(height) - 1
        ans = 0
        while l < r:
            area = min(height[l], height[r]) * (r - l)
            ans = max(ans, area)
            if height[l] <= height[r]:
                l += 1
            else:
                r -= 1
        return ans