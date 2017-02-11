# menu-driven program that uses your function from the previous ques-
tion to extract the sales data and can produce any of the following reports:
    (a) Each of the four types of reports described in the chapter.
    (b) The sales for a single store similar to that shown in Section 3.4 with the
    data sorted by total sales.
    (c) The total sales for each store sorted by total sales from largest to smallest.
    (d) The total sales for each item sorted by item number.Map ADT with list
class Map:
    def __init__(self):
        self._entryList = list()#empty list initialization

    def __len__(self):
        return len(self._entryList)

    def __contains__(self, key):
        ndx = self._findPosition(key)
        return ndx is not None

    #adds a new entry, or replace value if exists
    def add(self, key, value):
        ndx = self._findPosition(key)
        if ndx is not None: #key found
            self._entryList[ndx].value = value
            return False
        else:
            entry = _MapEntry(key,value)
            self._entryList.append(entry)
            return True

    def valueOf(self, key):#what value this key holds
        ndx = self._findPosition(key)
        assert ndx is not None, "Invalid map key"
        return self._entryList[ndx].value

    def remove(self, key):
        ndx = self._findPosition(key)
        assert ndx is not None, "Invalid map key"
        self._entryList.pop(ndx)

    def __iter__(self):
        return _MapIterator(self._entryList)

    #helper method - so private
    def _findPosition(self, key):
        for i in range(len(self)):
            if self._entryList[i].key == key:
                return i
            else:
                return None #check if key in ith element, returns None otherwise

class _MapEntry:
    def __init__(self, key, value):
        self.key = key
        self.value = value

class _MapIterator:
    def __init__(self, entryList):
        self._entryList = entryList
        self._index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._index < len(self._entryList):
            element = self._entryList[self._index]
            self._index += 1
            return element
        else:
            raise StopIteration
