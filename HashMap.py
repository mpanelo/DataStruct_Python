class HashMap:

    # Global variable(s) used to maintain readable code.

    # If an entry in the hash table is None, then it is equivalent to being
    # EMPTY.
    EMPTY = None

    # Initialize an empty hash table of the given size, and a count variable
    # to keep track of the nubmer of current items in the hash table.
    #
    # The fixed-size must be a prime number.
    def __init__( self, size ):
        self.hashTable = [None] * size
        self.count = 0


    # Returns the current number of items in the hash table.
    def __len__( self ):
        return self.count


    def __iter__( self ):
        return HashMapIterator( self.hashTable )


    def __contains__( self , key ):
        index = self.findIndex(key, inserting=False)
        return index is not None


    def set( self, key, value ):
        # If the given key is contained in the hash table, search for the index
        # of the HashEntry that contains the key and update the value of the
        # HashEntry.
        if key in self:
            index = self.findIndex(key, inserting=False)
            self.hashTable[index].value = value
        # If the key is not in the hash table, search for an EMPTY slot and
        # place a new HashEntry in the EMPTY slot.
        else:
            index = self.findIndex(key, inserting=True)

            # If the search for an EMPTY slot returns None, then the hash table
            # is full.
            if index is None:
                return False

            self.hashTable[index] = HashEntry(key, value)
            self.count += 1
        
        return True

    
    def get( self, key ):
        index = self.findIndex(key, inserting=False)

        if index is not None:
            return self.hashTable[index].value
        else:
            return None

    
    def delete( self, key ):
        index = self.findIndex(key, inserting=False)

        if index is not None:
            value, self.hashTable[index].value = \
            self.hashTable[index].value, None

            return value

        else:
            return None


    def load( self ):
        return self.count / len(self.hashTable)


    # Helper function used to find an appropriate index.
    # The parameter 'inserting' should hold a boolean value.
    def findIndex( self, key, inserting ):
        index = self.hashFunc1(key)
        offset = self.hashFunc2(key)

        while True:

            # If performing an insertion, return the index of the first 
            # encountered EMPTY slot.
            if inserting and self.hashTable[index] is self.EMPTY:
                return index
            # If not performing an insertion, and an EMPTY slot is encountered,
            # then no such index exists for the given key.
            elif not inserting and self.hashTable[index] is self.EMPTY:
                return None
            # Return the index of the HashEntry that contains the same key as
            # the given key.
            elif not inserting and self.hashTable[index].key == key:
                return index

            # Increment the index.
            index = (index + offset) % len(self.hashTable)
            
            # This check is needed because this implementation of HashMap does
            # not have a rehash function, so if the hash table is full there
            # will be no encounter of EMPTY slots.
            if index == self.hashFunc1(key):
                return None


    # Double hashing is used to map the items.
    # These two hash functions were taken from:
    # http://cseweb.ucsd.edu/~kube/cls/100/Lectures/lec16/lec16-23.html
    #
    # The first hash function returns the home index for the item.
    def hashFunc1( self, key ):
        K = abs(hash(key))
        M = len(self.hashTable)
        
        return K % M

    # The second hash function returns the offset value for creating the next
    # index when probing.
    def hashFunc2( self, key ):
        K = abs(hash(key))
        M = len(self.hashTable)

        return 1 + ((K // M) % (M - 1))


class HashEntry:

    def __init__( self, key, value ):
        self.key = key
        self.value = value


class HashMapIterator:

    def __init__( self, items ):
        self.hashMapItems = []

        for hashEntry in items:
            if hashEntry is not None:
                self.hashMapItems.append(hashEntry)
        
        self.current = 0


    def __iter__( self ):
        return self

    
    def __next__( self ):
        if self.current < len(self.hashMapItems):
            item = self.hashMapItems[self.current]
            self.current += 1

            return (item.key, item.value)

        else:
            raise StopIteration


def main():

    myHashMap = HashMap(7)

    # myHashMap.set(12, '12')
    myHashMap.set(100, '100')
    # myHashMap.set(30, '30')
    myHashMap.set(58, '58')
    myHashMap.set(17, '17')
    myHashMap.set(1, '1')
    # myHashMap.set(36, '36')
    myHashMap.set(22, '22')

    print('The value of 1: ' + myHashMap.get(1))
    print('Delete the value of 17: ' + myHashMap.delete(17))

    print('Current load: ' + str(myHashMap.load()))

    for key, value in myHashMap:
        print('Key: ' + str(key).ljust(20) + 'Value: ' + str(value))


if __name__ == '__main__':
    main()
