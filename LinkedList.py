# Singly Linked List Implementation

class LinkedList:


    def __init__( self ):
        self.head = None
        self.tail = None
        self.size = 0
    

    def __len__( self ):
        return self.size

    
    def __iter__( self ):
        return LinkedListIterator(self.head)


    def __contains__( self , item ):
        index = self.search(item)
        return index is not None


    def insert( self, item, slot=0 ):
        tmp = Node(item)

        prevNode = None
        curNode = self.head
        index = 0

        while curNode is not None and index < slot:
            prevNode = curNode
            curNode = curNode.nextNode
            index += 1

        tmp.nextNode = curNode

        if curNode is self.head:
            self.head = tmp
        else:
            prevNode.nextNode = tmp

        # Update the tail reference if the function is appending to the end of
        # the list.
        if prevNode is self.tail:
            self.tail = tmp

        self.size += 1


    def getTail( self ):
        assert self.tail is not None, 'The list is empty.'
        return self.tail.item


    def getHead( self ):
        assert self.head is not None, 'The list is empty.'
        return self.head.item


    def remove( self, item ):
        prevNode = None
        curNode = self.head

        while curNode is not None and curNode.item != item:
            prevNode = curNode
            curNode = curNode.nextNode

        assert curNode is not None, 'The item must be in the list.'

        if curNode is self.head:
            self.head = curNode.nextNode
        else:
            prevNode.nextNode = curNode.nextNode

        if curNode is self.tail:
            self.tail = prevNode

        self.size -= 1


    def clear( self ):
        for item in self:
            self.remove(item)


    def get( self, slot ):
        curNode = self.head
        index = 0

        while curNode is not None and index != slot:
            index += 1
            curNode = curNode.nextNode

        return curNode.item if (curNode is not None) else None


    def search( self, item ):
        curNode = self.head
        slot = 0

        while curNode is not None and curNode.item != item:
            slot += 1
            curNode = curNode.nextNode

        return slot if (curNode is not None) else None


class Node:


    def __init__( self, item ):
        self.item = item
        self.nextNode = None


class LinkedListIterator:

    
    def __init__( self, head ):
        self.curNode = head


    def __iter__( self ):
        return self


    def __next__( self ):
        if self.curNode is not None:
            item = self.curNode.item
            self.curNode = self.curNode.nextNode
            
            return item

        else:
            raise StopIteration


def main():
    myList = LinkedList()

    myList.insert('mau')
    myList.insert('ben')
    myList.insert('dalia', 0)
    myList.insert('clarky', 3)
    myList.insert('drago', 2)
    myList.insert('javier', 7)
    
    # print('Index of "ben": ' + str(myList.search('ben')))
    # print('Index of "drago": ' + str(myList.search('drago')))
    # myList.remove('clarky')
    # myList.remove('mau')
    # myList.remove('javier')
    print(myList.getHead())
    print(myList.getTail())

    for item in myList:
        print(item, end='   ')

    print()

if __name__ == '__main__':
    main()
