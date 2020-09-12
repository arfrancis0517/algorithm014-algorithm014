# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:

        if not root : 
            return 

        stack = [root]

        while stack :
            for i in range(len(stack)):
                cur = stack.pop(0)
                cur.left,cur.right = cur.right,cur.left
                if cur.left :
                    stack.append(cur.left)
                if cur.right :
                    stack.append(cur.right)
        return root