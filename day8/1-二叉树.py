# 2026年,01月,27日,12时
class Node(object):
    """
    节点类
    """
    def __init__(self,elem = -1,lchild = None,rchild = None):
        self.elem = elem
        self.lchild = lchild
        self.rchild = rchild

class Tree(object):
    def __init__(self):
        self.root = Node()
        self.myQueue = []

    def add(self,elem):
        """增加新节点"""
        node = Node(elem)
        if self.root.elem == -1:
            self.root = node
            self.myQueue.append(self.root)
        else:
            treeNode = self.myQueue[0]
            if treeNode.lchild == None:
                treeNode.lchild = node
                self.myQueue.append(treeNode.lchild)
            else:
                treeNode.rchild = node
                self.myQueue.append(treeNode.rchild)
                self.myQueue.pop(0)

    def front_digui(self,root):
        if root == None:
            return
        print(root.elem,end=" ")
        self.front_digui(root.lchild)
        self.front_digui(root.rchild)


    def mid_digui(self,root):
        if root == None:
            return
        self.mid_digui(root.lchild)
        print(root.elem,end=" ")
        self.mid_digui(root.rchild)

    def level_digui(self,root):
        if root == None:
            return
        myQueue = []
        node = root
        myQueue.append(node)
        while myQueue:
            node = myQueue.pop(0)
            print(node.elem,end=" ")
            if node.lchild != None:
                myQueue.append(node.lchild)
            if node.rchild != None:
                myQueue.append(node.rchild)

if __name__ == '__main__':
    elems = range(10)
    tree = Tree()
    for elem in elems:
        tree.add(elem)

    print("先序遍历")
    tree.front_digui(tree.root)
    print()
    print("中序遍历")
    tree.mid_digui(tree.root)
    print()
    print('层次遍历')
    tree.level_digui(tree.root)