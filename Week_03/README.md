学习笔记

# 递归代码模版
# Python

    def recursion(level, param1, param2, ...): 
    # recursion terminator 
        if level > MAX_LEVEL: 
          process_result 
	        return 
    # process logic in current level 
        process(level, data...) 
    # drill down 
        self.recursion(level + 1, p1, ...) 
    # reverse the current level status if needed


# 分治 Divide 回溯 Conquer 可以认为是特殊的递归 找重复性

# 分治代码模板
# Python

    def divide_conquer(problem, param1, param2, ...): 
    # recursion terminator  
        if problem is None: 
	        print_result 
	      return 

    # prepare data 
    data = prepare_data(problem) 
    subproblems = split_problem(problem, data) 

    # conquer subproblems 
    subresult1 = self.divide_conquer(subproblems[0], p1, ...) 
    subresult2 = self.divide_conquer(subproblems[1], p1, ...) 
    subresult3 = self.divide_conquer(subproblems[2], p1, ...) 
    …

    # process and generate the final result 
    result = process_result(subresult1, subresult2, subresult3, …)
	
    # revert the current level states


# 牛顿迭代法实现 y =（x-2）**3的解

    def f(x):
        return (x-2)**3
    def fd(x):
        return 3*((x-2)**2)
    def newtonMethod(n,assum):
        time = n
        x = assum
        next = 0
        a = f(x)
        b = fd(x)
        print('a = '+str(a)+',b = '+str(b)+',time = '+str(time))
        if f(x) == 0.0:
            return time,x
        else:
            next = x-a/b
            print('next x = '+str(next))
        if a - f(next)<1e-6:
            print('meet f(x) = 0 , x = '+ str(next))  
        ##设置跳出条件，同时输出满足f(x) = 0 的x的值
        else:
            return newtonMethod(n+1,next)