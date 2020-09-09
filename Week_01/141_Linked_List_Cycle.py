# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
## 快慢指针 
        if not head or not head.next:   #节点不存在或下一个节点不存在
            return False
        
        slow = head
        fast = head.next                #起点错开，防止下面循环判断有问题
        
        while fast and fast.next:       #快节点和快节点下一个节点不为空
            if slow == fast:
                return True
            slow = slow.next
            fast = fast.next.next
        return False