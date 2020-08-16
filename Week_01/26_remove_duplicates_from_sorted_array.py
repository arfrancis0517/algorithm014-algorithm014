class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i,j = 0,1
        while j < len(nums):
            if nums[j] == nums[i]:
                j += 1
            else:
                i += 1
                nums[i] = nums[j]
        return i+1
