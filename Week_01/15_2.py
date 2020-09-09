class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

## 暴力求解法 三个嵌套循环 O(N3)  如何去重复？
        if nums == 0 and len(nums)<=2:
            return []
        n = len(nums)
        nums.sort()        
        ans = list()
        i = 0
        j = i+1
        k = j+1
        
        for i in range(n):
            for j in range(n):
                for k in range(n):
                    if nums[i] + nums[j] + nums[k] == 0:
                        ans.append([nums[i], nums[j], nums[k]])
                    k += 1
                j += 1
            i += 1
        return ans        

## 两重暴力 加 hashset
## a + b = -c
## 把 所有 c 放到 hash 表里去， 只要两个循环就可以 -（a+b）是否在表里