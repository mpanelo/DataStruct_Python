import random

class BinarySearchTree:


    def __init__( self ):
        self.root = None
        self.num_of_nodes = 0


    def __len__( self ):
        return self.num_of_nodes


    def __contains__( self, key ):
        node = self.search(self.root, key)
        return node is not None


    def __iter__( self ):
        return BSTIterator(self.root)


    def insert( self, key, value ):
        if key in self:
            node = self.search(self.root, key)
            node.value = value
            return False
        else:
            self.root = self.BST_insert(self.root, key, value)
            self.num_of_nodes += 1
            return True


    def BST_insert( self, subtree, key, value ):
        if subtree is None:
            subtree = BSTNode(key, value)
        elif subtree.key < key:
            subtree.rightChild = self.BST_insert(subtree.rightChild, key, value)
        elif key < subtree.key:
            subtree.leftChild = self.BST_insert(subtree.leftChild, key, value)

        return subtree


    def minValue( self, subtree ):
        if subtree is None:
            return None
        elif subtree.leftChild is not None:
            return self.minValue(subtree.leftChild)
        else:
            return subtree


    def maxValue( self, subtree ):
        if subtree is None:
            return None
        elif subtree.rightChild is not None:
            return self.maxValue(subtree.rightChild)
        else:
            return subtree


    def valueOf( self, key ):
        node = self.search(self.root, key)
        return node.value if (node is not None) else None


    def search( self, subtree, target ):
        if subtree is None:
            return None
        elif subtree.key < target:
            return self.search(subtree.rightChild, target)
        elif target < subtree.key:
            return self.search(subtree.leftChild, target)
        else:
            return subtree


class BSTNode:


    def __init__( self, key, value ):
        self.key = key
        self.value = value
        self.leftChild = None
        self.rightChild = None
        # self.parent = None


def main():
    myBST = BinarySearchTree()
    keys = [int(random.randint(0,30)) for i in range(0, 10)]

    print(keys)
    for key in keys:
        myBST.insert(key, 'mau')


if __name__ == '__main__':
    main()
