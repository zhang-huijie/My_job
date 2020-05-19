'''
leecode617:合并二叉树
给定两个二叉树，想象当你将它们中的一个覆盖到另一个上时，两个二叉树的一些节点便会重叠。
你需要将他们合并为一个新的二叉树。合并的规则是如果两个节点重叠，
那么将他们的值相加作为节点合并后的新值，否则不为 NULL 的节点将直接作为新二叉树的节点。
'''
class Node:
    #首先构建二叉树
    def __init__(self,value = None,left = None,right = None):
        self.value = value
        self.left = left  #左子树
        self.right = right #右子树

class Solution:
    def mergeTrees(self,t1, t2):
        if t1 and t2:
            t1.value += t2.value
            t1.left = self.mergeTrees(t1.left,t2.left)
            t1.right = self.mergeTrees(t1.right,t2.right)
            return t1
        else:
            return t1 or t2

def preTraverse(root):
    #前序遍历
    if root== None:
        return
    print(root.value)
    preTraverse(root.left)
    preTraverse(root.right)


if __name__ == '__main__':
    node1 = Node(1,Node(3,Node(5),Node(0)),Node(2))
    node2 = Node(2,Node(1,Node(0),Node(4)),Node(3,Node(0),Node(7)))
    a = Solution()
    preTraverse(a.mergeTrees(node1,node2))
