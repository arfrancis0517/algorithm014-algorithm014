class Solution:
    def climbStairs(self, n: int) -> int:
# 找重复子问题
# 上三级台阶等于上一级台阶和二级台阶可能性之和
# f(n)=f(n-1)+f(n-2) fib数列

        if n <= 2:
            return n

        # 初始可能性次数
        p = 0 
        q = 0 
        r = 1
        
        for i in range(n):
            p = q # minu2
            q = r # minu1 
            r = p + q 
            i += 1
        return r