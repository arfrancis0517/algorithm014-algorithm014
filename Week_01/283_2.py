class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 循环遍历数组，当遇到非零元素则开始交换慢指针所指的0元素
        # i 为慢指针 指向最新一个0元素的位置
        i = 0
        for j in range(len(nums)):
            if nums[j] != 0:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
        return nums
        