# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if not headA or not headB:
            return None

        l1, l2 = 0, 0
        node1, node2 = headA, headB
        while node1:
            l1, node1 = l1 + 1, node1.next
        while node2:
            l2, node2 = l2 + 1, node2.next

        insLenght = min(l1, l2)
        node1, node2 = headA, headB
        for _ in range(l1 - insLenght):
            node1 = node1.next
        for _ in range(l2 - insLenght):
            node2 = node2.next

        while node1 and node2:
            if node1 == node2:
                return node1
            node1, node2 = node1.next, node2.next

        return None

