class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
##hash 对于每一个a （target-a)有没有在nums里
##o(N)

        hashmap={}
        for ind,num in enumerate(nums):
            hashmap[num] = ind
        for i,num in enumerate(nums):
            j = hashmap.get(target - num)
            if j is not None and i!=j:
                return [i,j]

##
        hashmap={}
        for i,num in enumerate(nums):
            if hashmap.get(target - num) is not None:
                return [i,hashmap.get(target - num)]
            hashmap[num] = i #这句不能放在if语句之前，解决list中有重复值或target-num=num的情况

