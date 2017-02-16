#implementation of the set ADT using the sorted list
class Set:
    #creates an empty set instance
    def __init__(self):
        self._theElements = list()

    def __len__(self):
        return len(self._theElements)

    def __contains__(self, element):
        ndx = self._findPosition(element)
        return ndx < len(self) and self._theElements[ndx] == element

    def add(self, element):
        if element not in self: #O(logn)
            ndx = self._findPosition(element) #O(logn)
            self._theElements.insert(ndx, element) #O(n)
            #O(logn+logn+n) -> O(n)

    def remove(self, element):
        assert element in self, "Element must be in the set"
        #O(logn)
        ndx = self._findPosition(element)
        #O(logn)
        self._theElements.pop(ndx)#O(n)
        #O(n) + O(logn) + O(logn) -> O(n)

    def isSubsetOf(self, setB):
        for element in self:
            if element not in setB:
                return False
        return True

    #remaining method here

    def __iter__(self):
        return _SetIterator(self._theElements)

    def _findPosition(self, element):
        low = 0
        high = len(theList) - 1
        while low <= high:
            mid = (high + low)/2
            if theList[mid] == target:
                return mid
            elif target < theList[mid]:
                high = mid - 1
            else:
                low = mid + 1
        return low

