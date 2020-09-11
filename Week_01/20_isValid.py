class Solution:
    def isValid(self, s: str) -> bool:
## 暴力求解 不断replace匹配括号    匹配就置换成空   最后是空了 说明所有都匹配 就返回true  O(N2)

## 用栈来解决

        dic = {'{': '}',  '[': ']', '(': ')', '?': '?'}
        stack = ['?']
        for c in s:
            if c in dic: 
                stack.append(c)
            elif dic[stack.pop()] != c: 
                return False 
        return len(stack) == 1