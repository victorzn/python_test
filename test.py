# -*- coding:utf-8 -*- 
class BinaryTreeNode(object):
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

class BinaryTree(object):
    def __init__(self, root=None):
        self.root = root

    def is_empty(self):
        return self.root == None

    def preOrder(self,BinaryTreeNode):
        if BinaryTreeNode == None:
            return
        # 先打印根结点，再打印左结点，后打印右结点
        print(BinaryTreeNode.data)
        self.preOrder(BinaryTreeNode.left)
        self.preOrder(BinaryTreeNode.right)

    def mid(self,BinaryTreeNode):
        if BinaryTreeNode == None:
            return 
        while BinaryTreeNode != None:
            if BinaryTreeNode.left == None:
                print(BinaryTreeNode.data)
                BinaryTreeNode = BinaryTreeNode.right
            else:
                pre = BinaryTreeNode.left
                while pre.right!=None and pre.right!=BinaryTreeNode:
                    pre = pre.right
                if pre.right == None:
                    pre.right = BinaryTreeNode
                    BinaryTreeNode = BinaryTreeNode.left
                else:
                    pre.right = None
                    print(BinaryTreeNode.data)
                    BinaryTreeNode = BinaryTreeNode.right


    def inOrder(self,BinaryTreeNode):
        if BinaryTreeNode == None:
            return
        # 先打印左结点，再打印根结点，后打印右结点
        self.inOrder(BinaryTreeNode.left)
        print(BinaryTreeNode.data)
        self.inOrder(BinaryTreeNode.right)

    def postOrder(self,BinaryTreeNode):
        if BinaryTreeNode == None:
            return
        # 先打印左结点，再打印右结点，后打印根结点
        self.postOrder(BinaryTreeNode.left)
        self.postOrder(BinaryTreeNode.right)
        print(BinaryTreeNode.data)

n1 = BinaryTreeNode(data="D")
n2 = BinaryTreeNode(data="E")
n3 = BinaryTreeNode(data="F")
n4 = BinaryTreeNode(data="B", left=n1, right=n2)
n5 = BinaryTreeNode(data="C", left=n3, right=None)
root = BinaryTreeNode(data="A", left=n4, right=n5)

bt = BinaryTree(root)
print('先序遍历')
bt.preOrder(bt.root)
print('中序遍历')
bt.inOrder(bt.root)
print('后序遍历')
bt.postOrder(bt.root)
print('ffff')
bt.mid(bt.root)
