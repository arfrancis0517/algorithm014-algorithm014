class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n1,n2=len(nums1),len(nums2)
        if n1>n2:
            return self.findMedianSortedArrays(nums2,nums1)
        k=(n1+n2+1)//2 #k表示切割后左半部分的个数，m+n为奇数时，中位数切割给了左半部分
        l,r=0,n1       #[l,r]表示在nums1中切割的范围
        while l<=r:
            i=(l+r)//2  #i表示nums1的切割位置
            j=k-i       #j表示nums2的切割位置
            if j>0 and i<n1 and nums2[j-1]>nums1[i]:
                l=i+1
            elif i>0 and j<n2 and nums1[i-1]>nums2[j]:
                r=i-1
            else:    #执行到此的条件为： nums1[i-1]<=nums2[j] and nums2[j-1]<=nums1[i] 或者一方超出边界
                maxLeft=max(float('-inf') if i==0 else nums1[i-1],float('-inf') if j==0 else nums2[j-1])
                if (n1+n2)%2==1:     #因为中位数划分给了左半部分，所以奇数的时候，返回左半部分最末端元素即可
                    return maxLeft
                minRight=min(float('inf') if i==n1 else nums1[i],float('inf') if j==n2 else nums2[j])  #偶数的时候需要求2个值
                return (maxLeft+minRight)/2
        return -1 #永远不会执行