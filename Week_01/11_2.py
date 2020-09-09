class Solution:
    def maxArea(self, height: List[int]) -> int:
##嵌套循环的遍历
## O(n2)
## 时间复杂度很高
        ans=0
        i=0
        j=i+1
        for i in range(len(height)-1):
            for j in range(len(height)):
                area= min(height[i], height[j]) * (j - i)
                ans = max(ans, area) 
            j += 1
        i += 1
        return ans