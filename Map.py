class Map:

    def __init__( self ):
        self.entryList = list()

	
    def __len__( self ):
        return len(self.entryList)

    
    def __contains__( self, key):
        ndx = self.findPosition(key)

        return ndx is not None


    def __setitem__( self, key, value ):
        ndx = self.findPosition(key)

        if ndx is not None:
            self.entryList[ndx].value = value
        else:
            self.entryList.append( _MapEntry(key, value) )


    def __getitem__( self, key ):
        ndx = self.findPosition(key)
        assert ndx is not None, "Invalid map key."

        return self.entryList[ndx].value

        
    def remove( self, key ):
        ndx = self.findPosition(key)
        assert ndx is not None, "Invalid map key."

        del self.entryList[ndx]


    def __iter__( self ):
        return _MapIterator( self.entryList )


    def findPosition( self, key ):

        for i in range(len(self)):

            if self.entryList[i].key == key:
                return i

        return None


class _MapEntry:

    def __init__( self, key, value ):
        self.key = key
        self.value = value


class _MapIterator:

    def __init__( self, items ):
        self.mapItems = items
        self.currentIndex = 0


    def __iter__( self ):
        return self


    def __next__( self ):
        if self.currentIndex < len(self.mapItems):
            item = self.mapItems[ self.currentIndex ]
            self.currentIndex += 1
            return (item.key, item.value)
        else:
            raise StopIteration


def main():
    myMap = Map()

    myMap['Name'] = 'Mauricio Panelo'
    myMap['Age'] = 21
    myMap['Birthday'] = '16-11-1994'
    myMap['Girlfriend'] = 'Dalia Tafoya'

    for key, value in myMap:
        print('Key: ' + str(key).ljust(20) + 'Value: ' + str(myMap[key]))
    
    myMap['Age'] = 22
    print('\nName in myMap: ' + str('Name' in myMap) + '\n')
    # print('Age' in myMap)
    # print('Ag' in myMap)

    myMap.remove('Girlfriend')
    # print('Girlfriend' in myMap)
    # print(myMap['Age'])

    for key, value in myMap:
        print('Key: ' + str(key).ljust(20) + 'Value: ' + str(value))


if __name__ == '__main__':
    main()
