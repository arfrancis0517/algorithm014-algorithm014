class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:

        all_combination=[]

        def backtracking(remain_selection,unfinished_count,prefix):
            if unfinished_count==0:
                all_combination.append(prefix[:])
            tmp_length=len(remain_selection)
            for i in range(tmp_length):
                #此处代码优化可以显著提高运行的效率
                if unfinished_count<=tmp_length-i+1:
                    backtracking(remain_selection[i+1:],unfinished_count-1,prefix+[remain_selection[i]])
                else:
                    break
        
        if n<k or n<=0 or k<=0:
            return []
        backtracking([i for i in range(1,n+1)],k,[])
        return all_combination