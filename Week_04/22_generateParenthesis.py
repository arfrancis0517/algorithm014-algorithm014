class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def dfs(lr, rr, cur):
            if len(cur) == 2*n:
                res.append(cur)
                return
            if n >= lr > 0: dfs(lr-1, rr, cur+"(")
            if rr > lr: dfs(lr, rr-1, cur+")")
        dfs(n, n, "")
        return res