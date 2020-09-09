class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        if nums == 0 and len(nums)<=2:
            return []

## 3. 排序 加 双指针 O(N2)
## 

        n = len(nums)
        nums.sort()  ## 排序一下
        ans = list()
        
        # 枚举 a ---target
        for first in range(n-2):
            # 需要和上一次枚举的数不相同
            if first > 0 and nums[first] == nums[first - 1]: ## 判重复
                continue
            # c 对应的指针初始指向数组的最右端
            third = n - 1
            target = -nums[first]
            # 枚举 b
            for second in range(first + 1, n-1):
                # 需要和上一次枚举的数不相同
                if second > first + 1 and nums[second] == nums[second - 1]:
                    continue
                # 需要保证 b 的指针在 c 的指针的左侧
                while second < third and nums[second] + nums[third] > target:
                    third -= 1
                # 如果指针重合，随着 b 后续的增加
                # 就不会有满足 a+b+c=0 并且 b<c 的 c 了，可以退出循环
                if second == third:
                    break
                if nums[second] + nums[third] == target:
                    ans.append([nums[first], nums[second], nums[third]])
        
        return ans