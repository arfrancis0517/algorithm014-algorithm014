class Solution:
    def fib(self, N: int) -> int:

        if N <= 1:
            return N
            
        f = 0
        fMinusOne = 1
        fMinusTwo = 0

        while N >= 2:

## 采取从下往上的方法，把计算过的中间项保存起来，避免重复计算导致递归调用栈溢出
            f = fMinusOne + fMinusTwo
            fMinusTwo = fMinusOne
            fMinusOne = f
            N -= 1

        return f