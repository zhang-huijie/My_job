class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if fast == slow:
                return True
        return False

if __name__ == '__main__':
    b = ListNode(1)
    a = ListNode(1)
    a.next = ListNode(2)
    a.next.next = a
    m = Solution()
    print(m.hasCycle(a))
    print(m.hasCycle(b))