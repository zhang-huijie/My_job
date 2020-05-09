def reverseList1(self, head):
    """
    leetcode官方解法，思路和上一个解法大同小异，重点是在第1个节点前构造一个虚拟节点
    """
    if head is None or head.next is None:  # 兼容leetcode特殊用例，链表为空或只有1个节点
        return head
    pre_node = None
    current_node = head
    while current_node is not None:
        next_node = current_node.next
        current_node.next = pre_node
        pre_node = current_node
        current_node = next_node
    return pre_node