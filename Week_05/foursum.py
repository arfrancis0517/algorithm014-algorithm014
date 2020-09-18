class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        if nums == 0 and len(nums)<=3:
            return []

        n = len(nums)
        nums.sort()  
        ans = list()
        
        for d in range(n-3):
            if d > 0 and nums[d] == nums[d - 1]: 
                continue
            for first in range(d+1, n-2):
                if first > d+1 and nums[first] == nums[first - 1]: 
                    continue
                third = n - 1
                tar = target - nums[first] - nums[d]
                for second in range(first + 1, n-1):
                    if second > first + 1 and nums[second] == nums[second - 1]:
                        continue
                    while second < third and nums[second] + nums[third] > tar:
                        third -= 1
                    if second == third:
                        break
                    if nums[second] + nums[third] == tar:
                        ans.append([nums[d], nums[first], nums[second], nums[third]])
         
        return ans