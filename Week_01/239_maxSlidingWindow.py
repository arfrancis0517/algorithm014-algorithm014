class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        双排队列
        """
        queue, res = [], []
        for i in range(len(nums)):
            if len(queue) > 0 and i - queue[0] + 1 > k: del queue[0]
            while len(queue) > 0 and nums[i] > nums[queue[-1]]: del queue[-1]
            queue.append(i)
            if i >= k - 1: 
                res.append(nums[queue[0]])
                
        return res