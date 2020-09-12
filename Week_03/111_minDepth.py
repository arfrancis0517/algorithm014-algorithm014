# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minDepth(self, root: TreeNode) -> int:


        if root is None: 
            return 0 
        
        left_height = self.minDepth(root.left) 
        right_height = self.minDepth(root.right) 

        if left_height == 0 or right_height == 0:
            return left_height + right_height + 1
        else:
            return min(left_height, right_height) + 1