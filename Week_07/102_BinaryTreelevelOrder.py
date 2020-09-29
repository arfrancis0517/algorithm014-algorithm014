# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
		"""
		:type root: TreeNode
		:rtype: List[List[int]]
		"""
		if not root:
			return []
		res = []
		def dfs(index,r):
			# 假设res是[ [1],[2,3] ]， index是3，就再插入一个空list放到res中
			if len(res)<index:
				res.append([])
			#  将当前节点的值加入到res中，index代表当前层，假设index是3，节点值是99
			# res是[ [1],[2,3] [4] ]，加入后res就变为 [ [1],[2,3] [4,99] ]
			res[index-1].append(r.val)
			# 递归的处理左子树，右子树，同时将层数index+1
			if r.left:
				dfs(index+1,r.left)
			if r.right:
				dfs(index+1,r.right)
		dfs(1,root)
		return res