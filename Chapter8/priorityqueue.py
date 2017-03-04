#Unbounded Priority Queue ADT using list
class PriorityQueue:
    def __init__(self):
        """initlaizes a list for unbounded queue"""
        self._qList = list()

    def isEmpty(self):
        """True if queue is empty"""
        return len(self) == 0

    def __len__(self):
        return len(self._qList)
    #O(n) - but O(1) amortized cost
    def enqueue(self, item, priority):
        """New instance of storage class is created, and appended to the list"""
        entry = self._PriorityQEntry(item, priority)
        self._qList.append(entry)
    #O(n) as it transverses the list in worst possible case
    def dequeue(self):
        """Looks for the entry with highest priority and dequeue"""
        assert not self.isEmpty(), "Empty queue"
        index = 0
        highest = self._qList[index].priority
        for i in range(len(self)):
            if self._qList[i].priority < highest:
                highest = self._qList[i].priority
                index = i
        entry = self._qList.pop(index)
        return entry.item
    #__slots__ is good when many instances of the class is to be crated
    #the class should inherit object, and all of the inheritance shoulddelcare
    #__slot__ and not __dict__
    #arbirtray attributes can not be added in __slots__ unlike in __dict__ though
    class _PriorityQEntry(object):
        __slots__ = 'item', 'priority'
        def __init__(self, item, priority):
            self.item = item
            self.priority = priority
