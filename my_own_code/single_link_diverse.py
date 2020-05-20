#python实现单链表的反转
#coding = utf-8
class Node:
    def __init__(self,data = None,next = None):
        self.data = data
        self.next = next
def rev(link):
    #9-11是将原链表的第一个节点变成了新链表的最后一个节点，同时将原链表的第二个节点保存在cur中
    pre = link
    cur = link.next
    pre.next =None
    #从原链表的第二个节点开始遍历到最后一个节点，将所有节点翻转一遍
    while cur:
        temp = cur.next
        cur.next = pre
        pre = cur
        cur = temp
    return pre

#/////////////////////////////////////////////////
#方法二
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
#/////////////////////////////////////////////////////////

if __name__ == '__main__':
    link = Node(1, Node(2, Node(3, Node(4, Node(5, Node(6, Node(7, Node(8, Node(9)))))))))
    root = rev(link)
    while root:
        print(root.data)
        root = root.next

'''
解释一下rev函数的实现过程：

line 9-11是将原链表的第一个节点变成了新链表的最后一个节点，同时将原链表的第二个节点保存在cur中

line13-16就是从原链表的第二个节点开始遍历到最后一个节点，将所有节点翻转一遍

以翻转第二个节点为例

temp = cur.next是将cur的下一个节点保存在temp中，也就是第节点3，因为翻转后，节点2的下一个节点变成了节点1，原先节点2和节点3之间的连接断开，通过节点2就找不到节点3了，因此需要保存

cur.next = pre就是将节点2的下一个节点指向了节点1

然后pre向后移动到原先cur的位置，cur也向后移动一个节点，也就是pre = cur ,cur =temp

这就为翻转节点3做好了准备
'''