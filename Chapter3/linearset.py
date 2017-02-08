class Set:
    #creates an empty set
    def __init__(self):
        self._theElements = list()

    def __len__(self):
        return len(self._theElements)

    def __contains__(self, element):
        return element in self._theElements

    def add(self, element):
        if element not in self:
            self._theElements.append(element)

    def remove(self, element):
        assert element in self, "The element must be in the set."
        self._theElements.remove(element)

    def __eq__(self, setB):
        if len(self) != len(setB):
            return False
        else:
            return self.isSubsetOf(setB)
    #determinse if this set is subset of setB
    def isSubsetOf(self, setB):
        for element in self:
            if element not in setB:
                return False
        return True

    def union(self, setB):
        newSet = Set()
        newSet._theElements.extend(self._theElements)
        for element in setB:
            if element not in self:
                newSet._theElements.append(element)
        return newSet

    def interset(self, setB):
        newSet = Set()
        for element in self:
            if element in setB:
                newSet._theElements.append(element)
        return newSet

    #creates the difference self set and setB
    def difference(self, setB):
        newSet = Set()
        for element in self:
            if element not in setB:
                newSet._theElements.append(element)
        return newSet

    def __iter__(self):
        return _SetIterator(self._theElements)


class _SetIterator:
    def __init__(self, setElements):
        self._elements = setElements
        self._index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._index < len(self._elements):
            element = self._elements[self._index]
            self._index += 1
            return element
        else:
            raise StopIteration
