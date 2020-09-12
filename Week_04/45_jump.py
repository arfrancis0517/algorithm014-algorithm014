class Solution:
    def jump(self, nums: List[int]) -> int:
        n, step, end, maxPosition = len(nums), 0, 0, 0
        for i in range(n-1):
            maxPosition = max(maxPosition, nums[i] + i)
            if i == end:
                end = maxPosition
                step += 1
        return step