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

    def enqueue(self, item, priority):
        """New instance of storage class is created, and appended to the list"""
        entry = self._PriorityQEntry(item, priority)
        self._qList.append(entry)

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

    class _PriorityQEntry(object):
        def __init__(self, item, priority):
            self.item = item
            self.priority = priority
