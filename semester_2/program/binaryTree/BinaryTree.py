class BinaryTree:
    def __init__(self, rootObj):
        self.key = rootObj
        self.leftChild = None
        self.rightChild = None

    def insertLeft(self, newNode):
        if self.leftChild is None:
            self.leftChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.leftChild = self.leftChild
            self.leftChild = t

    def insertRight(self, newNode):
        if self.rightChild is None:
            self.rightChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.rightChild = self.rightChild
            self.rightChild = t

    def getLeftChild(self):
        return self.leftChild

    def getRightChild(self):
        return self.rightChild

    def setRootVal(self, obj):
        self.key = obj

    def getRootVal(self):
        return self.key

# fungsi traversal di Python

def preorder(tree):
    if tree:
        print(tree.getRootVal(), end=' ')
        preorder(tree.getLeftChild())
        preorder(tree.getRightChild())

def inorder(tree):
    if tree:
        inorder(tree.getLeftChild())
        print(tree.getRootVal(), end=' ')
        inorder(tree.getRightChild())

def postorder(tree):
    if tree:
        postorder(tree.getLeftChild())
        postorder(tree.getRightChild())
        print(tree.getRootVal(), end=' ')

# fungsimenghitung jumlah node

def countNodes(tree):
    if tree is None:
        return 0
    else:
        return 1 + countNodes(tree.getLeftChild()) + countNodes(tree.getRightChild())

def height(tree):
    if tree is None:
        return 0
    else:
        left_height = height(tree.getLeftChild())
        right_height = height(tree.getRightChild())
        return max(left_height, right_height) + 1

# contoh penggunaan

if __name__ == "__main__":
    tree = BinaryTree(10)
    tree.insertLeft(5)
    tree.insertRight(20)
    tree.getLeftChild().insertLeft(3)
    tree.getLeftChild().insertRight(7)
    tree.getRightChild().insertLeft(15)
    tree.getRightChild().insertRight(30)

    print("Preorder traversal:")
    preorder(tree)
    print("\n\nInorder traversal:")
    inorder(tree)
    print("\n\nPostorder traversal:")
    postorder(tree)

    print("\n\nJumlah node:", countNodes(tree))
    print("Tinggi tree:", height(tree))